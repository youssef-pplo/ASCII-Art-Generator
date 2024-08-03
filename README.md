# ASCII Art Generator

This project is an ASCII Art Generator that converts images into ASCII art. It features a web-based interface allowing users to drag and drop images, upload files, or paste images from the clipboard to see them converted into ASCII art.

## Features

- **Drag and Drop**: Drop images anywhere on the page to convert them to ASCII art.
- **File Upload**: Select image files directly from your computer.
- **Paste Images**: Paste images from the clipboard to convert them.
- **Adjustable Size**: Control the width of the ASCII output using a number selector.
- **Copy to Clipboard**: Easily copy the ASCII art to your clipboard.
- **Loading Indicator**: Visual feedback while the image is being processed.

## Requirements

- Python 3.x
- Flask
- Pillow
- numpy

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Youssef-pplo/ascii-art-generator.git
    cd ascii-art-generator
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**

    ```bash
    python app.py
    ```

5. **Open your browser and navigate to** `http://127.0.0.1:5000` **to use the application.**

## Usage

- **Drag and Drop**: Drag and drop an image into the designated area to convert it to ASCII art.
- **File Upload**: Click the "Select Image" button to choose an image file from your computer.
- **Paste Image**: Paste an image from the clipboard directly into the web page.
- **Adjust Size**: Use the number selector to set the width of the ASCII output.

## Credits

- **Youssef Elsayed** - [pplo.dev](https://pplo.dev) - [GitHub](https://github.com/Youssef-pplo)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
