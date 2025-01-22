import os
import requests
from PIL import Image, UnidentifiedImageError
import hashlib
import io
from datetime import datetime

def calculate_image_hash(img_data):
    """
    Calculate the MD5 hash of an image for duplicate detection.
    """
    return hashlib.md5(img_data).hexdigest()

def download_image(download_dir, img_url, query, index, website, existing_hashes):
    """
    Download and verify an image while checking for duplicates.
    """
    try:
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()
        img_data = response.content

        img_hash = calculate_image_hash(img_data)
        if img_hash in existing_hashes:
            print(f"Skipped duplicate image: {img_url}")
            return False
        existing_hashes.add(img_hash)

        with Image.open(io.BytesIO(img_data)) as img:
            img.verify()
            img_format = img.format.lower()
            if img_format not in ["jpeg", "jpg", "png"]:
                print(f"Skipped unsupported format: {img_url}")
                return False

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        filepath = os.path.join(download_dir, f"{query}_{index}_{website}_{timestamp}.jpg")
        with open(filepath, 'wb') as img_file:
            img_file.write(img_data)
        print(f"Downloaded: {filepath}")
        return True
    except (UnidentifiedImageError, IOError):
        print(f"Failed to identify image format: {img_url}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {img_url} - {e}")
        return False
