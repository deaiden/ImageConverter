from PIL import Image
import os

# Define the image path
username = os.getlogin()
img_filename = 'YourImage.Blah'  # Replace 'your_image.jpg' with your actual image file name
img_path = f'C:\\Users\\{username}\\Pictures\\Python\\{img_filename}'

# Open the image file
img = Image.open(img_path)
# The format here is necessary to convert PNG (RGBA) to JPEG (RGB)
img = img.convert('RGB')

# Define the output filename and path for the compressed image
output_filename = 'compressed_' + img_filename  # Change 'compressed_your_image.jpg' as needed
output_path = f'C:\\Users\\{username}\\Pictures\\Python\\{output_filename}'

# Function to compress image
def compress_image(img, output_path, quality):
    img.save(output_path, 'JPEG', quality=quality)
    return os.path.getsize(output_path)

# Initialize the quality for JPEG saving
quality = 95  # Start with high quality

# Compress the image until it's less than 1mb
while compress_image(img, output_path, quality) > 1 * 1024 * 1024:
    quality -= 5  # Reduce quality by 5
    if quality < 10:  # Stop if quality gets too low
        break

# Return the path to the compressed image and its size
print(output_path, os.path.getsize(output_path))
