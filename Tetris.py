from random import *
import pygame
import copy

# TEST

SIZE = 20
GAP = 1
GRIDX = 20
GRIDY = 20
SPEED = 1000
PLAYING = False


class Block:

    def __init__(self, pos, col):
        self.pos = pos
        self.currRotPos = 0
        self.color = col


    def getPosition(self):
        return self.pos[self.currRotPos]

    def getColor(self):
        return self.color

    def changeRotation(self):
        if self.currRotPos == 3:
            self.currRotPos = 0
        else:
            self.currRotPos += 1

    def gravity(self):
        for i in range(len(self.pos)):
            for j in range(len(self.pos)):
                self.pos[i][j][1] = self.pos[i][j][1] + 1

    def move(self, dir):
        for i in range(len(self.pos)):
            for j in range(len(self.pos)):
                self.pos[i][j][0] = self.pos[i][j][0] + dir






xDim = ((SIZE + GAP) * GRIDX + 2 * GAP + SIZE)
yDim = ((SIZE + GAP) * GRIDY + 2 * GAP + SIZE)

CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((xDim, yDim))

#block1 = Block([[0, 0], [1, 0], [2, 0], [2, 1]],
#               [[1, 0], [1, 1], [1, 2], [0, 2]],
#               [[0, 0], [0, 1], [1, 1], [2, 1]],
#               [[0, 0], [1, 0], [0, 1], [0, 2]])

BLOCKS = [
    [
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[1, 0], [1, 1], [1, 2], [0, 2]],
        [[0, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 0], [1, 0], [0, 1], [0, 2]]
    ],
    [
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[1, 0], [1, 1], [1, 2], [0, 2]],
        [[0, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 0], [1, 0], [0, 1], [0, 2]]
    ]
]





def goBlocks(currBlock, col):
    for i in currBlock:
        # drawSquare(i[0],i[1],(255,255,255))
        drawSquare(i[0], i[1], col)

def printTheFin(finishedArr):
    for i in finishedArr:
        for j in range(len(i) - 1):

            drawSquare(i[j][0], i[j][1], i[len(i) - 1])



# Function to draw individual squares of the entire block
def drawSquare(x, y, cols):
    dims = [GAP + (SIZE + GAP) * x, GAP + (SIZE + GAP) * y, SIZE, SIZE]
    pygame.draw.rect(screen, cols, dims, 0)


# Function to move the block down like gravity
def gravity(currentBlock):
    for i in range(len(currentBlock)):
        for j in range(len(currentBlock)):
            currentBlock[i][j][1] = currentBlock[i][j][1] + 1


# Function to move left to right
def move(dir, currentBlock):
    for i in range(len(currentBlock)):
        for j in range(len(currentBlock)):
            currentBlock[i][j][0] = currentBlock[i][j][0] + dir


def rotate(rotation):

    if rotation == 3:
        rotation = 0
    else:
        rotation += 1

    return rotation

def check(currentBlock, finishedArray, col):
    for i in currentBlock:
        if i[1] == GRIDY:
            currentBlock.append(col)
            finishedArray.append(currentBlock)
            return True
        for j in finishedArray:
            for k in j:
                if i[1] == (k[1] - 1) and i[0] == k[0]:
                    currentBlock.append(col)
                    finishedArray.append(currentBlock)
                    return True

def checkBounds(currentBlock, finishedArray, dir):

    direct = [0, GRIDX]

    check = direct[(int) ((dir + 2) / 2)]

    for i in currentBlock:
        if i[0] == check:
            return False

        if dir == -1:
            for j in finishedArray:
                for k in j:
                    if (i[0] -1) == k[0] and (i[1] == k[1]):
                        return False

        if dir == 1:
            for j in finishedArray:
                for k in j:
                    if i[0]+1 == k[0] and i[1] == k[1]:
                        return False

    return True





currentBlock = Block(copy.deepcopy(BLOCKS[0]), (randint(0,255),randint(0,255),randint(0,255)))


def run():
    # set playing equal to true
    PLAYING = True

    finishedArray = []

    speedCt = 0
    screen.fill((0, 0, 0))

    global currentBlock
    while PLAYING:
        speedCt += 1
        screen.fill((0, 0, 0))
        goBlocks(currentBlock.getPosition(), currentBlock.getColor())
        if speedCt == SPEED / 2:
            currentBlock.gravity()
            if (check(currentBlock.getPosition(), finishedArray, currentBlock.getColor())):
                currentBlock = Block(copy.deepcopy(BLOCKS[0]), (randint(0,255),randint(0,255),randint(0,255)))
            speedCt = 0
        if len(finishedArray) != 0:
            printTheFin(finishedArray)
        pygame.display.update()
        CLOCK.tick(SPEED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if(checkBounds(currentBlock.getPosition(), finishedArray, 1)):
                        currentBlock.move(1)
                if event.key == pygame.K_LEFT:
                    if(checkBounds(currentBlock.getPosition(), finishedArray, -1)):
                        currentBlock.move(-1)
                if event.key == pygame.K_UP:
                    if(not check(currentBlock.getPosition(),finishedArray, currentBlock.getColor())):
                        currentBlock.changeRotation()


def initialFunc():
    pygame.init()
    pygame.display.set_caption("TETRIS")


initialFunc()
run()
