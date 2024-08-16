def write_pixels(f, pixels):
    for pixel in pixels:
        hex_pixel = '{:02X}{:02X}{:02X}'.format(*pixel)
        f.write(hex_pixel + '\n')

def read_pixels(f, width, height, pixel_depth):
    pixels = []
    for _ in range(width * height):
        hex_pixel = f.readline().strip()
        r = int(hex_pixel[0:2], 16)
        g = int(hex_pixel[2:4], 16)
        b = int(hex_pixel[4:6], 16)
        pixels.append((r, g, b))
    return pixels
