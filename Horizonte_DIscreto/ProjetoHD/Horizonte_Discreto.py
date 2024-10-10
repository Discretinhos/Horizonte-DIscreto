import pygame
import sys

pygame.init()

pygame.mixer_music.load("recursos/musica_meu.mp3")
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.4)
passos = pygame.mixer.Sound("recursos/som_passos.wav")


largura = 1365
altura = 510


background_primavera_desfocado = pygame.image.load("backgrounds/cenario1(primavera-desfocado).jpg")
background_primavera_desfocado = pygame.transform.scale(background_primavera_desfocado, (largura, altura))
background_primavera_meio_foco = pygame.image.load("backgrounds/cenario1(primavera-meio_foco).jpg")
background_primavera_meio_foco = pygame.transform.scale(background_primavera_meio_foco, (largura, altura))
background_primavera_nitido = pygame.image.load("backgrounds/cenario1(primavera-nitido).jpg")
background_primavera_nitido = pygame.transform.scale(background_primavera_nitido, (largura, altura))
background_inicio = pygame.image.load("recursos/tela_inicial.jpg")
background_inicio = pygame.transform.scale(background_inicio, (largura, altura))


mapa = pygame.image.load("recursos/mapa.jpg")  # tela: 1280 x 700
mapa = pygame.transform.scale(mapa, (largura,altura))
personagem_sprite_sheet = pygame.image.load('recursos/sprites_Ella_prota.png')
personagem_sprite_sheet = pygame.transform.scale(personagem_sprite_sheet, (32 * 6, 32 * 8))

icon = pygame.image.load("recursos/icon.jpg")
bau = pygame.image.load("recursos/baú fechado.png")
barra_xp = pygame.image.load("barras_xp/barra_xp_comeco.png")
barra_xp_20 = pygame.image.load("barras_xp/barra_xp_20%.png")
barra_xp = pygame.transform.scale(barra_xp, (200, 50))
barra_xp_20 = pygame.transform.scale(barra_xp_20, (200, 50))


# Posição inicial do personagem
personagem_x = 500
personagem_y = 418
personagem_largura = 64
personagem_altura = 64

# Velocidade do personagem
velocidade = 5

# Controlar a direção do personagem
direcao = 'direita'

# Posição do baú
bau_x = 1280
bau_y = 432
bau_largura = 32
bau_altura = 32

barra_xp_x = 25
barra_xp_y = 10
barra_xp_largura = 32
barra_xp_altura = 32

# Título e ícone da janela
pygame.display.set_caption("Horizonte Discreto")
pygame.display.set_icon(icon)

# Perguntas
pergunta_1 = pygame.image.load("recursos/pergunta_1_primavera.jpg")
pergunta_1 = pygame.transform.scale(pergunta_1, (1365,510))
pergunta_2 = pygame.image.load("recursos/pergunta_2_primavera.jpg")
pergunta_2 = pygame.transform.scale(pergunta_2, (1365,510))
pergunta_3 = pygame.image.load("recursos/pergunta_3_primavera.jpg")
pergunta_3 = pygame.transform.scale(pergunta_3, (1365,510))
pergunta_4 = pygame.image.load("recursos/pergunta_4_primavera.jpg")
pergunta_4 = pygame.transform.scale(pergunta_4, (1365,510))
pergunta_5 = pygame.image.load("recursos/pergunta_5_primavera.jpg")
pergunta_5 = pygame.transform.scale(pergunta_5, (1365,510))
perguntas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5]
pergunta_atual = 0
respondendo = True

# Baú e Ticket
bau_transformado = False
ticket_primavera = pygame.image.load("recursos/ticket_primavera.png")
ticket_primavera = pygame.transform.scale(ticket_primavera, (44, 44))

def transicao_background(tela):
    """Função para realizar a transição de foco das imagens."""
    clock = pygame.time.Clock()

    # Duração de cada transição em milissegundos
    duracao_transicao = 1000  # 1 segundo

    # Imagem desfocada
    tela.blit(background_primavera_desfocado, (0, 0))
    pygame.display.update()
    pygame.time.delay(duracao_transicao)

    # Imagem com foco médio
    tela.blit(background_primavera_meio_foco, (0, 0))
    pygame.display.update()
    pygame.time.delay(duracao_transicao)

    # Imagem nítida
    tela.blit(background_primavera_nitido, (0, 0))
    pygame.display.update()
    pygame.time.delay(duracao_transicao)


