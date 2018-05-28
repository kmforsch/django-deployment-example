import random, time, pygame
pygame.init()

numberPool = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58,59,60,
          61,62,63,64,65,66,67,68,69,70,
          71,72,73,74,75,76,77,78,79,80,
          81,82,83,84,85,86,87,88,89,90,
          91,92,93,94,95,96,97,98,99,100]

pink  = (255, 51 , 102)
black = (0  , 0  , 0  )

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Python Bingo')
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 175)

def quitgame():
    pygame.quit()
    quit()

while True:
    clock.tick(5)
    gameDisplay.fill(pink)

    for i in range(99):
        currentNumber = random.choice(numberPool)
        text = font.render(str(currentNumber), True, black)
        gameDisplay.blit(text,(display_width/2,display_height/2))
        numberPool.remove(currentNumber)
        time.sleep(2)

   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
