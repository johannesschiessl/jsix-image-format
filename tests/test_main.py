import pytest
from jsix.main import JSIXImageFormat

def test_save_and_load_image():
    # Prepare test data
    pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    image = JSIXImageFormat(2, 2, pixels)
    test_filename = 'test_image.jsix'

    image.save(test_filename)

    loaded_image = JSIXImageFormat.load(test_filename)

    assert loaded_image.width == 2
    assert loaded_image.height == 2
    assert loaded_image.pixel_depth == 3
    assert loaded_image.pixels == pixels
