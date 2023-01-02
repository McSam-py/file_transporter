import sys
import socket
import os
import time

if len(sys.argv) != 3 or sys.arv[1] == "help" or sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("""Usage:
    python3 send.py <server_to_send_file_to> <port_of_destination_server> <full_path_to_file>\n
Example:
    python3 send.py 192.168.34.1 8989 /root/Desktop/test.jpg
        """)
    sys.exit()

lhost = sys.argv[1]
lport = int(sys.argv[2])
file_path = sys.argv[3]


def get_image_bytes(path):
    with open(path, "rb") as file_bytes_object:
        file_bytes = file_bytes_object.read()
        file_size = file_bytes_object.seek(0, os.SEEK_END)

    file_name = path.split("/")[-1]
    return file_bytes, file_size, file_name


def send_image_bytes(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    file_bytes_to_send, file_size_to_send, file_name_to_send = get_image_bytes(
        file_path)

    sock.send(
        (f"File Name: {file_name_to_send}\nFile Size: {file_size_to_send}").encode())

    print(f"File Name: {file_name_to_send}\nFile Size: {file_size_to_send}")

    send_data = input("\nEnter yes if you want to send the file: (yes/no) ")

    if send_data.lower() == "yes":
        sock.send(("[..] Sending File").encode())
        bytes_sent = 1024
        start_bytes = 0

        for i in range((file_size_to_send // 1024) + 1):
            time.sleep(0.05)
            sock.send(file_bytes_to_send[start_bytes:bytes_sent])
            start_bytes = bytes_sent
            bytes_sent *= 2

    else:
        print("[-] Closing program..")
        sys.exit()


send_image_bytes(lhost, lport)
