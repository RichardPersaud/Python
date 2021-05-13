import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 192.168.30.50 | 10.0.0.174 | zooboo.ddns.net | 196.53.217.231 | oojjs.ddns.net
host = 'zooboo.ddns.net'  # The IP printed by the server must be set here
port =  53128

# host = socket.gethostbyname(link)

def send():
    sys = s.recv(2024)
    print(sys.decode() +" : "+ username+"\n")

    while True:
        # ----------------------------
        # sending msg to server
        message = input(username+" >>>: ")
        # encoding the msg before to send
        s.send(message.encode())

    # -----------------------------
    # Receive data from server
    response = s.recv(2024)
    # Print to the console
    print(response.decode())
    






# ===================================================================
# ===================================================================
try:
    print("Connecting to {}:{}".format(host, port))
    s.connect((host, port))
    print("\nSuccessfully Connected!\n")

    username = input("Enter Username: ")
    s.send(username.encode())

    send() #calls the method above ^


except ConnectionRefusedError as e:
    print(str(e))
    input("C.R.E ERROR!....")

except OSError as o:
    print(str(o))
    input("O.S ERROR...")

except:
    print(username+" has left the server!")