import pygame

# Inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Carregar a imagem do personagem
player_image = pygame.image.load("idle.png")  # Substitua pelo caminho da sua imagem
player_x = 300  # Posição inicial X
player_y = 500  # Posição inicial Y
player_speed = 5  # Velocidade do personagem
player_image = pygame.transform.scale(player_image, (120, 120))  # Define um novo tamanho (largura, altura)


while running:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:  # Move para a direita
        player_x += player_speed

    # Preencher o fundo
    screen.fill("black")

    # Desenhar o personagem na tela
    screen.blit(player_image, (player_x, player_y))

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
