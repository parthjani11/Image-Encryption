#  Image Encryption Using Verilog and Google Colab

This project demonstrates a complete image encryption system using an AES-128 encryption core written in Verilog. The encryption is performed at the **RTL simulation level** using ModelSim, while Python scripts in Google Colab handle image processing and visualization.

---

##  Project Workflow

### 1. Image Upload in Google Colab  
The process starts by uploading a `.jpg` image in Google Colab. This image serves as the input for the encryption process.

### 2. Convert Image to Memory Format (`output.mem`)  
The uploaded image is converted into a memory file that contains the binary representation of the image, with each line storing 8 bits. The bitstream is padded (if required) so its total length becomes a multiple of 128 bits, which matches the AES block size.

### 3. Simulated AES Encryption in Verilog (ModelSim)  
The generated `output.mem` file is processed using a Verilog module that implements the AES-128 encryption algorithm.  
This simulation is run in **ModelSim**, which simulates how the encryption logic would behave in real hardware. The module reads 128-bit blocks from the file, encrypts them, and writes the results to a new file called `encrypted.mem`.

### 4. Convert Encrypted Memory to Image  
The `encrypted.mem` file is uploaded back into Colab. A Python script reads the AES-encrypted hex values, converts them to grayscale pixel data, and reconstructs them into an encrypted image.  
This image visually represents the encrypted data and appears completely different from the original, though it is derived from it.

---

##  Tools Used

- **ModelSim:**  
  Simulates the Verilog AES encryption module at the RTL level. It verifies the logic and behavior of the design without requiring physical hardware like an FPGA.

- **Google Colab:**  
  Used for:
  - Uploading and processing images
  - Converting images to memory format and back
  - Displaying the encrypted image
  - Running Python scripts without local installation

- **Python (NumPy & PIL):**  
  Handles image data transformation, memory file generation, and final image reconstruction.

---

##  Final Outcome

At the end of the flow:
- The input image is converted into binary form.
- It is then **simulated through AES-128 encryption** using Verilog in ModelSim.
- The output is transformed back into an image to visualize the encrypted data.

This project demonstrates a complete **encryption simulation pipeline** integrating digital design (Verilog) with modern data processing tools (Python, Colab).
