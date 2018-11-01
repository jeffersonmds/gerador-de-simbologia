import pygame
import csv
import socket
import pickle


def rotaciona_alt(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def simbologia(label):
    res = 0
    value = [0, 0, 0, 0, 0]
    list(reversed(label))
    """10 ao 13"""
    if label[10] == '1':
        value[4] = value[4] + 1
    if label[11] == '1':
        value[4] = value[4] + 2
    if label[12] == '1':
        value[4] = value[4] + 4
    if label[13] == '1':
        value[4] = value[4] + 8
    res += value[4]

    if label[14] == '1':
        value[3] = value[3] + 1
    if label[15] == '1':
        value[3] = value[3] + 2
    if label[16] == '1':
        value[3] = value[3] + 4
    if label[17] == '1':
        value[3] = value[3] + 8
    res += value[3] * 10

    if label[18] == '1':
        value[2] = value[2] + 1
    if label[19] == '1':
        value[2] = value[2] + 2
    if label[20] == '1':
        value[2] = value[2] + 4
    if label[21] == '1':
        value[2] = value[2] + 8
    res += value[2] * 100

    if label[22] == '1':
        value[1] = value[1] + 1
    if label[23] == '1':
        value[1] = value[1] + 2
    if label[24] == '1':
        value[1] = value[1] + 4
    if label[25] == '1':
        value[1] = value[1] + 8
    res += value[1] * 1000

    if label[26] == '1':
        value[0] = value[0] + 1
    if label[27] == '1':
        value[0] = value[0] + 2
    if label[28] == '1':
        value[0] = value[0] + 4
    res += value[0] * 10000

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
            if inf[cont][0:8] == ['0', '0', '0', '1', '0', '1', '0', '1']:
                angle = simbologia(data)
            screen.blit(background_image, background_position)
            screen.blit(rotaciona_alt(seta10000, (angle * (-1) / 285)), background_position)
            screen.blit(rotaciona_alt(seta1000, (angle * (-1) / 28)), background_position)
            screen.blit(rotaciona_alt(seta100, (angle * (-1) / 2.75) + 375), background_position)
            cont += 1
            pygame.display.flip()
            clock.tick(1000)

            if cont == 40000:
                done = True
    pygame.quit()


if __name__ == '__main__':
    pygame.init()

    # 400x400 sized screen
    screen = pygame.display.set_mode([600, 600])

    # This sets the name of the window
    pygame.display.set_caption('Altimetro')

    clock = pygame.time.Clock()
    background_position = [0, 0]

    # Load and set up graphics.
    background_image = pygame.image.load("background_altimeter.png")  # .convert()
    seta10000 = pygame.image.load("seta3.png")
    seta1000 = pygame.image.load("seta1.png")
    seta100 = pygame.image.load("seta2.png")
    client_program()


