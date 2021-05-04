import hashlib, base64, random, sys, argparse, os, time

parser = argparse.ArgumentParser(description="Convert line-seperated strings into a hash for rainbow tables. Valid hashing methods are sha1, sha256, sha384, sha512, sha3_512, md5 and shake_128.")
parser.add_argument('method', type=str, help='Hashing method') # define the hash method to use
parser.add_argument('input', type=str, help='Input file') # define the source file
parser.add_argument('output', type=str, help='Output file') # define the output file
args = parser.parse_args()
hash_method = str(args.method)
input_file = str(args.input)
output_file = str(args.output)

def identifyMethod(string):
    if hash_method == "sha1": # hash with the sha1 method
        hash_object = hashlib.sha1((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if hash_method == "sha256": # hash with the sha256 method
        hash_object = hashlib.sha256((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if hash_method == "sha384": # hash with the sha384 method
        hash_object = hashlib.sha384((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if hash_method == "sha512": # hash with the sha512 method
        hash_object = hashlib.sha512((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if hash_method == "sha3_512": # hash with the sha3_512 method
        hash_object = hashlib.sha3_512((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
        
    if hash_method == "md5": # hash with the md5 method
        hash_object = hashlib.md5((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    if hash_method == "shake_128": # hash with the shake_128 method
        hash_object = hashlib.shake_128((string).encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig

start_time = time.perf_counter()
counter = 1 # init the counter
print("Text2Hash")
with open (input_file, "r") as fileHandler:
    for line in fileHandler:
        string = line.strip()
        hashed = identifyMethod(string)
        print("{} | {}:{}".format(counter, string, hashed))
        counter = counter+1 # increase the counter by one
        with open(output_file, "a") as output:
            output.write("{}:{}\n".format(string, hashed))
finish_time = time.perf_counter()
total_time = int(finish_time) - int(start_time)
print("Successfully hashed {} strings in {} seconds!".format(counter, total_time))
print("Output is available in {}".format(output_file))
