import os
import requests

def download_images_from_url_pattern(base_url_pattern, folder_start, folder_end, file_start, file_end, base_directory):
    # Loop over the folder range
    for folder_num in range(folder_start, folder_end + 1):
        # Loop over the file range
        for file_num in range(file_start, file_end + 1):
            # Define the folder and file names using the current integers
            folder_name = str(folder_num)
            image_filename = f"{file_num}.png"
            
            # Create the local folder path
            local_folder_path = os.path.join(base_directory, folder_name)
            os.makedirs(local_folder_path, exist_ok=True)  # Create folder if it doesn't exist

            # Construct the image URL using the folder and file names
            image_url = base_url_pattern.format(folder_name, image_filename)
            
            # Define the local image path where the image will be saved
            local_image_path = os.path.join(local_folder_path, image_filename)
            
            try:
                # Download the image
                response = requests.get(image_url, stream=True)
                
                # Check if the request was successful
                if response.status_code == 200:
                    # Save the image in the corresponding folder
                    with open(local_image_path, 'wb') as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    print(f"Downloaded: {image_filename} in folder {folder_name}")
                else:
                    print(f"Failed to download: {image_url} - Status code: {response.status_code}")
            
            except Exception as e:
                print(f"An error occurred while downloading {image_url}: {e}")

# Example usage
base_url_pattern = "http://localhost:8080/styles/basic-preview/512/15/{}/{}"  # URL pattern with placeholders for folder and file
folder_start = 16029  # Start of the folder range
folder_end = 16187    # End of the folder range
file_start = 10340    # Start of the file range
file_end = 10537      # End of the file range
base_directory = "./Downloads/temp/"  # Local base directory for saving images

download_images_from_url_pattern(base_url_pattern, folder_start, folder_end, file_start, file_end, base_directory)