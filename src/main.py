from config import parser
from readers.imap import IMAPReader

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    reader = IMAPReader("alvie.zhang@gmail.com", "demdzllugjusifnj", "imap.gmail.com")
    i = reader.iter()
    m = next(i)
    with open("/Users/alvie/Downloads/test.html", "wb") as f:
        f.write(m.as_bytes())
    print(m)
    # print(next(i))
