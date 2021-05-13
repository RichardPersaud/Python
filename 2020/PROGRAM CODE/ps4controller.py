
import os
import pygame

pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()

axis_data = {}

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            axis_data[event.axis] = round(event.value, 2)

        os.system('cls')
        # print.pprint(axis_data)
        print("Left Stick:")
        print(f'X: {axis_data.get(0)}\nY: {axis_data.get(1)}')
        print("\nRight Stick:")
        print(f'X: {axis_data.get(2)}\nY: {axis_data.get(3)}')
