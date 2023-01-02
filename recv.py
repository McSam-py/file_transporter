import socket
import sys
import os

lhost = sys.argv[1]  # Taking the ip address to listen on
lport = int(sys.argv[2])  # Taking the port to listen on

sock = socket.socket()  # Creating socket object
sock.bind((lhost, lport))  # bind the lhost to the lport

sock.listen(2)
print("[!] Listening for incoming connections")

conn, addr = sock.accept()
print(f"[+] Connection from {addr[0]} on port {addr[1]}")


def receive_data():
    received_info = []
    while True:
        data = conn.recv(1024).decode('utf-8', 'ignore')
        # print(data)
        if data:
            received_info.append(data)

            if data.strip() == "[..] Sending File":
                file_name = received_info[0].split(
                    '\n')[0].split(":")[1].strip()
                file_size = received_info[0].split(
                    '\n')[1].split(":")[1].strip()
                current_file_size = 0

                print(received_info[0])

                with open(file_name, 'ab') as file_bytes_object:
                    while current_file_size != int(file_size):
                        newdata = conn.recv(1024)
                        file_bytes_object.write(newdata)
                        current_file_size = file_bytes_object.seek(
                            0, os.SEEK_END)

                print("[+] File received successfully")
                break

        else:
            pass


receive_data()
sock.close()  # Close socket connection
