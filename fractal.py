from numba import njit
import numpy as np
import pygame

# Fractals
MANDELBROT = "Mandelbrot"
JULIA = "Julia"
RATIONAL = "Rational"

# Gets color based on iteration
@njit
def get_color(iteration, max_iter):
    if iteration == max_iter:
        return 0, 0, 0  # Black if inside the set
    return 255 - int(iteration * 255 / max_iter), 255 - int(iteration * 255 / (max_iter / 2)), 255 - int(iteration * 255 / (max_iter / 3))

# Rational fractal
@njit
def rational_set(c, max_iter):
    iteration = 0
    z = c
    while abs(z) < 2 and iteration < max_iter:
        if z == 0: z = 1e-6
        z = z - (z**3 - 1) / (3 * z**2)
        iteration += 1
    return iteration

# Fractal generation using njit for speed
@njit
def generate_fractal(width, height, zoom, move_x, move_y, fractal_type, max_iter=256):
    fractal = np.zeros((height, width, 3), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + move_x
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + move_y
            if fractal_type == MANDELBROT:
                c = complex(zx, zy)
                z = complex(0, 0)
            elif fractal_type == JULIA:
                c = complex(-0.7, 0.27015)
                z = complex(zx, zy)
            elif fractal_type == RATIONAL:
                c = complex(zx, zy)
                iteration = rational_set(c, max_iter)
                fractal[y, x] = get_color(iteration, max_iter)
                continue

            iteration = 0
            while abs(z) < 2 and iteration < max_iter:
                z = z * z + c
                iteration += 1

            fractal[y, x] = get_color(iteration, max_iter)

    return np.rot90(fractal, k=3)

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Generator")
font = pygame.font.Font(None, 36)

# Buttons
button_color = (100, 200, 100)
buttons = {
    MANDELBROT: pygame.Rect(width - 400, height - 50, 150, 40),
    JULIA: pygame.Rect(width - 600, height - 50, 150, 40),
    RATIONAL: pygame.Rect(width - 800, height - 50, 150, 40),
    "Reset": pygame.Rect(width - 200, height - 50, 150, 40),
}

# Initialize dragging vars
dragging = False
start_pos = None

# Fractal defaults
zoom = 1.0
move_x = 0.0
move_y = 0.0
current_fractal = MANDELBROT
max_iter = 256

# Main loop deals with zooming and mouse interactions
running = True
fractal = generate_fractal(width, height, zoom, move_x, move_y, current_fractal, max_iter)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked_button = None
            for fractal_type, button in buttons.items():
                if button.collidepoint(event.pos):
                    clicked_button = fractal_type
                    break

            if clicked_button:
                if clicked_button == "Reset":
                    zoom = 1.0
                    move_x = 0.0
                    move_y = 0.0
                else:
                    current_fractal = clicked_button
                    zoom = 1.0
                    move_x = 0.0
                    move_y = 0.0
                fractal = generate_fractal(width, height, zoom, move_x, move_y, current_fractal, max_iter)
            else:
                dragging = True
                start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                dragging = False
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                rect.normalize()
                zoom_factor = min(width / rect.width, height / rect.height)
                zoom *= zoom_factor
                center_x = rect.left + rect.width / 2
                center_y = rect.top + rect.height / 2
                move_x += (center_x - width / 2) / (0.5 * width * zoom)
                move_y += (center_y - height / 2) / (0.5 * height * zoom)
                fractal = generate_fractal(width, height, zoom, move_x, move_y, current_fractal, max_iter)

    # Render fractal
    screen.fill((0, 0, 0))
    fractal_resized = pygame.transform.scale(pygame.surfarray.make_surface(fractal), (width, height))
    screen.blit(fractal_resized, (0, 0))

    # Draw buttons + labels
    for fractal_type, button in buttons.items():
        pygame.draw.rect(screen, button_color, button)
        label = "Reset Zoom" if fractal_type == "Reset" else fractal_type
        text = font.render(label, True, (0, 0, 0))
        screen.blit(text, (button.x + 20, button.y + 10))

    # Draw the zoom rectangle if dragging
    if dragging:
        end_pos = pygame.mouse.get_pos()
        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
        pygame.draw.rect(screen, (255, 255, 255), rect, 2)  # White rectangle for visibility

    pygame.display.flip()

pygame.quit()
