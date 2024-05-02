import os
import datetime
import time

# Variables globales: Colores en formato ANSI escape code
reset_color = "\033[0m"
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
blue_color = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"
white_color = "\033[97m"

# funciones de usuario


def gotoxy(x, y):
    print("%c[%d;%df" % (0x1B, y, x), end="")


def borrarPantalla():
    os.system("cls")


def mensaje(widht, height, msg, color=yellow_color):
    color = color
    width = widht + 4

    title_x = (width - len(msg)) // 2

    gotoxy(title_x, height)
    print(color + msg + reset_color)


def marco_lateral(content_width, content_height):
    frame_width = content_width + 4  
    frame_height = content_height + 4

    # Dibujar los bordes laterales y el contenido interno
    for i in range(2, frame_height - 1):
            gotoxy(2, i + 2)
            print(green_color + "*" + reset_color + " " *
                content_width + green_color + "*" + reset_color)
    
    
def marco_inferior(content_width, content_height):
    frame_width = content_width + 2  
    frame_height = content_height + 4
    gotoxy(2, frame_height);print(green_color + "*" * frame_width + reset_color)


def confirmacion(widht, height, msg):
    width = widht + 4

    title_x = (width - len(msg)) // 2

    gotoxy(title_x, height)
    print(f'{red_color}{msg}{reset_color}', end=' ')
    procesar = input().lower()
    gotoxy(title_x + len(msg) + 2, height)
    print(green_color+" ✔"+reset_color)
    return procesar


