#import pwn tools and sys
from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid arguments!")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()

wantedHash = sys.argv[1]
passwordFile = "rockyou.txt"
attempts = 0

#use log.progress from pwn tools to crack the hash
with log.progress("Attempting to crack: {}!\n".format(wantedHash)) as p:
    with open(passwordFile, "r", encoding='latin-1') as passwordList: #open password file
        for password in passwordList: #iterate through password file
            password = password.strip("\n").encode('latin-1') #strip new line and encode to match password list file
            passwordHash = sha256sumhex(password) #compare via sha256 in hex
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), passwordHash)) #list progress statistics
            if passwordHash == wantedHash:
                #if comparison = true, print the password and hash
                p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts,password.decode('latin-1'), passwordHash))
                exit()
            attempts += 1
        p.failure("Password hash not found!")