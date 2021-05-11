# hashed 466549 words in 447 seconds on a Dell Lattitude E7250 using sha512
import hashlib, sys, argparse, time
from datetime import datetime
from hashlib import *

parser = argparse.ArgumentParser(description="Convert line-seperated strings into a hash for rainbow tables. Valid hashing methods are sha1, sha256, sha384, sha512, sha3_512, md5, shake_128, shake_256, blake2b and blake2s.")
parser.add_argument('method', type=str, help='Hashing method') # define the hash method to use
parser.add_argument('input', type=str, help='Input file') # define the source file
parser.add_argument('output', type=str, help='Output file') # define the output file
parser.add_argument('seperator', type=str, help='Character used to seperate the string and hash') # define the seperating character
args = parser.parse_args()

def identifyMethod(string): # find out what algorithm the user wants to choose
    if str(args.method) == "sha1": # hash with the sha1 method
        hash_object = hashlib.sha1((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if str(args.method) == "sha256": # hash with the sha256 method
        hash_object = hashlib.sha256((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if str(args.method) == "sha384": # hash with the sha384 method
        hash_object = hashlib.sha384((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if str(args.method) == "sha512": # hash with the sha512 method
        hash_object = hashlib.sha512((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if str(args.method) == "sha3_512": # hash with the sha3_512 method
        hash_object = hashlib.sha3_512((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
        
    if str(args.method) == "md5": # hash with the md5 method
        hash_object = hashlib.md5((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if str(args.method) == "shake_128": # hash with the shake_128 method
        hash_object = hashlib.shake_128((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if str(args.method) == "shake_256": # hash with the shake_256 method
        hash_object = hashlib.shake_256((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if str(args.method) == "blake2b": # hash with the blake2b method
        hash_object = hashlib.blake2b((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if str(args.method) == "blake2s": # hash with the blake2s method
        hash_object = hashlib.blake2s((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    else: # invalid option
        return "Unknown value passed!"

start_time = time.perf_counter()
counter = 0 # init the counter
print("Text2Hash -- Created by SkryptKiddie\nShared under the GNU General Public License v3.0")
with open(str(args.output), "a+") as output: # initialise the file so we don't have to use a+ during the hash method, which makes the program run much faster. also creates the output file if it doesn't already exist.
    output.write("Generated at {} using the {} algorithm with text from {}\n\n".format(datetime.now(), str(args.method), str(args.input)))
    output.close()

with open (str(args.input), "r") as fileHandler:
    for line in fileHandler:
        string = line.strip()
        hashed = identifyMethod(string)
        print("{} | {}{}{}".format(counter, string, str(args.seperator), hashed)) # print the output as we save it into the file
        counter = counter+1 # increase the counter by one
        with open(str(args.output), "a") as output:
            output.write("{}:{}\n".format(string, hashed)) 
    output.close()
            
finish_time = time.perf_counter()
total_time = int(finish_time) - int(start_time)
print("Successfully hashed {} strings in {} seconds!".format(counter, total_time))
print("Output is available in {}".format(str(args.output)))
