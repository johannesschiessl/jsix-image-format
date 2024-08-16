import sys
from jsix_format.main import JSIXImageFormat

def convert_png_to_jsix(png_filename, jsix_filename):
    JSIXImageFormat.png_to_jsix(png_filename, jsix_filename)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_png_to_jsix.py <input.png> <output.jsix>")
        sys.exit(1)

    png_filename = sys.argv[1]
    jsix_filename = sys.argv[2]

    convert_png_to_jsix(png_filename, jsix_filename)
    print(f"Converted {png_filename} to {jsix_filename} successfully.")
