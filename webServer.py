import http, os, sys # tested on python 3.8.5
from http.server import HTTPServer, CGIHTTPRequestHandler

IP=("127.0.0.1") # local web server IP
PORT=(80) # local web server port
WWW=("joshek-www/") # directory where files are stored
address=(str(IP), PORT) # combined variables for httpServer
serverURL=("http://"+str(IP)+":"+(str(PORT))) # prettyprint the http server URL

httpServer = HTTPServer(server_address=(IP, PORT), RequestHandlerClass=CGIHTTPRequestHandler) # defines the httpServer object
os.chdir(WWW) # set current directory as set in the WWW variable
print("URL: " + str(serverURL)) # prints a url to the webserver
print("WWW folder: " + str(os.getcwd())) # current directory
print("WWW files: " + str(os.listdir("."))) # list files in current directory

try:
    print("Starting HTTP server, stop with ^C \n")
    httpServer.serve_forever()
except KeyboardInterrupt:
    print("Stopping...")
    exit()
