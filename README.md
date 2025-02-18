# 🖼 Image Filtering with Convolution Kernels

This project uses convolution kernels in Python to apply various image-filtering techniques. Users can modify an image using different effects, such as edge detection, sharpening, and blurring. The program processes the selected area of the image using a kernel-based convolution operation.

## 💡 Why This Project?
Image processing is essential in various applications such as computer vision, and machine learning. This project provides an interactive way to understand how convolution kernels modify images. It allows users to experiment with different filters and observe their effects.

## 🚀 Project Overview

🔍 Goal: Apply user-selected filters to an image efficiently.

🔧 Features:
- Various Filtering Options:
  - No effect
  - Edge Detection
  - Image Sharpening
  - Image Blurring
- Flexible Processing:
  - Apply effects to the entire image
  - Apply effects to a specific region of the image

## 🛠 Tech Stack
- Programming Language: Python
- Matrix Operations: NumPy
- Image Handling: PIL
- Image Display: Matplotlib

## ✨ Convolution Kernels Used
- Edge Detection:
```bash
[[-1, -1, -1],
 [-1,  8, -1],
 [-1, -1, -1]]
```
```bash
Sharpening:

[[ 0, -1,  0],
 [-1,  5, -1],
 [ 0, -1,  0]]
```
```bash
Blurring:

[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
```

## 📜 How It Works
1. The user selects an effect from the available options.
2. The user chooses whether to apply the effect to the whole image or just a portion of it.
3. The program applies a 3×3 convolution kernel to process the image.
4. The result is displayed using Matplotlib.

## 📊 Results
- Edge Detection: Highlights the edges of objects in the image.
- Sharpening: Enhances the details and sharpness of the image.
- Blurring: Makes the image look softer and more blurry.

## 🏗 How to Run

1️⃣ Clone this repository
```bash
  git clone https://github.com/vierikurniawan/Image-Filtering-Kernels.git  
  cd Image-Filtering-Kernels  
```
2️⃣ Install dependencies
```
  pip install numpy matplotlib pillow
```
3️⃣ Run the script
```
  python Image Filtering Using Convolution Kernels.py
```
