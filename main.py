from PIL import Image
import numpy as np

# Extended ASCII characters set from darkest to lightest for more granularity
ASCII_CHARS = "@#8&$%*o!;:,. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width / 1.65  # Adjust for terminal character aspect ratio
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def to_grayscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    scale = 255 / (len(ASCII_CHARS) - 1)
    for pixel in pixels:
        ascii_str += ASCII_CHARS[int(pixel / scale)]
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return ""

    image = resize_image(image, new_width)
    image = to_grayscale(image)

    pixels = np.array(image)
    ascii_str = ""
    scale = 255 / (len(ASCII_CHARS) - 1)
    for pixel_row in pixels:
        for pixel in pixel_row:
            ascii_str += ASCII_CHARS[int(pixel / scale)]
        ascii_str += "\n"

    return ascii_str

# Test the function
if __name__ == "__main__":
    path = "download.png"  # Replace with your image path
    ascii_art = image_to_ascii(path, new_width=100)
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_art)
    print(ascii_art)
