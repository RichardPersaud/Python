import socket
from _thread import start_new_thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())

# socket.sethostname()

# host_name = socket.gethostname() 
# host_ip = socket.gethostbyname(host_name) 

port = 1248
ThreadCount = 0

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

while True:
    s.listen(5)
    print("Server listening @ {}:{}".format(host, port))

    def threaded_client(s):

        s.send(str.encode('\nWelcome to the Server'))

        while True:
            data = s.recv(2024)
            print("\n"+data.decode() + " Connected!\n")

            while True:
                msg = s.recv(2024)
                print(data.decode()+" >>> : "+msg.decode())

            if not data:
                break

            s.sendall(str.encode(data))

        s.close()

    while True:
        Client, address = s.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))

        start_new_thread(threaded_client, (Client, ))

        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

    s.close()

