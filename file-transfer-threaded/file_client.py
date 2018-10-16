#! /usr/bin/env python3

import argparse, socket

## parse command line input

parser = argparse.ArgumentParser('Run a file transfer client.')

parser.add_argument('--host', help='default 127.0.0.1', default='127.0.0.1', type=str)
parser.add_argument('--port', help='default 12345', default=12345, type=int)
parser.add_argument('--file', help='the path to the file', metavar='file_path', type=str)
parser.add_argument('--name', help='the requested name for the file to be saved as', metavar='file_name', type=str)
parser.add_argument('--append', help='appends to the end of the file if file exists', default=False, action='store_true')

args = parser.parse_args()

