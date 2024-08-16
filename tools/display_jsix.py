import sys
import os
import pygame
from jsix.main import JSIXImageFormat

def suppress_pygame_warnings():
    sys.stdout = open(os.devnull, 'w')
    pygame.init()
    sys.stdout = sys.__stdout__

def display_jsix_image(jsix_filename, max_size=(800, 800)):
    jsix_image = JSIXImageFormat.load(jsix_filename)

    scale_width, scale_height = jsix_image.width, jsix_image.height
    if jsix_image.width > max_size[0]:
        scale_width = max_size[0]
        scale_height = int((max_size[0] / jsix_image.width) * jsix_image.height)
    if scale_height > max_size[1]:
        scale_height = max_size[1]
        scale_width = int((max_size[1] / jsix_image.height) * jsix_image.width)

    suppress_pygame_warnings()

    screen = pygame.display.set_mode((scale_width, scale_height))
    pygame.display.set_caption(f"Showing image: {os.path.basename(jsix_filename)}")

    surface = pygame.Surface((jsix_image.width, jsix_image.height))
    for y in range(jsix_image.height):
        for x in range(jsix_image.width):
            surface.set_at((x, y), jsix_image.pixels[y * jsix_image.width + x])

    scaled_surface = pygame.transform.scale(surface, (scale_width, scale_height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python display_jsix.py <input.jsix>")
        sys.exit(1)

    jsix_filename = sys.argv[1]
    display_jsix_image(jsix_filename)
