import pygame

# Inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Carregar imagens do personagem
player_still = pygame.image.load("idle.png")  # Parado
player_walk = pygame.image.load("run.png")  # Andando para a direita

# Redimensionar se necessário
player_still = pygame.transform.scale(player_still, (140, 140))
player_walk = pygame.transform.scale(player_walk, (140, 140))

# Criar imagem espelhada para andar para a esquerda
player_walk_left = pygame.transform.flip(player_walk, True, False)

# Posição e velocidade
player_x = 100
player_y = 500
player_speed = 5

facing_right = True  # Direção inicial
current_image = player_still  # Começa com a imagem parada

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar teclas pressionadas
    keys = pygame.key.get_pressed()
    moving = False  # Variável para detectar se o personagem está se movendo

    if keys[pygame.K_RIGHT]:  # Direita
        player_x += player_speed
        current_image = player_walk
        facing_right = True
        moving = True

    elif keys[pygame.K_LEFT]:  # Esquerda
        player_x -= player_speed
        current_image = player_walk_left
        facing_right = False
        moving = True

    if keys[pygame.K_UP]:  # Para cima
        player_y -= player_speed
        moving = True

    elif keys[pygame.K_DOWN]:  # Para baixo
        player_y += player_speed
        moving = True

    # Se não estiver se movendo, volta para a imagem parada
    if not moving:
        current_image = player_still

    # Preencher o fundo
    screen.fill("purple")

    # Desenhar o personagem na tela
    screen.blit(current_image, (player_x, player_y))

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
