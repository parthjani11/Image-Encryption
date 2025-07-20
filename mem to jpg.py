import numpy as np
from PIL import Image
from google.colab import files

def mem_to_image(mem_file, output_image="output.png", width=128, height=None):
    """
    Convert a .mem file containing 128-bit hex values into an image.

    :param mem_file: Path to the .mem file
    :param output_image: Path to save the output image
    :param width: Width of the output image (default: 128 pixels)
    :param height: Auto-calculated based on the number of pixels
    """
    byte_data = []

    # Read the uploaded .mem file and skip the first line
    with open(mem_file, "r") as f:
        lines = f.readlines()[1:]  # Skips the first line

        for line in lines:
            line = line.strip()
            if len(line) == 32 and all(c in "0123456789abcdefABCDEF" for c in line):  
                # Convert hex to 16-byte array
                byte_data.extend(bytes.fromhex(line))
            else:
                print(f"⚠️ Skipping invalid line: {line}")

    if not byte_data:
        print("❌ No valid hex data found in the file!")
        return None

    # Convert list to NumPy array
    byte_array = np.array(byte_data, dtype=np.uint8)

    # Calculate image dimensions
    if height is None:
        height = len(byte_array) // width  # Auto height calculation

    # Ensure we have enough data to form a proper image
    if len(byte_array) < height * width:
        print("⚠️ Not enough data to fill the image, resizing accordingly.")
        height = len(byte_array) // width

    # Reshape to match image dimensions
    image_data = byte_array[:height * width].reshape((height, width)) 

    # Create and save image
    img = Image.fromarray(image_data, mode="L")  # Grayscale
    img.save(output_image)

    # Display the image in Colab
    print(f"✅ Image saved as {output_image}")
    return img

# *🔹 Upload .mem File in Google Colab*
uploaded = files.upload()

# Get the first uploaded file name
mem_filename = list(uploaded.keys())[0]

# Convert .mem to Image and display
image = mem_to_image(mem_filename)
if image:
    image.show()