def tela_inicio():
    """Tela inicial onde ocorre a transição de imagens."""
    largura_inicio, altura_inicio = background_inicio.get_size()
    tela = pygame.display.set_mode((largura_inicio, altura_inicio))

    # Loop da tela inicial
    while True:
        tela.blit(background_inicio, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    transicao_background(tela)  # Iniciar a transição antes do jogo
                    jogo()


def mostrar_mapa(tela):
    """Função para mostrar o mapa na tela."""
    clock = pygame.time.Clock()
    while True:
        tela.blit(mapa, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Voltar ao jogo ao pressionar ESC
                    return

        clock.tick(60)


def mostrar_tuto_inicial(tela, largura):
    """Função para exibir o tutorial inicial na tela."""
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 32)
    cor_texto = (0, 0, 0)  # Texto cor preta

    tuto_inicial = [
        "Seja bem-vinda à sua nova aventura, andarilha Ella!",
        "Agora que decidistes adentrar por entre as misteriosas e",
        "desconhecidas incertezas desta floresta tão diversa e imaculada,",
        "recomendo que seja discreta como a matemática que logo a frente",
        "te espera com enigmas lógicos que decidirão se estás apta,",
        "de fato, a seguir o árduo e desafiador caminho pela frente.",
        "Ao fim de cada um dos quatro enigmas sazonais, um ticket te espera",
        "para simbolizar o valor e a aptidão demonstrados por sua brava figura,",
        "em busca de desbravar o pico da serra e as mitológicas figuras",
        "de dois grandes desbravadores que fundaram estas antes abandonadas terras."
    ]

    while True:
        fundo_tutorial = pygame.image.load("recursos/fundo_tutorial_inicial.jpg")
        fundo_tutorial = pygame.transform.scale(fundo_tutorial, (largura, altura))
        tela.blit(fundo_tutorial, (0, 0))

        # Renderiza cada linha do texto do tutorial
        y_offset = 100
        for linha in tuto_inicial:
            text_surface = fonte.render(linha, True, cor_texto)
            text_rect = text_surface.get_rect(center=(largura / 2, y_offset))
            tela.blit(text_surface, text_rect)
            y_offset += 40  # Espaçando entre as linhas

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Voltar ao jogo ao pressionar ESC
                    return
        clock.tick(60)


def quiz_primavera(tela):
    global pergunta_atual, respondendo

    # Gabarito das perguntas
    gabarito = [pygame.K_b, pygame.K_d, pygame.K_a, pygame.K_c, pygame.K_b]

    # Loop para responder todas as perguntas
    while respondendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if pergunta_atual < len(perguntas):
                    # Verifica se a tecla digitada corresponde ao gabarito da pergunta atual
                    if evento.key == gabarito[pergunta_atual]:
                        pergunta_atual += 1  # Avança para a próxima pergunta
                        if pergunta_atual >= len(perguntas):
                            respondendo = False  # Finaliza o quiz após a última pergunta
                            receber_ticket()  # Chama a função para transformar o baú em ticket
                    else:
                        print("Resposta incorreta! Tente novamente.")

        # Mostrar a pergunta atual na tela, se houver perguntas restantes
        if pergunta_atual < len(perguntas):
            tela.blit(perguntas[pergunta_atual], (0, 0))
        else:
            receber_ticket()
        pygame.display.update()

def receber_ticket():
    """Função para trocar a imagem do baú pelo ticket após o quiz ser finalizado."""
    global bau, bau_transformado
    bau = ticket_primavera  # Troca a imagem do baú pela imagem do ticket
    bau_y = personagem_y
    bau_transformado = True  # Indica que o baú foi transformado em ticket


def jogo():
    """Função principal do jogo após a transição."""
    global personagem_x, personagem_y, direcao, barra_xp_20, barra_xp

    largura_primavera, altura_primavera = background_primavera_nitido.get_size()
    tela = pygame.display.set_mode((largura_primavera, altura_primavera))

    clock = pygame.time.Clock()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Verific as teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            if personagem_y > 418:  # Limite superior
                personagem_y -= velocidade
                pygame.mixer.Sound.play(passos, 1, 2)
                direcao = 'cima'
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            if personagem_y < 418:  # Limite inferior
                personagem_y += velocidade
                pygame.mixer.Sound.play(passos, 1, 2)
                direcao = 'baixo'
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            if personagem_x > 0:  # Limite esquerdo
                personagem_x -= velocidade
                pygame.mixer.Sound.play(passos, 1, 2)
                direcao = 'esquerda'
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            if personagem_x < largura_primavera - personagem_largura:  # Limite direito
                personagem_x += velocidade
                pygame.mixer.Sound.play(passos, 1, 2)
                direcao = 'direita'
        if teclas[pygame.K_m]:  # Pressione 'M' para mostrar o mapa
            mostrar_mapa(tela)
        if teclas[pygame.K_h]:  # Pressione 'H' para mostrar o tutorial inicial
            mostrar_tuto_inicial(tela, largura)

        # Background geral do jogo
        tela.blit(background_primavera_nitido, (0, 0))

        # Perspectiva da personagem com base na direção
        if direcao == 'cima':
            tela.blit(personagem_sprite_sheet, (personagem_x, personagem_y),
                      (0, 0, 64, 64))
        elif direcao == 'baixo':
            tela.blit(personagem_sprite_sheet, (personagem_x, personagem_y),
                      (0, 64, 64, 64))
        elif direcao == 'esquerda':
            personagem_invertido = pygame.transform.flip(personagem_sprite_sheet, True, False)
            tela.blit(personagem_invertido, (personagem_x, personagem_y), (0, 64 * 2, 64, 64))
        elif direcao == 'direita':
            tela.blit(personagem_sprite_sheet, (personagem_x, personagem_y), (64 * 2, 64 * 2, 64, 64))

        # Detectar colisão
        retangulo_personagem = pygame.Rect(personagem_x, personagem_y, personagem_largura, personagem_altura)
        retangulo_bau = pygame.Rect(bau_x, bau_y, bau_largura, bau_altura)

        # Verificar a colisão entre a personagem e o baú
        if retangulo_personagem.colliderect(retangulo_bau):
            quiz_primavera(tela)
            barra_xp = barra_xp_20

            # Inverter a direção da personagem ao colidir
            if direcao == 'direita':
                direcao = 'esquerda'
                personagem_x -= velocidade  # Mover a personagem para longe do baú
            elif direcao == 'esquerda':
                direcao = 'direita'
                personagem_x += velocidade
            elif direcao == 'cima':
                direcao = 'baixo'
                personagem_y += velocidade
            elif direcao == 'baixo':
                direcao = 'cima'
                personagem_y -= velocidade

        # Desenhe o baú
        tela.blit(bau, (bau_x, bau_y))
        tela.blit(barra_xp, (barra_xp_x, barra_xp_y))

        # Atualize a tela
        pygame.display.update()
        clock.tick(60)


# Inicie o jogo
tela_inicio()