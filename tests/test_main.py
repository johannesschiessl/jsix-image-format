import pytest
from unittest import mock
from PIL import Image
from io import StringIO
from jsix.jsix_format.main import JSIXImageFormat

@pytest.fixture
def sample_pixels():
    return [(255, 0, 0), (0, 255, 0), (0, 0, 255)] * 10

@pytest.fixture
def sample_jsix_image(sample_pixels):
    return JSIXImageFormat(3, 10, sample_pixels)

def test_jsiximageformat_initialization(sample_jsix_image, sample_pixels):
    assert sample_jsix_image.magic_number == "JSIXIMAGEFORMAT"
    assert sample_jsix_image.width == 3
    assert sample_jsix_image.height == 10
    assert sample_jsix_image.pixel_depth == 3
    assert sample_jsix_image.pixels == sample_pixels

@mock.patch('your_module.write_header')
@mock.patch('your_module.write_pixels')
def test_jsiximageformat_save(mock_write_pixels, mock_write_header, sample_jsix_image):
    mock_file = mock.mock_open()

    with mock.patch('builtins.open', mock_file):
        sample_jsix_image.save('test.jsix')

    mock_file.assert_called_once_with('test.jsix', 'w')
    mock_write_header.assert_called_once_with(mock_file(), 'JSIXIMAGEFORMAT', 3, 10, 3)
    mock_write_pixels.assert_called_once_with(mock_file(), sample_jsix_image.pixels)

@mock.patch('your_module.read_header')
@mock.patch('your_module.read_pixels')
def test_jsiximageformat_load(mock_read_pixels, mock_read_header, sample_pixels):
    mock_read_header.return_value = ("JSIXIMAGEFORMAT", 3, 10, 3)
    mock_read_pixels.return_value = sample_pixels

    mock_file = mock.mock_open(read_data="fake_data")

    with mock.patch('builtins.open', mock_file):
        jsix_image = JSIXImageFormat.load('test.jsix')

    mock_file.assert_called_once_with('test.jsix', 'r')
    mock_read_header.assert_called_once_with(mock_file())
    mock_read_pixels.assert_called_once_with(mock_file(), 3, 10, 3)

    assert jsix_image.magic_number == "JSIXIMAGEFORMAT"
    assert jsix_image.width == 3
    assert jsix_image.height == 10
    assert jsix_image.pixel_depth == 3
    assert jsix_image.pixels == sample_pixels

@mock.patch('PIL.Image.open')
def test_jsiximageformat_from_png(mock_image_open, sample_pixels):
    mock_image = mock.Mock()
    mock_image.convert.return_value = mock_image
    mock_image.size = (3, 10)
    mock_image.getdata.return_value = sample_pixels
    mock_image_open.return_value = mock_image

    jsix_image = JSIXImageFormat.from_png('test.png')

    mock_image_open.assert_called_once_with('test.png')
    mock_image.convert.assert_called_once_with('RGB')
    assert jsix_image.width == 3
    assert jsix_image.height == 10
    assert jsix_image.pixels == sample_pixels

@mock.patch('your_module.JSIXImageFormat.save')
@mock.patch('your_module.JSIXImageFormat.from_png')
def test_jsiximageformat_png_to_jsix(mock_from_png, mock_save, sample_jsix_image):
    mock_from_png.return_value = sample_jsix_image

    JSIXImageFormat.png_to_jsix('test.png', 'test.jsix')

    mock_from_png.assert_called_once_with('test.png')
    mock_save.assert_called_once_with('test.jsix')
