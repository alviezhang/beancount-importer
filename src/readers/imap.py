import base64
import email
import imaplib
import re


class IMAPReader:
    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        port: int = 993,
    ) -> None:
        self.server = imaplib.IMAP4_SSL(host=host, port=port)
        self.credentials = {
            "user": user,
            "password": password,
        }

    def iter(self):
        self.server.login(**self.credentials)
        self.server.select("Bank/CMB")

        ok, mail_list = self.server.search(None, "ALL")
        if ok != "OK":
            raise RuntimeError(f"IMAP server returned {ok}")

        for uid in reversed(mail_list[0].split(b" ")):
            yield self.fetch_content(uid)

    def fetch_content(self, uid):
        response = self.server.fetch(uid, "(RFC822)")
        if response[0] != "OK":
            raise RuntimeError(f"IMAP server returned {response[0]}")

        body = response[1][0][1]
        message = email.message_from_bytes(body, policy=email.policy.email)
        return message
