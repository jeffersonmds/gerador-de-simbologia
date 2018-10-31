import pygame
import csv
import socket
import pickle

"""import math"""
"""import gerador_simbologia"""




def rotaciona_vsi(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def simbologia(label):
    res = 0
    value = [0, 0, 0, 0]
    list(reversed(label))
    """att = label[14:28]"""
    if label[14] == '1':
        value[3] = value[3] + 1
    if label[15] == '1':
        value[3] = value[3] + 2
    if label[16] == '1':
        value[3] = value[3] + 4
    if label[17] == '1':
        value[3] = value[3] + 8
    res += value[3]

    if label[18] == '1':
        value[2] = value[2] + 1
    if label[19] == '1':
        value[2] = value[2] + 2
    if label[20] == '1':
        value[2] = value[2] + 4
    if label[21] == '1':
        value[2] = value[2] + 8
    res += value[2] * 10

    if label[22] == '1':
        value[1] = value[1] + 1
    if label[23] == '1':
        value[1] = value[1] + 2
    if label[24] == '1':
        value[1] = value[1] + 4
    if label[25] == '1':
        value[1] = value[1] + 8
    res += value[1] * 100

    if label[26] == '1':
        value[0] = value[0] + 1
    if label[27] == '1':
        value[0] = value[0] + 2
    if label[28] == '1':
        value[0] = value[0] + 4
    res += value[0] * 1000

    res = res / 100
    return res


def negativ(label, res):
    if label[29] == '1' and label[30] == '1':
        res = res * (-1)
    return res


def client_program():
    angle = 0
    cont = 0
    done = False
    host = '127.0.0.1'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        data = pickle.loads(client_socket.recv(8192))
        print (data)
        if data[0:8] == ['0', '0', '0', '1', '0', '0', '0', '0']:
            angle = simbologia(data)
            angle = negativ(data, angle)
        screen.blit(background_image, background_position)
        screen.blit(rotaciona_vsi(seta, angle * (-1)), background_position)
        print(angle, " ", cont)
        cont += 1
        pygame.display.flip()
        clock.tick(10000)

        if cont == 10000:
            done = True

    pygame.quit()
    client_socket.close()  # close the connection


if __name__ == '__main__':
    pygame.init()

    # 400x400 sized screen
    screen = pygame.display.set_mode([400, 400])

    # This sets the name of the window
    pygame.display.set_caption('Indicador de Velocidade Vertical')

    clock = pygame.time.Clock()
    background_position = [0, 0]

    # Load and set up graphics.
    background_image = pygame.image.load("indicador.png")  # .convert()
    seta = pygame.image.load("seta_vsi.png")
    client_program()
