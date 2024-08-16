import pytest
from jsix.main import JSIXImageFormat
from PIL import Image

def test_save_and_load_image():
    pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    image = JSIXImageFormat(2, 2, pixels)
    test_filename = 'test_image.jsix'

    image.save(test_filename)

    loaded_image = JSIXImageFormat.load(test_filename)

    assert loaded_image.width == 2
    assert loaded_image.height == 2
    assert loaded_image.pixel_depth == 3
    assert loaded_image.pixels == pixels

def test_from_png_to_jsix(tmp_path):
    png_filename = tmp_path / 'test_image.png'
    image = Image.new('RGB', (2, 2), color=(255, 255, 255))
    pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    image.putdata(pixels)
    image.save(png_filename)

    jsix_image = JSIXImageFormat.from_png(png_filename)

    assert jsix_image.width == 2
    assert jsix_image.height == 2
    assert jsix_image.pixel_depth == 3
    assert jsix_image.pixels == pixels

    jsix_filename = tmp_path / 'test_image.jsix'
    jsix_image.save(jsix_filename)

    loaded_jsix_image = JSIXImageFormat.load(jsix_filename)
    assert loaded_jsix_image.width == 2
    assert loaded_jsix_image.height == 2
    assert loaded_jsix_image.pixel_depth == 3
    assert loaded_jsix_image.pixels == pixels
