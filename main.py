import pygame
import random
import time

pygame.init()


#intialize screen and set it up

screen = pygame.display.set_mode([1000,1000])
pygame.display.set_caption("Rock, Scissors and Circle")
def suspense():
  pygame.sleep(10)

#variables and constansts here

BGCOLOR = "LavenderBlush3"
player_1 = ""
computer = ""
player_2 = ""
computer_number = random.randint(1,3)

#load assests here
rock_image = pygame.image.load("assets/rocks.png")
rock_image = pygame.transform.scale(rock_image, (200,200))

scissor_image = pygame.image.load("assets/scissors.png")
scissor_image = pygame.transform.scale(scissor_image, (200,200))

paper_image = pygame.image.load("assets/paper.png")
paper_image = pygame.transform.scale(paper_image, (200,200))
#set up objects

def rock(x,y):
    pass

def scissor(x,y):
    pass

def paper(x,y):
    pass

def player_choice(text):
    set_my_font = pygame.font.SysFont("comic sans", 60)
    textSurface = set_my_font.render(text, True, "black")
    screen.blit(textSurface, (300, 500))
def player2_choice(text):
    set_my_font = pygame.font.SysFont("comic sans", 60)
    textSurface = set_my_font.render(text, True, "black")
    screen.blit(textSurface, (100, 100))
  
running = True
while running:
    #get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player_2 = "Rock"
            elif event.key == pygame.K_p:
                player_2 = "Paper"
            elif event.key == pygame.K_s:
                player_2 = "Scissors"
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = event.pos
            if rocky.collidepoint(m_x, m_y):
              player_1 = "rock"
            if papery.collidepoint(m_x, m_y):
              player_1 = "paper"
            if scissorz.collidepoint(m_x, m_y):
              player_1 = "scissors"
    

  
              
    #process input
    
    #update state
    screen.fill(BGCOLOR)
    #pygame.draw.circle(screen, "grey2", (100, 250), 50)
 
    scissorz = screen.blit(scissor_image, (300, 200))  
    papery = screen.blit(paper_image, (500, 200))
    rocky = screen.blit(rock_image, (100, 200))
    
    if player_1 != "":
      time.sleep(10)
      player_choice(f"You have chosen {player_1}")
    if player_2 != "" :
      player2_choice(f"Opponent has chosen {player_2}")
    #draw screen
    pygame.display.flip()
 

pygame.quit()
