# Image Steganography

This Python script enables you to perform image steganography operations, such as encoding and decoding text messages within images using OpenCV.

## Requirements
- Python 3.x
- OpenCV (`cv2`)

## Usage

1. Ensure you have Python installed on your system.
2. Install OpenCV using `pip install opencv-python`.
3. Place the script in your working directory and ensure you have an image file (e.g., `image.jpg`) in the same directory.

### Encoding Data into an Image
- Run the script.
- Choose option 1 to encode a text message into the image.
- Enter the text message to be encoded.
- Provide a name for the new image (stego image) after encoding, including the file extension (e.g., `.png`, `.jpg`, `.bmp`).
- The script will encode the data into the image and save it with the specified name.

### Decoding Data from an Image
- Run the script.
- Choose option 2 to decode a text message from an image.
- Enter the name of the image file from which you want to decode the hidden message.
- The script will extract and display the hidden message from the image.

### Exiting
- Choose option 3 to exit the script.

## Notes
- The script utilizes the least significant bit (LSB) technique to encode and decode data into/from the image.
- Ensure that the image file provided for encoding and decoding is in the same directory as the script.
- Supported image file extensions for encoding are `.png`, `.jpg`, `.jpeg`, and `.bmp`.

**Note:** This script is for educational purposes only. Make sure to respect privacy and legal regulations when using steganography techniques.
