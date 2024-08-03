# ASCII Art Generator

## Description

Convert images to ASCII art with a web interface. Drag, drop, or paste images to generate ASCII art.

## Features

- **Drag and Drop:** Easily drag and drop images to convert.
- **File Selection:** Upload images using a file picker.
- **Paste Functionality:** Paste images directly from the clipboard.
- **Customizable Output:** Adjust ASCII art width from 25 to 250 characters.
- **Loading Indicator:** See a loading spinner while processing.
- **Copy to Clipboard:** Copy the ASCII art to your clipboard.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/youssef-pplo/ascii-art-generator.git
    cd ascii-art-generator
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000` to use the application.

## Usage

- **Drag and Drop**: Drag an image file into the designated area.
- **File Picker**: Click "Select Image" to choose a file from your computer.
- **Paste**: Copy an image to your clipboard and paste it to upload.
- **Adjust Width**: Use the number selector to set the width of the ASCII output.
- **Copy Output**: Click the "Copy" button to copy the ASCII art to your clipboard.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
