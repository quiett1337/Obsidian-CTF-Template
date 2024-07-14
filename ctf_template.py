#!/usr/bin/python3
import os
import time
import sys




def thm():
    ctf_name = input("CTF Name: ")
    os.mkdir("THM/"+ctf_name)
    
    #nmap
    os.mkdir('THM/'+ctf_name+'/nmap')
    initial = open('THM/'+ctf_name+'/nmap/initial.md', 'a')
    All = open('THM/'+ctf_name+'/nmap/all.md', 'a')
    udp = open('THM/'+ctf_name+'/nmap/udp.md', 'a')
    script = open('THM/'+ctf_name+'/nmap/script.md', 'a')
    
    #general info
    info = open('THM/'+ctf_name+'/info.md', 'a')
    
    #port 80 [http]
    os.mkdir('THM/'+ctf_name+'/port80_http')
    http_info = open('THM/'+ctf_name+'/port80_http/info.md', 'a')
    directories = open('THM/'+ctf_name+'/port80_http/directories.md', 'a')
    
    #port 22 [ssh] 
    os.mkdir('THM/'+ctf_name+'/port22_ssh')
    http_info = open('THM/'+ctf_name+'/port22_ssh/info.md', 'a')
    
    
    
    
    
    
def htb():
    ctf_name = input("CTF Name: ")
    os.mkdir("HTB/"+ctf_name)
    
    #nmap
    os.mkdir('HTB/'+ctf_name+'/nmap')
    initial = open('HTB/'+ctf_name+'/nmap/initial.md', 'a')
    All = open('HTB/'+ctf_name+'/nmap/all.md', 'a')
    udp = open('HTB/'+ctf_name+'/nmap/udp.md', 'a')
    script = open('HTB/'+ctf_name+'/nmap/script.md', 'a')
    
    #general info
    info = open('HTB/'+ctf_name+'/info.md', 'a')
    
    #port 80 [http]
    os.mkdir('HTB/'+ctf_name+'/port80_http')
    http_info = open('HTB/'+ctf_name+'/port80_http/info.md', 'a')
    directories = open('HTB/'+ctf_name+'/port80_http/directories.md', 'a')
    
    #port 22 [ssh] 
    os.mkdir('HTB/'+ctf_name+'/port22_ssh')
    http_info = open('HTB/'+ctf_name+'/port22_ssh/info.md', 'a')
    
    
    
def pg():
    ctf_name = input("CTF Name: ")
    os.mkdir("PG/"+ctf_name)
    
    #nmap
    os.mkdir('PG/'+ctf_name+'/nmap')
    initial = open('PG/'+ctf_name+'/nmap/initial.md', 'a')
    All = open('PG/'+ctf_name+'/nmap/all.md', 'a')
    udp = open('PG/'+ctf_name+'/nmap/udp.md', 'a')
    script = open('PG/'+ctf_name+'/nmap/script.md', 'a')
    
    #general info
    info = open('PG/'+ctf_name+'/info.md', 'a')
    
    #port 80 [http]
    os.mkdir('PG/'+ctf_name+'/port80_http')
    http_info = open('PG/'+ctf_name+'/port80_http/info.md', 'a')
    directories = open('PG/'+ctf_name+'/port80_http/directories.md', 'a')
    
    #port 22 [ssh] 
    os.mkdir('PG/'+ctf_name+'/port22_ssh')
    http_info = open('PG/'+ctf_name+'/port22_ssh/info.md', 'a')



print("1. THM")
print("2. HTB")
print("3. PG")
time.sleep(2)

choice = input("which ctf: ")

if choice == "1":
    thm()
elif choice == "2":
    htb()
elif choice == "3":
    pg()
    
else:
    print("this is not an option...quitting")
    sys.exit()

