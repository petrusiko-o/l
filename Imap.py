import socket
import ssl

server = 'imap.mail.ru'
port = 993

def create_socket(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    ssl_sock = ssl.wrap_socket(sock)
    print(ssl_sock.recv(1024))
    return ssl_sock


def send_command(command, sock):
    sock.send(bytes(command + '\r\n','utf-8'))
    answer = ""
    need_recv = False
    array = command.split('\r\n')
    while True:
        if need_recv and answer.endswith('\r\n'):
            break
        for i in array:
            if i.startswith(command.split(' ')[0]):
                need_recv = True
                break
        data = sock.recv(1024).decode()
        answer += data
    print(answer)


sockt = create_socket(server,port)
send_command('AUTH LOGIN ee-tester@mail.ru bhd11hd8',sockt)
send_command('A1 SELECT Inbox',sockt)
send_command('A2 Search UNSEEN',sockt)
send_command('A3 FETCH 5 (FLAGS)',sockt)
sockt.close()