from PIL import Image
import numpy as np

def jpg_to_mem(input_jpg, output_mem):
    # Open image and get dimensions
    with Image.open(input_jpg) as img:
        width, height = img.size

    # Read the binary content of the JPEG file
    with open(input_jpg, "rb") as f:
        binary_data = f.read()

    # Convert binary data to a bit string
    bit_string = ''.join(f"{byte:08b}" for byte in binary_data)

    # Pad with zeros to make the total length a multiple of 128
    padding_length = (128 - (len(bit_string) % 128)) % 128
    bit_string = bit_string.ljust(len(bit_string) + padding_length, '0')

    # Write to the .mem file with 8 bits per line
    with open(output_mem, "w") as f:
        for i in range(0, len(bit_string), 8):
            f.write(bit_string[i:i+8] + '\n')

    # Return total lines in the .mem file and image dimensions
    total_lines = len(bit_string) // 8
    return total_lines, (width, height)

# *For Google Colab: Upload File*
from google.colab import files

uploaded = files.upload()  # Upload image
input_jpg = list(uploaded.keys())[0]  # Get uploaded filename
output_mem = "output.mem"

# Convert JPG to .mem
total_lines, dimensions = jpg_to_mem(input_jpg, output_mem)

print(f"✅ Total lines in {output_mem}: {total_lines}")
print(f"🖼️ Original Image Dimensions: {dimensions}")  # Returns (width, height)

# *For Google Colab: Download File*
files.download(output_mem)