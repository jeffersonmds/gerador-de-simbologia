import pygame
import csv
import socket
import pickle


def rotaciona_vsi(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def simbologia(label):
    res = 0
    value = [0, 0, 0]
    list(reversed(label))

    if label[18] == '1':
        value[2] = value[2] + 1
    if label[19] == '1':
        value[2] = value[2] + 2
    if label[20] == '1':
        value[2] = value[2] + 4
    if label[21] == '1':
        value[2] = value[2] + 8
    res += value[2] * 1

    if label[22] == '1':
        value[1] = value[1] + 1
    if label[23] == '1':
        value[1] = value[1] + 2
    if label[24] == '1':
        value[1] = value[1] + 4
    if label[25] == '1':
        value[1] = value[1] + 8
    res += value[1] * 10

    if label[26] == '1':
        value[0] = value[0] + 1
    if label[27] == '1':
        value[0] = value[0] + 2
    if label[28] == '1':
        value[0] = value[0] + 4
    res += value[0] * 100

    res = res
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
        if data[0:8] == ['0', '0', '0', '1', '0', '1', '1', '0']:
            angle = simbologia(data)
        screen.blit(background_image, background_position)
        screen.blit(rotaciona_vsi(seta, (angle * (-1)) * 1.395), background_position)
        cont += 1
        pygame.display.flip()
        clock.tick(10000)

        if cont == 40000:
            done = True

    pygame.quit()
    client_socket.close()  # close the connection


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode([600, 600])

    # This sets the name of the window
    pygame.display.set_caption('Indicador de Velocidade')

    clock = pygame.time.Clock()
    background_position = [0, 0]

    # Load and set up graphics.
    background_image = pygame.image.load("asi_background.png")  # .convert()
    seta = pygame.image.load("asi_seta.png")
    client_program()
