import pygame

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

PRINT_MOUSE = True
USE_MOTION = True

mouse_pos = [(1, 1), (2, 2)]
# mouse meter
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def mdir(mouse_pos):
    global matrix

    if (pygame.mouse.get_pressed(num_buttons=3)[0]):
        if (mouse_pos[0][0] > mouse_pos[1][0]):  # x right
            matrix[1][0] += 1
        if (mouse_pos[0][1] > mouse_pos[1][1]):  # y down
            matrix[0][1] += 1
        if (mouse_pos[0][0] < mouse_pos[1][0]):  # x left
            matrix[1][2] += 1
        if (mouse_pos[0][1] < mouse_pos[1][1]):  # y up
            matrix[2][1] += 1
        # corners
        if (matrix[1][2] > 0 and matrix[2][1] > 0):  # right down
            matrix[2][2] += 1
        if (matrix[1][2] > 0 and matrix[0][1] > 0):  # right up
            matrix[0][2] += 1
        if (matrix[1][0] > 0 and matrix[2][1] > 0):  # left down
            matrix[2][0] += 1
        if (matrix[1][0] > 0 and matrix[0][1] > 0):  # left up
            matrix[0][0] += 1
        if (PRINT_MOUSE):
            print(matrix[0])
            print(matrix[1])
            print(matrix[2])
            print("")
        reset_mouse()


def reset_mouse():
    # reset mouse meter
    global matrix
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


while True:

    pos = pygame.mouse.get_pos()
    if (len(mouse_pos) >= 3):
        mouse_pos.pop(0)
    else:
        mouse_pos.append(pos)
    if not USE_MOTION:
        mdir(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if (USE_MOTION):
            if event.type == pygame.MOUSEMOTION:
                mdir(mouse_pos)
    clock.tick(60)