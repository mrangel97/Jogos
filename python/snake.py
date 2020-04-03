import pygame
from random import randrange

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

try:
    pygame.init() # inicialize o módulo de exibição
except:
    print("O modulo pygame não foi inicializado com sucesso")

largura = 640 
altura = 480
tamanho = 10
placar = 40

relogio = pygame.time.Clock()

fundo = pygame.display.set_mode((largura,altura)) # inicialize uma janela ou tela para exibição
pygame.display.set_caption("Snake") # defina a legenda da janela atual

def text(msg, color, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    text1 = font.render(msg, True, color)
    fundo.blit(text1, [x, y])

def snake(SnakeXY):
    for XY in SnakeXY:
        pygame.draw.rect(fundo,green,[XY[0], XY[1], tamanho, tamanho])

def apple(pos_x, pos_y):
    pygame.draw.rect(fundo,red,[pos_x, pos_y, tamanho, tamanho])

def game():
    dentro = True
    end_game = False
    pos_x =  randrange(0, largura - tamanho , 10)
    pos_y =  randrange(0, altura - tamanho - placar , 10)
    apple_x =  randrange(0, largura - tamanho , 10)
    apple_y =  randrange(0, altura - tamanho - placar , 10)
    velocidade_x = 0
    velocidade_y = 0
    SnakeXY = []
    SnakeComp = 1
    pontos = 0
    while dentro:
        while end_game:
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 dentro = False
                 end_game = False
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_c:
                      dentro = True
                      end_game = False
                      pos_x =  randrange(0, largura - tamanho , 10)
                      pos_y =  randrange(0, altura - tamanho - placar , 10)
                      apple_x =  randrange(0, largura - tamanho , 10)
                      apple_y =  randrange(0, altura - tamanho - placar, 10)
                      velocidade_x = 0
                      velocidade_y = 0
                      SnakeXY = []
                      SnakeComp = 1
                      pontos = 0
                  if event.key == pygame.K_s:
                      dentro = False
                      end_game = False
              
            fundo.fill(black)
            text("Fim de jogo!", red, 50, 65, 30)
            text("Pontuação Final: "+str(pontos), blue, 30, 70, 80)
            pygame.draw.rect(fundo, white, [45, 120, 135, 27])
            text("Continuar(C)", red, 30, 50, 125)
            pygame.draw.rect(fundo, white, [190, 120, 75, 27])
            text("Sair(S)", red, 30, 195, 125)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dentro = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_y = -tamanho
                    velocidade_x = 0
                if event.key == pygame.K_DOWN and velocidade_y != tamanho:
                    velocidade_y = tamanho
                    velocidade_x = 0
                if event.key == pygame.K_SPACE:
                    SnakeComp += 1

        if dentro:
            fundo.fill(black)
            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x == apple_x and pos_y == apple_y:
                 apple_x = randrange(0, largura - tamanho , 10)
                 apple_y = randrange(0, altura - tamanho - placar , 10) 
                 SnakeComp += 1
                 pontos += 1

            if pos_x + tamanho > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x = largura - tamanho
            if pos_y + tamanho > altura - placar:
                pos_y = 0
            if pos_y < 0:
                pos_y = altura - tamanho - placar

            SnakeBegin = []
            SnakeBegin.append(pos_x)
            SnakeBegin.append(pos_y)
            SnakeXY.append(SnakeBegin)
            if len(SnakeXY) > SnakeComp:
                del SnakeXY[0]
            if any(bloco == SnakeBegin for bloco in SnakeXY[:-1]):
                end_game = True

            pygame.draw.rect(fundo,white,[0, altura - placar, largura, placar])
            text("Pontuação: " + str(pontos), blue, 30, 10, altura - 30)
            snake(SnakeXY)
            apple(apple_x, apple_y)
            pygame.display.update() #atualizar a janela atual
            relogio.tick(15)
       

game()
pygame.quit()
