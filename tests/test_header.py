import pytest
from jsix.header import write_header, read_header
from io import StringIO

def test_write_and_read_header():
    magic_number = "JSIXIMAGEFORMAT"
    width = 2
    height = 2
    pixel_depth = 3

    file_sim = StringIO()

    write_header(file_sim, magic_number, width, height, pixel_depth)

    file_sim.seek(0)

    read_magic_number, read_width, read_height, read_pixel_depth = read_header(file_sim)

    assert read_magic_number == magic_number
    assert read_width == width
    assert read_height == height
    assert read_pixel_depth == pixel_depth
