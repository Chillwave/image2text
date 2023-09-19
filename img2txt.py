import pytesseract
from PIL import Image
import sys

# You must set the Tesseract path to where you have Tesseract installed on your PC
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Get the file path from the first command line argument
image_file_path = sys.argv[1]

# Open image file with PIL
image = Image.open(image_file_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Print the text
print(text)
