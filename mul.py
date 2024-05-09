import cv2

def encode_img_data(img):
    data = input("\nEnter the data to be encoded in the image: ")
    if len(data) == 0:
        raise ValueError('Data entered to be encoded is empty')

    name_of_file = input("\nEnter the name of the new image (stego image) after encoding (with extension): ")

    # Ensure that the output image filename has a valid extension
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp']
    if not any(name_of_file.endswith(ext) for ext in valid_extensions):
        raise ValueError("Invalid image file extension. Supported extensions are: " + ', '.join(valid_extensions))

    # Calculate the maximum number of bytes that can be encoded in the image
    no_of_bytes = (img.shape[0] * img.shape[1] * 3) // 8
    print("\t\nMaximum bytes to encode in image:", no_of_bytes)

    # Check if the data size exceeds the maximum capacity of the image
    if len(data) > no_of_bytes:
        raise ValueError("Insufficient bytes Error, need a bigger image or less data!")

    # Add a delimiter to the data to mark the end of the message
    data += '*^*^*'

    # Convert the data to binary
    binary_data = ''.join(format(ord(c), '08b') for c in data)
    length_data = len(binary_data)
    print("\nThe Length of Binary data:", length_data)

    index_data = 0

    # Loop through each pixel in the image and modify the least significant bit (LSB) to encode the data
    for i in range(len(img)):
        for pixel in img[i]:
            r, g, b = [format(c, '08b') for c in pixel]

            # Encode the data into the LSB of each color channel
            if index_data < length_data:
                pixel[0] = int(r[:-1] + binary_data[index_data], 2)
                index_data += 1
            if index_data < length_data:
                pixel[1] = int(g[:-1] + binary_data[index_data], 2)
                index_data += 1
            if index_data < length_data:
                pixel[2] = int(b[:-1] + binary_data[index_data], 2)
                index_data += 1
            if index_data >= length_data:
                break

    # Save the encoded image
    cv2.imwrite(name_of_file, img)
    print("\nEncoded the data successfully in the image, and the image is saved with the name:",
          name_of_file)

def decode_img_data(img):
    data_binary = ""
    for i in range(len(img)):
        for pixel in img[i]:
            r, g, b = [format(c, '08b') for c in pixel]
            data_binary += r[-1]
            data_binary += g[-1]
            data_binary += b[-1]
            total_bytes = [data_binary[i:i + 8] for i in range(0, len(data_binary), 8)]
            decoded_data = ""
            for byte in total_bytes:
                decoded_data += chr(int(byte, 2))
                if decoded_data[-5:] == "*^*^*":
                    print("\nThe encoded data hidden in the image is:", decoded_data[:-5])
                    return



def img_steg():
    while True:
        print("\n\t\tIMAGE STEGANOGRAPHY OPERATIONS")
        print("1. Encode the text message")
        print("2. Decode the text message")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            image = cv2.imread("image.jpg")
            encode_img_data(image)
        elif choice == 2:
            image = cv2.imread(input("Enter the image you want to decode to retrieve the secret message: "))
            decode_img_data(image)
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    img_steg()