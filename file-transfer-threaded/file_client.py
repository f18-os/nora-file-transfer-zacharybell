#! /usr/bin/env python3

import argparse, pickle, socket

from models import ClientFile

## parse command line input

parser = argparse.ArgumentParser('Run a file transfer client.')

parser.add_argument('--host', help='default 127.0.0.1', default='127.0.0.1', type=str)
parser.add_argument('--port', help='default 12345', default=12345, type=int)
parser.add_argument('--file', help='the path to the file', metavar='file_path', type=str)
parser.add_argument('--name', help='the requested name for the file to be saved as', metavar='file_name', type=str)
parser.add_argument('--append', help='appends to the end of the file if file exists', default=False, action='store_true')

args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect((args.host, args.port))
    with open(args.file_path, 'rt') as f:
        ## pickle aka serialize
        file_pickle = pickle.dump(ClientFile(args.file_name, f.read(), args.append))
        soc.sendall(file_pickle)