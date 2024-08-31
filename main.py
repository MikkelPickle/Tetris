# Tetris med Pygame!
# Dette er et tetris spil, hvor det går ud på at flyde vandrette linjer ud.
# For hver linje, som du får udfyldt får du 1 point. Dine totale point vil blive
# vist i shell-konsollen, når du har tabt.
# Man må helst ikke flytte blokken lige før den bliver sat fast, da dette kan
# lave en fejl i programmet.

# De forskellige inputs programmet forstår er:
# Pil-op = Roter block med uret.
# Pil-ned = Flyt block et felt ned.
# Pil-højre = Flyt block mod højre.
# Pil-venstre = Flyt block mod venstre.


# Imports
import pygame
import random
import time

# Initializering af pygame
pygame.init()
screen = pygame.display.set_mode((360, 660))
Quit = False
clock = pygame.time.Clock()

# Globale konstanter
x1, x2, x3, x4 = 1, 1, 2, 2
y1, y2, y3, y4 = 1, 2, 1, 2
k = 0
existing_object = 0
object_type = 5
rotation = 1
score = 0
quit_variable = 0
rotation_lock = 0


# Funktioner
def create_layers():
    '''Denne funktion laver den tomme spilleplade'''
    global layers
    layers = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


create_layers()


# Board is 360 x 660 (30x)
# Tetris is 12 x 22
def coordinates():
    '''Denne funktion kan lave elementerne i spilpladen om til koordinater'''
    global layers
    layer_elements = []
    for q in range(0, 10):
        for i in range(0, 21):
            if layers[i][q] == 1:
                k = [q, i]
                layer_elements.append(k)
    return layer_elements


def create_object():
    '''Denne funktion laver et tilfældigt objekt'''
    global existing_object, x1, x2, x3, x4, y1, y2, y3, y4, object_type, rotation
    if existing_object == 0:
        brick_nummer = random.randint(1, 7)
        existing_object = 1
        rotation = 1
        if brick_nummer == 1:  # S-brick
            x1, x2, x3, x4 = 1, 2, 2, 3
            y1, y2, y3, y4 = 2, 2, 1, 1
            object_type = 1
        elif brick_nummer == 2:  # Z-brick
            x1, x2, x3, x4 = 1, 2, 2, 3
            y1, y2, y3, y4 = 1, 1, 2, 2
            object_type = 2
        elif brick_nummer == 3:  # L-Brick
            x1, x2, x3, x4 = 3, 1, 2, 3
            y1, y2, y3, y4 = 1, 2, 2, 2
            object_type = 3
        elif brick_nummer == 4:  # J-Brick
            x1, x2, x3, x4 = 1, 1, 2, 3
            y1, y2, y3, y4 = 1, 2, 2, 2
            object_type = 4
        elif brick_nummer == 5:  # Firkant
            x1, x2, x3, x4 = 1, 2, 1, 2
            y1, y2, y3, y4 = 1, 1, 2, 2
            object_type = 5
        elif brick_nummer == 6:  # I-brick
            x1, x2, x3, x4 = 1, 2, 3, 4
            y1, y2, y3, y4 = 1, 1, 1, 1
            object_type = 6
        elif brick_nummer == 7:  # T-brick.
            x1, x2, x3, x4 = 2, 1, 2, 3
            y1, y2, y3, y4 = 1, 2, 2, 2
            object_type = 7


