def write_header(f, magic_number, width, height, pixel_depth):
    f.write(magic_number + '\n')
    f.write(f"{width:08X}\n")
    f.write(f"{height:08X}\n")
    f.write(f"{pixel_depth:08X}\n")

def read_header(f):
    magic_number = f.readline().strip()
    width = int(f.readline().strip(), 16)
    height = int(f.readline().strip(), 16)
    pixel_depth = int(f.readline().strip(), 16)
    return magic_number, width, height, pixel_depth
