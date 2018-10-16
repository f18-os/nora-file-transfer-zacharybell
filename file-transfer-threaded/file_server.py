#! /usr/bin/env python3

import argparse, socket

## parse command line input

parser = argparse.ArgumentParser('Run a file transfer server.')

parser.add_argument('--host', help='default 127.0.0.1', metavar='host', default='127.0.0.1', type=str)
parser.add_argument('--port', help='default 12345', metavar='port', default=12345, type=int)
parser.add_argument('--max', help='the maximum clients', metavar='n_clients', default=None)

args = parser.parse_args()