def rotate_obj():
    '''Denne funktion kan dreje en block'''
    global object_type, rotation, y1, y2, y3, y4, x1, x2, x3, x4
    if object_type == 1:  # S-brick
        if rotation == 1:
            y1 -= 2
            y2 -= 1
            x2 -= 1
            x4 -= 1
            y4 += 1
            rotation = 2
        elif rotation == 2:
            y1 += 1
            x2 += 1
            y3 -= 1
            y4 -= 2
            x4 += 1
            rotation = 1

    elif object_type == 2:  # Z-brick
        if rotation == 1:
            x1 += 1
            y1 -= 1
            x3 -= 1
            y3 -= 1
            x4 -= 2
            rotation = 2
        elif rotation == 2:
            x1 -= 1
            y2 -= 1
            x3 += 1
            x4 += 2
            y4 -= 1
            rotation = 1

    elif object_type == 3:  # L-brick
        if rotation == 1:
            y1 += 1
            x2 += 1
            y2 -= 2
            y3 -= 1
            x4 -= 1
            rotation = 2

        elif rotation == 2:
            x1 -= 1
            x2 += 2
            y2 += 1
            x3 += 1
            y4 -= 1
            rotation = 3

        elif rotation == 3:
            y1 -= 2
            x2 -= 1
            y2 += 1  # -
            x4 += 1
            y4 -= 1
            rotation = 4

        elif rotation == 4:
            x1 += 1
            x2 -= 2
            y2 -= 1
            x3 -= 1
            y4 += 1
            rotation = 1

    elif object_type == 4:  # J-brick
        if rotation == 1:
            x1 += 1
            y1 -= 1
            y2 -= 2
            x3 -= 1
            y3 -= 1
            x4 -= 2
            rotation = 2

        elif rotation == 2:
            x1 += 1
            y1 += 1
            x2 += 2
            x3 += 1
            y3 -= 1
            y4 -= 2
            rotation = 3

        elif rotation == 3:
            x1 -= 1
            y2 += 1
            x3 += 1
            x4 += 2
            y4 -= 1
            rotation = 4

        elif rotation == 4:
            x1 -= 1
            y1 -= 1
            x2 -= 2
            x3 -= 1
            y3 += 1
            y4 += 2
            rotation = 1

    elif object_type == 5:  # Firkant
        if rotation == 1:
            rotation = 1

    elif object_type == 6:  # I-brick
        if rotation == 1:
            x1 += 2
            y1 -= 3
            x2 += 1
            y2 -= 2
            y3 -= 1
            x4 -= 1
            rotation = 2

        elif rotation == 2:
            x1 -= 2
            y1 += 3
            x2 -= 1
            y2 += 2
            y3 += 1
            x4 += 1
            rotation = 1

    elif object_type == 7:  # T-brick
        if rotation == 1:
            x1 += 1
            y1 += 1
            x2 += 1
            y2 -= 1
            x4 -= 1
            y4 += 1
            rotation = 2

        elif rotation == 2:
            x1 -= 1
            y1 += 1
            x2 += 1
            y2 += 1
            x4 -= 1
            y4 -= 1
            rotation = 3

        elif rotation == 3:
            x1 -= 1
            y1 -= 1
            x2 -= 1
            y2 += 1
            x4 += 1
            y4 -= 1
            rotation = 4

        elif rotation == 4:
            x1 += 1
            y1 -= 1
            x2 -= 1
            y2 -= 1
            x4 += 1
            y4 += 1
            rotation = 1


def force_move_object(y1, y2, y3, y4):
    '''Denne funktion vil langsomt bevæge blokken nedad'''
    global k
    if k < 10:
        k += 1
    elif k > 9:
        k = 0
        y1 += 1
        y2 += 1
        y3 += 1
        y4 += 1
    return y1, y2, y3, y4


def freeze_block():
    '''Denne funktion fryser blokken, hvis den bevæger sig ned i en anden block'''
    global layers, x1, x2, x3, x4, y1, y2, y3, y4, existing_object
    freeze_layer = [[x1 - 1, y1], [x2 - 1, y2], [x3 - 1, y3], [x4 - 1, y4]]
    new_layer = coordinates()
    for x in freeze_layer:
        if (x in new_layer):
            layers[y1 - 1][x1 - 1] = 1
            layers[y2 - 1][x2 - 1] = 1
            layers[y3 - 1][x3 - 1] = 1
            layers[y4 - 1][x4 - 1] = 1
            existing_object = 0


