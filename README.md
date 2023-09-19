# Image to Text Converter

This is a simple Python script that takes an image file as an argument and uses the Tesseract OCR engine to convert the text in the image to plain text. Used in Kubuntu 22.04.

## Requirements

This script requires the following Python libraries: 
- Pillow
- pytesseract

Along with these Python dependencies, you will also need to have Tesseract OCR installed on your machine.

## Installation

### Python Dependencies

You can install the required Python libraries with pip:

```
pip install Pillow pytesseract
```

### Tesseract OCR

To install Tesseract OCR, use the following command:
```
sudo apt install tesseract-ocr
```
After installation, you can locate its path by entering:
```
which tesseract
```

This path will need to be included in the script where Tesseract's path is specified.

## Usage

This script is run via the command line and takes the path of the image file as an argument.

```
python3 image_to_text.py path_to_your_image.png
```

This script will then print the extracted text to the console.
