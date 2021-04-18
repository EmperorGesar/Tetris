import pygame
import board
import block


pygame.init()
screen = pygame.display.set_mode((320, 640))
pygame.display.set_caption("Tetris")

gameBoard = board.Board()
currentBlock = block.Block()


def drawBoard():

    grid = gameBoard.getGrid()

    for i in range(3, 23):
        for j in range(1, 11):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, [80, 90, 70], [32 * (j - 1), 32 * (i - 3), 32, 32], 0)


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                currentBlock.transform()
            elif event.key == pygame.K_LEFT:
                gameBoard.moveLeft(currentBlock)
            elif event.key == pygame.K_RIGHT:
                gameBoard.moveRight(currentBlock)
            elif event.key == pygame.K_DOWN:
                gameBoard.update(currentBlock)

    screen.fill([150, 170, 130])
    pygame.draw.rect(screen, [80, 90, 70], [0, 0, 320, 640], 2)

    if not gameBoard.hasCurrentBlock():
        gameBoard.clear()
        currentBlock.regenerate()

    gameBoard.update(currentBlock)
    drawBoard()

    pygame.display.flip()
    pygame.time.delay(500)
