import csv
import socket
import msvcrt
import pickle
import pygame


def server_program():
    # get the hostname
    host = ''
    port = 5000  # initiate port no above 1024
    cont = 0
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    print("Waiting for connections...")
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    # conn2, address2 = server_socket.accept()
    print("Connection from: " + str(address))
    # print("Connection from: " + str(address2))
    input("Press Enter to send data...")

    while True:
        data = pickle.dumps(inf[cont])
        conn.send(data)  # send data to the client
        # conn2.send(data)
        print(inf[cont])
        cont += 1
        clock.tick(96)

    conn.close()  # close the connection


if __name__ == '__main__':
    clock = pygame.time.Clock()
    csv_inf = open("entrada de dados_VSI.csv")
    file = csv.reader(csv_inf)
    inf = []
    for row in file:
        inf.append(list(reversed(row[0].replace('\t', ''))))
    server_program()