def draw_rectangles():
    '''Denne funktion tegner hele outputtet til brugeren'''
    screen.fill((0, 0, 0))
    color = (0, 128, 255)

    element_x1 = 30 * int(x1)
    element_x2 = 30 * int(x2)
    element_x3 = 30 * int(x3)
    element_x4 = 30 * int(x4)

    element_y1 = 30 * int(y1)
    element_y2 = 30 * int(y2)
    element_y3 = 30 * int(y3)
    element_y4 = 30 * int(y4)

    pygame.draw.rect(screen, color, (element_x1, element_y1, 30, 30))
    pygame.draw.rect(screen, color, (element_x2, element_y2, 30, 30))
    pygame.draw.rect(screen, color, (element_x3, element_y3, 30, 30))
    pygame.draw.rect(screen, color, (element_x4, element_y4, 30, 30))

    # Siderne på displayed.
    board_colour = (128, 128, 128)
    pygame.draw.rect(screen, board_colour, (0, 0, 30, 660))
    pygame.draw.rect(screen, board_colour, (0, 0, 360, 30))
    pygame.draw.rect(screen, board_colour, (330, 0, 30, 660))
    pygame.draw.rect(screen, board_colour, (0, 630, 360, 30))

    # Forskellige lag på display
    lagd = coordinates()
    for b in range(len(lagd)):
        xgrey = 30 * int(lagd[b][0] + 1)
        ygrey = 30 * int(lagd[b][1] + 1)
        pygame.draw.rect(screen, board_colour, (xgrey, ygrey, 30, 30))
    pygame.display.update()
    clock.tick(20)


def remove_line():
    '''Denne funktion fjerner en linje, hvis den er helt udfyldt'''
    global score
    for x in range(len(layers) - 1):
        if layers[x] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
            score += 1
            for i in range(x):
                layers[x - i] = layers[x - i - 1]


def out_of_bounds():
    '''Denne funktion sørger for, at man ikke kan gå ud af banen sidelæns'''
    global x1, x2, x3, x4
    if x1 < 1 or x2 < 1 or x3 < 1 or x4 < 1:
        x1 += 1
        x2 += 1
        x3 += 1
        x4 += 1
    elif x1 > 10 or x2 > 10 or x3 > 10 or x4 > 10:
        x1 -= 1
        x2 -= 1
        x3 -= 1
        x4 -= 1


def check_if_lost():
    '''Denne funktion checker, om man har tabt'''
    global Quit, layers, quit_variable
    if 1 in layers[0] and 1 in layers[1]:
        if quit_variable == 1:
            Quit = True
        else:
            quit_variable = 1
    else:
        quit_variable = 0


# Main loop:
while Quit == False:
    for event in pygame.event.get():
        Quit = False
    freeze_block()
    y1_new, y2_new, y3_new, y4_new = force_move_object(y1, y2, y3, y4)
    y1, y2, y3, y4 = y1_new, y2_new, y3_new, y4_new
    # Frysning af blokke
    # Knap Input:
    freeze_block()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        y1 += 1
        y2 += 1
        y3 += 1
        y4 += 1
    if pressed[pygame.K_LEFT]:
        x1 -= 1
        x2 -= 1
        x3 -= 1
        x4 -= 1
    if pressed[pygame.K_RIGHT]:
        x1 += 1
        x2 += 1
        x3 += 1
        x4 += 1
    if pressed[pygame.K_UP]:
        if rotation_lock == 0:
            rotate_obj()
        rotation_lock = 1
    else:
        rotation_lock = 0

    # Funktionskald
    draw_rectangles()
    out_of_bounds()
    freeze_block()
    remove_line()
    check_if_lost()
    create_object()

# Her får man sin score at vide.
if Quit == True:
    tekst = 'Du har tabt! Du scorede ' + str(score) + ' points.'
    print(tekst)



