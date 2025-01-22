# Web Image Scraper

## Overview
The Image Scraper is a Python-based tool designed to automate the process of downloading images from the web while verifying their format and ensuring no duplicates are stored. It provides a modular structure that allows developers to extend functionality for various platforms such as Unsplash or Google Images.

## Features
- Automated image downloading based on user queries.
- Duplicate image detection using MD5 hashing.
- Image format verification (supports JPEG, JPG, PNG).
- Modular design for easy extension to additional platforms.

## Usage
### Prerequisites
- Python 3.8+
- Google Chrome browser
- ChromeDriver installed and accessible (ensure the path is configured).

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Justinian-I/Web-image-scraper.git 
   cd Web-image-scraper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update the `chrome_driver_path` variable in `src/main_scraper.py` to point to your ChromeDriver location.

### Running the Scraper
To run the scraper, use:
```bash
python src/main_scraper.py
```
Follow the prompts to enter a search query and the number of images to download.

#### Example Input
```text
Enter the search query: cats
Enter the total number of images to download: 10
```

#### Example Outcome
Downloaded images are stored in a directory named after the query (e.g., `cats`). Each image file is uniquely named and verified to avoid duplicates. Example path:
```text
C:/Users/YourUsername/Downloads/cats/
```
Sample image filenames:
- `cats_1_google_20250120123456.jpg`
- `cats_2_google_20250120123501.jpg`

### Extending Functionality
To add support for a new platform, modify the `scraper` function in `src/scraper_interface.py` and implement the platform-specific logic.

## Limitations
- This is a simplified version and does not include full implementations for platform-specific scraping.
- Designed for educational and non-commercial use. Ensure compliance with website terms of service.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer
Use this tool responsibly. Ensure that scraping does not violate the terms of service of any platform. The authors are not liable for misuse.

