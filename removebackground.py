from rembg import remove

def remove_bg(input_path, output_path):
    with open(input_path, "rb") as i:
        with open(output_path, "wb") as o:
            o.write(remove(i.read()))
    return output_path
