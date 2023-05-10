import math
import pygame

# Inicializar pygame
pygame.init()

# Variables de entrada
h0 = float(input("Ingrese altura inicial (en metros): "))
v0 = float(input("Ingrese velocidad inicial (en metros por segundo): "))
theta = float(input("Ingrese ángulo de lanzamiento (en grados): "))

# Convertir ángulo de grados a radianes
theta = math.radians(theta)

# Constantes
g = 9.81

# Variables de salida
t_max = v0 * math.sin(theta) / g
x_max = v0 * math.cos(theta) * t_max

# Configurar ventana
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lanzamiento parabólico")

# Crear suelo
ground_color = (128, 64, 0)
ground_width = width
ground_height = 50
ground = pygame.Surface((ground_width, ground_height))
ground.fill(ground_color)

# Crear pelota
ball_color = (255, 0, 0)
ball_radius = 10
ball = pygame.Surface((ball_radius * 2, ball_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(ball, ball_color, (ball_radius, ball_radius), ball_radius)

# Tiempo inicial
t = 0
dt = 0.01

# Bucle principal
clock = pygame.time.Clock()
while True:
    clock.tick(60) # Limitar a 60 fotogramas por segundo
    
    # Manejar eventos de teclado y ratón
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Calcular posición de la pelota en función del tiempo
    x = v0 * math.cos(theta) * t
    y = h0 + v0 * math.sin(theta) * t - 0.5 * g * t * t
    
    # Actualizar posición de la pelota
    ball_x = int(x)
    ball_y = int(height - y)
    window.blit(ball, (ball_x - ball_radius, ball_y - ball_radius))
    
    # Dibujar objetos en la ventana
    window.blit(ground, (0, height - ground_height))
    pygame.display.update()
    
    # Actualizar tiempo
    t += dt
    
    # Si la pelota ha llegado al suelo, salir del bucle
    if y <= 0:
        break

# Calcular altura máxima alcanzada
y_max = h0 + (v0 * v0 * math.sin(theta) * math.sin(theta)) / (2 * g)

# Mostrar resultados
print("Altura máxima alcanzada: {:.2f} metros".format(y_max))
print("Tiempo en que se alcanza la altura máxima: {:.2f} segundos".format(t_max))
print("Alcance máximo: {:.2f} metros".format(x_max))

# Salir de pygame
pygame.quit()
