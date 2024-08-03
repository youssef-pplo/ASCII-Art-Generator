from flask import Flask, request, render_template, jsonify
from PIL import Image
import numpy as np
import base64
from io import BytesIO

app = Flask(__name__)

# Extended ASCII characters set from darkest to lightest for more granularity
ASCII_CHARS = "@#8&$%*o!;:,. "

def resize_image(image, new_width=150):  # Default width
    width, height = image.size
    aspect_ratio = height / width / 1.65  # Adjust for terminal character aspect ratio
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def to_grayscale(image):
    return image.convert("L")

def image_to_ascii(image, width):
    image = resize_image(image, width)
    image = to_grayscale(image)

    pixels = np.array(image)
    ascii_str = ""
    scale = 255 / (len(ASCII_CHARS) - 1)
    for pixel_row in pixels:
        for pixel in pixel_row:
            ascii_str += ASCII_CHARS[int(pixel / scale)]
        ascii_str += "\n"

    return ascii_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    image_data = base64.b64decode(data['image'].split(",")[1])
    image = Image.open(BytesIO(image_data))
    ascii_art = image_to_ascii(image, data.get('width', 150))
    return jsonify({'ascii_art': ascii_art})

if __name__ == "__main__":
    app.run(debug=True)
