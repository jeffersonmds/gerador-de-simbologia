import csv
import socket
import msvcrt
import pickle
import pygame


def server_program():
    host = ''
    port = 5000  # porta inicializada
    cont = 0
    server_socket = socket.socket()
    server_socket.bind((host, port))  # bind host address and port together

    # configuração de quantos clientes o servidor poderá interagir simultaneamente
    print("Waiting for connections...")
    server_socket.listen(3)
    conn, address = server_socket.accept()  # aceitar conexão
    conn2, address2 = server_socket.accept()
    conn3, address3 = server_socket.accept()
    print("Connection from: " + str(address))
    print("Connection from: " + str(address2))
    print("Connection from: " + str(address3))
    input("Press Enter to send data...")

    while True:
        data = pickle.dumps(inf[cont])
        # enviar dados para os clientes
        conn.send(data)
        conn2.send(data)
        conn3.send(data)
        print(inf[cont])
        cont += 1
        clock.tick(300)


if __name__ == '__main__':
    clock = pygame.time.Clock()
    csv_inf = open("entrada de dados_VSI.csv")
    csv_inf2 = open("entrada_de_dados_ALT.csv")
    csv_inf3 = open("entrada de dados_ASI.csv")
    file = csv.reader(csv_inf)
    file2 = csv.reader(csv_inf2)
    file3 = csv.reader(csv_inf3)
    inf = list(range(0, 30003))
    cont = 0
    for row in file:
        inf[cont] = (list(reversed(row[0].replace('\t', ''))))
        cont += 3
    cont = 1
    for row in file2:
        inf[cont] = (list(reversed(row[0].replace('\t', ''))))
        cont += 3
    cont = 2
    for row in file3:
        inf[cont] = (list(reversed(row[0].replace('\t', ''))))
        cont += 3
    server_program()
