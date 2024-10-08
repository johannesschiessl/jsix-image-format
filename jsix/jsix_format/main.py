from PIL import Image
from .header import write_header, read_header
from .pixel_data import write_pixels, read_pixels

class JSIXImageFormat:
    def __init__(self, width, height, pixels):
        self.magic_number = "JSIXIMAGEFORMAT"
        self.width = width
        self.height = height
        self.pixel_depth = 3
        self.pixels = pixels

    def save(self, filename):
        with open(filename, 'w') as f:
            write_header(f, self.magic_number, self.width, self.height, self.pixel_depth)
            write_pixels(f, self.pixels)

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            magic_number, width, height, pixel_depth = read_header(f)
            pixels = read_pixels(f, width, height, pixel_depth)
        return JSIXImageFormat(width, height, pixels)

    @staticmethod
    def from_png(png_filename):
        image = Image.open(png_filename)
        image = image.convert("RGB")
        width, height = image.size
        pixels = list(image.getdata())
        return JSIXImageFormat(width, height, pixels)

    @staticmethod
    def png_to_jsix(png_filename, jsix_filename):

        jsix_image = JSIXImageFormat.from_png(png_filename)

        jsix_image.save(jsix_filename)
