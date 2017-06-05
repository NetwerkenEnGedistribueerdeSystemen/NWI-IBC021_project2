#!/usr/local/bin/python3
import argparse
import socket

from bTCP.client import Client

# Handle arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-w", "--window", help="Define bTCP window size", type=int, default=100
)
parser.add_argument(
    "-t", "--timeout", help="Define bTCP timeout in milliseconds", type=int,
    default=100
)
parser.add_argument("-i", "--input", help="File to send", default="tmp.file")
parser.add_argument(
    "-d", "--destination", help="Define destination IP", type=str,
    default="127.0.0.1"
)
parser.add_argument(
    "-p", "--port", help="Define destination port", type=int, default=9001
)
args = parser.parse_args()

with open(args.input, "rb") as input:
    input_bytes = input.read()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client = Client(
    sock=sock,
    input_bytes=input_bytes,
    destination=args.destination,
    destination_port=args.port,
    window=args.window,
    timeout=args.timeout / 1000,
)

try:
    while client.state is not client.finished:
        client.run()
finally:
    sock.close()
