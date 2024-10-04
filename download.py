import os
import requests

# Base URL for constructing download links
BASE_URL = 'http://localhost:8080/styles/basic-preview/512'

# Function to download the image from the constructed URL
def download_image(folder_path, filename):
    print(folder_path)
    real_path = folder_path.replace("./Downloads/tiles", "")
    #real_name = filename.replace(".pbf", ".png")
    image_url = BASE_URL + real_path.replace(os.sep, '/') + '/' + filename
    
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image_save_path = os.path.join(folder_path, filename)
            with open(image_save_path, 'wb') as f:
                f.write(response.content)
            print(f"Image saved to {image_save_path}")
        else:
            print(f"Failed to download image from {image_url}")
    except Exception as e:
        print(f"Error with {image_url}: {e}")

# Function to traverse the directory structure and download images
def traverse_and_download_images(base_directory):
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            download_image(root, file)

# Example usage: Specify the base directory where your folder structure exists
base_directory = './Downloads/tiles'
traverse_and_download_images(base_directory)