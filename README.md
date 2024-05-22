# Pinterest Image Data Crawler
Image data crawler (web scrapping) program for Pinterest. Crawl images of Pinterest's specified search query.

# Installation
1. Create conda environment by <b>environment.yml</b>
<blockquote>conda env create -f environment.yml</blockquote>

2. Activate conda environment
<blockquote>conda activate pinterest-data-crawling</blockquote>

3. Run Python command
<blockquote>python main.py</blockquote>

Program will crawl images from Pinterest and crawled images will be downloaded into <I>/data/downloads/</I> by query.

# Selenium Installation for MacOS

Follow these steps to install Selenium:

1. **Give permission to the script.**
    ```
    chmod +x mac_update_chromedriver_and_chrome.sh
    ```
2. **Run the script.**
    ```
    ./mac_update_chromedriver_and_chrome.sh
    ```
3. **Check if Google Chrome and ChromeDriver are successfully installed.**
    ```
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version && chromedriver --version
    ```

## Troubleshooting

If you encounter an installation error, follow these steps:

- Navigate to "System Preferences" --> "Security & Privacy"
- Click "Allow Anyway"
  
## Test Selenium 

To test if Selenium is working correctly, run the `test.py` script:

```bash
python test.py