#! /usr/bin/env python3

import argparse, pickle, os, socket
from threading import Thread, Lock

from framedSock import FramedStreamSock

FILE_STORAGE_DIR = 'storage'

## parse command line input

parser = argparse.ArgumentParser('Run a file transfer server.')

parser.add_argument('--host', help='default 127.0.0.1', metavar='host', default='127.0.0.1', type=str)
parser.add_argument('--port', help='default 12345', metavar='port', default=12345, type=int)
parser.add_argument('--max', help='the maximum clients', metavar='n_clients', default=None)
parser.add_argument('--debug', metavar='debug', default=False)

args = parser.parse_args()


class FileServerThread(Thread):

    _lock = Lock()

    def __init__(self, soc, debug):
        Thread.__init__(self, daemon=True)
        self.fsock, self.debug = FramedStreamSock(sock, debug), debug
        self.start()
    
    def run(self):
        while True:    
            message = self.fsock.receivemsg()
            if not message: return

            client_file_model = pickle.loads(message)

            with self._lock:
                with open(os.path.join(FILE_STORAGE_DIR, client_file_model.file_name), 'ab') as f:
                    f.write(client_file_model.contents)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lsock:
    lsock.bind((args.host, args.port))
    if args.n_clients:
        lsock.listen(args.n_clients)
    else:
        lsock.listen()
    while True:
        sock, _ = lsock.accept()
        FileServerThread(sock, args.debug)
