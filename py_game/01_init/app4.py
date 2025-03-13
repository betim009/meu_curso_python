import pygame

# Inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Carregar imagens do personagem
player_still = pygame.image.load("idle.png")  # Imagem quando está parado
player_walk = pygame.image.load("run.png")  # Imagem quando está andando

# Redimensionar se necessário
player_still = pygame.transform.scale(player_still, (140, 140))
player_walk = pygame.transform.scale(player_walk, (140, 140))

# Posição e velocidade
player_x = 100
player_y = 500
player_speed = 5

# Começa com a imagem parada
current_image = player_still

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:  # Move para a direita
        player_x += player_speed
        current_image = player_walk  # Troca para a imagem andando
    else:
        current_image = player_still  # Volta para a imagem parada

    # Preencher o fundo
    screen.fill("purple")

    # Desenhar o personagem na tela
    screen.blit(current_image, (player_x, player_y))

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
