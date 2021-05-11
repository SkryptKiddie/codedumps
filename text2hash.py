import hashlib, base64, random, sys, argparse, os, time

parser = argparse.ArgumentParser(description="Convert line-seperated strings into a hash for rainbow tables. Valid hashing methods are sha1, sha256, sha384, sha512, sha3_512, md5 and shake_128.")
parser.add_argument('method', type=str, help='Hashing method') # define the hash method to use
parser.add_argument('input', type=str, help='Input file') # define the source file
parser.add_argument('output', type=str, help='Output file') # define the output file
parser.add_argument('seperator', type=str, help='Character used to seperate the string and hash') # define the seperating character
args = parser.parse_args()
hash_method = str(args.method)
input_file = str(args.input)
output_file = str(args.output)
div_char = str(args.seperator)

def identifyMethod(string): # find out what algorithm the user wants to choose
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
    
    else: # invalid option
        return "Unknown value passed!"
        sys.exit()

start_time = time.perf_counter()
counter = 0 # init the counter
print("Text2Hash")
with open (input_file, "r") as fileHandler:
    for line in fileHandler:
        string = line.strip()
        hashed = identifyMethod(string)
        print("{} | {}{}{}".format(counter, string, div_char, hashed))
        counter = counter+1 # increase the counter by one
        with open(output_file, "a") as output:
            output.write("{}:{}\n".format(string, hashed))
            
finish_time = time.perf_counter()
total_time = int(finish_time) - int(start_time)
print("Successfully hashed {} strings in {} seconds!".format(counter, total_time))
print("Output is available in {}".format(output_file))
