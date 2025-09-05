import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt user for URL
    url = input("🌍 Enter an image URL: ").strip()

    # Directory to store images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)  # create if not exists

    try:
        # Fetch image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # if URL doesn’t end with a filename
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # Save the file in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✅ Image saved to {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Error: Invalid URL. Please include http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Error: The request timed out.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


if __name__ == "__main__":
    print("✨ Ubuntu Image Fetcher ✨")
    print('"I am because we are" – Fetching images with respect and sharing 🌍')
    fetch_image()
