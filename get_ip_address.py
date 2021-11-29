import socket
hostname = socket.gethostname()
name = socket.gethostbyname(hostname)
print(f'O nome do seu Computador: {hostname}')  # retorna o nome da maquina
print(f'O IP do seu computador na rede: {name}')  # retorna o IP da maquina
