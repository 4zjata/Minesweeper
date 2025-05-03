import random
import pygame

#inicjalizacja
pygame.init()
grid = 20
celsiz = 25
LoseCheck = False
screen = pygame.display.set_mode((grid * celsiz, grid * celsiz))
pygame.display.set_caption('minesweeper')
screen.fill("darkgrey")
for x in range(grid + 1):
    pygame.draw.line(screen, "black", [0, x * celsiz], [screen.get_height(), x * celsiz], 5)
for x in range(grid + 1):
    pygame.draw.line(screen, "black", [x * celsiz, 0], [x * celsiz, screen.get_width()], 5)

#funkcje
def flood(row, column):
    if 0 <= row < grid and 0 <= column < grid and trackBoard[row][column] == 0:
        print(f'to 0...FLOOD!')
        trackBoard[row][column] = -2
        tekst(row,column,"red",17,"x")
        for x, y in pozycja:
            nowyX = row + x
            nowyY = column + y

            # If neighbor is within bounds and is a bomb, increment bomby
            if 0 <= nowyX < grid and 0 <= nowyY < grid and board[nowyX][nowyY] == 0:
                flood(nowyX,nowyY)
    else:
        return

def tekst(row,column,color,size,text):
    textXY = [0, 0]
    textXY[0] = column * 25 + 5
    textXY[1] = row * 25 + 5
    myFont = pygame.font.SysFont('Comic Sans MS', size)
    textSurface = myFont.render(text, False, color)
    screen.blit(textSurface, textXY)


# Create an empty board
board = [[0 for _ in range(grid)] for _ in range(grid)]
trackBoard = [[0 for _ in range(grid)] for _ in range(grid)]
# Set 20 bombs randomly on the board
bomb_count = 0
while bomb_count < 27:
    x = random.randint(0, grid - 1)
    y = random.randint(0, grid - 1)
    if board[x][y] != -1:  # Avoid placing a bomb in an already bombed cell
        board[x][y] = -1
        bomb_count += 1

# Define the directions to check the neighboring cells
pozycja = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Iterate through each cell to count bombs around non-bomb cells
for poz in range(grid):
    for pion in range(grid):
        if board[poz][pion] == -1:  # Skip bombs
            continue

        bomby = 0
        # Check all 8 neighboring cells
        for x, y in pozycja:
            nowyX = poz + x
            nowyY = pion + y

            # If neighbor is within bounds and is a bomb, increment bomby
            if 0 <= nowyX < grid and 0 <= nowyY < grid and board[nowyX][nowyY] == -1:
                bomby += 1

        # Only update the current cell if it's not a bomb
        board[poz][pion] = bomby

# Print the board to check the results
for row in board:
    print(row)

trackBoard == board
mb1 = (True,False,False)
mb2 = (False,False,True)
running = True
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed() == mb1 and LoseCheck == False:
            pos = pygame.mouse.get_pos()
            row = pos[1]//celsiz
            column = pos[0]//celsiz
            print(f'klik na komune {column},i rzad {row}')
            if board[row][column] == -1:
                screen.fill("grey")
                tekst( 5,0,"red",90,"Przegrales")
                LoseCheck = True
            elif board[row][column]>0:
                print(board[row][column])
                tekst(row,column,"black",17,str(board[row][column]))
            elif board[row][column] == 0:
                flood(row,column)
        if pygame.mouse.get_pressed() == mb2 and LoseCheck == False:
            pos = pygame.mouse.get_pos()
            row = pos[1] // celsiz
            column = pos[0] // celsiz
            tekst(row,column,"White",16,"F")
            print(f'klik na komune {column},i rzad {row}')
            trackBoard[row][column] = "F"






    # Flip the display to put your work on screen
    pygame.display.flip()

pygame.quit()
