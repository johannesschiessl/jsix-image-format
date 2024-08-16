import pytest
from jsix.pixel_data import write_pixels, read_pixels
from io import StringIO

def test_write_and_read_pixels():
    pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    width = 2
    height = 2
    pixel_depth = 3

    file_sim = StringIO()

    write_pixels(file_sim, pixels)

    file_sim.seek(0)

    read_pixels_data = read_pixels(file_sim, width, height, pixel_depth)

    assert read_pixels_data == pixels
