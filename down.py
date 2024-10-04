import os
import requests

def download_images(url_pattern, start, end, save_directory):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    for i in range(start, end + 1):
        # Construct the image URL using the integer
        image_url = url_pattern.format(i)
        image_filename = f"{i}.png"
        image_path = os.path.join(save_directory, image_filename)
        
        try:
            # Send the HTTP request to download the image
            response = requests.get(image_url, stream=True)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                with open(image_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Downloaded: {image_filename}")
            else:
                print(f"Failed to download: {image_url} - Status code: {response.status_code}")
        
        except Exception as e:
            print(f"An error occurred while downloading {image_url}: {e}")

# Example usage
url_pattern = "http://localhost:8080/styles/basic-preview/256/14/8013/{}.png"  # URL pattern where {} will be replaced with the integer
start = 1290  # Start of the range
end = 1317   # End of the range
save_directory = "./Downloads/8013/"  # Local directory to save the images

download_images(url_pattern, start, end, save_directory)