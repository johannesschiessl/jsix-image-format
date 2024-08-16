import pytest
from unittest import mock
from jsix.jsix_format.pixel_data import write_pixels, read_pixels

@pytest.fixture
def sample_pixels():
    return [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

def test_write_pixels(sample_pixels):
    mock_file = mock.mock_open()

    with mock.patch('builtins.open', mock_file):
        with open('test_file', 'w') as f:
            write_pixels(f, sample_pixels)

    mock_file().write.assert_any_call("FF0000\n")  # Red
    mock_file().write.assert_any_call("00FF00\n")  # Green
    mock_file().write.assert_any_call("0000FF\n")  # Blue

def test_read_pixels(sample_pixels):
    mock_file = mock.mock_open(read_data="FF0000\n00FF00\n0000FF\n")

    with mock.patch('builtins.open', mock_file):
        with open('test_file', 'r') as f:
            pixels = read_pixels(f, 1, 3, 3)

    assert pixels == sample_pixels
