import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", dest="reader", type=str)
parser.add_argument("-s", dest="server", type=str)
parser.add_argument("-p", dest="port", type=int)
