import os, sys, argparse, binascii
from sys import exit

parser = argparse.ArgumentParser(description="DMR radio encryption key generator tool")
parser.add_argument("KeyType", help="basic, enhanced or both (case-sensitive)")
args = parser.parse_args()

def keyGeneration(len):
    return str(binascii.b2a_hex(os.urandom(len)))[2:-1]

try:
    if str(args.KeyType) == "basic":
        print("Basic key: " + keyGeneration(2))
        sys.exit()

    if str(args.KeyType) == "enhanced":
        print("Enhanced key: " + keyGeneration(16))
        sys.exit()

    if str(args.KeyType) == "both":
        print("Basic key: " + keyGeneration(2))
        print("Enhanced key: " + keyGeneration(16))
        sys.exit()

    else:
        print("Invalid option! Must be basic, enhanced or both")
        sys.exit()
except:
    sys.exit()
