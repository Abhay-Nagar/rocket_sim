import pygame
import math

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Rocket properties
mass = 10.0
gravity = 9.81
engine_thrust = 200.0
torque = 0
# State variables (using screen coordinates)
x = 500.0
y = 200.0
vy = 0.0
vx = 0
theta = 0.0        # Angular position (radians)
omega = 0.0        # Angular velocity (rad/s)
alpha = 0.0        # Angular acceleration (rad/s²)
mi = 10
rocket_width = 30
rocket_height = 70

# Scale: 10 pixels = 1 metre
scale = 10.0

running = True
# BEFORE the game loop
rocket_surface = pygame.Surface((30, 70), pygame.SRCALPHA)
rocket_surface.fill("white")

while running:
    dt = min(clock.tick(60) / 1000, 0.05)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read controls
    keys = pygame.key.get_pressed()

    thrust = engine_thrust if keys[pygame.K_SPACE] else 0

    if keys[pygame.K_LEFT]:
        torque=-10
        
    elif keys[pygame.K_RIGHT]:
        torque=10
        
    else:
        torque = 0

    alpha = torque/mi
    omega += alpha*dt
    theta += omega*dt

    # Calculate acceleration
    ay = gravity - thrust*math.cos(theta)/ mass
    ax = thrust*math.sin(theta)/mass
    # Numerically integrate motion
    vy += ay * dt
    y += vy * dt * scale
    vx += ax *dt
    x +=vx * dt
    # Draw everything
    screen.fill((20, 20, 30))

    rotated = pygame.transform.rotate(
    rocket_surface,
    -math.degrees(theta)
    )

    rocket_rect = rotated.get_rect(center=(x, y))
    screen.blit(rotated, rocket_rect)
    pygame.display.flip()

pygame.quit()