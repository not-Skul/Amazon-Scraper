# Amazon Product Scraper

A Python-based web scraping tool that extracts product information from Amazon India, including product names, prices, and URLs. The scraper uses Selenium with stealth mode to avoid detection and can scrape multiple pages of search results.

## Features

- 🔍 Search for any product on Amazon India
- 📄 Scrape multiple pages of search results
- 🥷 Stealth mode to avoid bot detection
- 📊 Export data to pandas DataFrame
- 💰 Extract product names, prices, and URLs
- 🖥️ Headless browser mode for background operation

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone this repository or download the project files:
```bash
git clone <repository-url>
cd AmazonFinder
```

2. Install required Python packages:
```bash
pip install selenium pandas selenium-stealth
```

3. Download ChromeDriver:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Download the version matching your Chrome browser
   - Add ChromeDriver to your system PATH or place it in the project directory

## Usage

1. Run the script:
```bash
python main.py
```

2. Enter the product you want to search for when prompted:
```
Which product do you want to search for: laptop
```

3. Enter the number of pages to scrape:
```
how many pages do you want to scrape: 5
```

4. The script will:
   - Navigate through Amazon India search results
   - Extract product information from each page
   - Display the number of items discovered on each page
   - Print the final DataFrame with all collected data

## Output

The scraper collects the following information for each product:
- **Product Name**: The title/name of the product
- **Price**: The price in Indian Rupees (₹)
- **URL**: Direct link to the product page

The data is stored in a pandas DataFrame and displayed in the console.

## Project Structure

```
AmazonFinder/
│
├── main.py           # Main scraper script
├── product.csv       # Sample output file
├── data/             # Directory containing cached HTML files
│   ├── laptop_0.html
│   ├── laptop_1.html
│   └── ...
├── opensea.png       # Project related images
├── opensea2.png
└── README.md         # This file
```

## Configuration

### Stealth Settings
The scraper uses selenium-stealth with the following configuration:
- User Agent: Chrome 110 on Windows 10
- Languages: en-US, en
- Platform: Win32
- WebGL Vendor: Intel Inc.

### Chrome Options
- Automation flags are disabled to avoid detection
- Headless mode is enabled for background operation

## Important Notes

⚠️ **Legal and Ethical Considerations:**
- Web scraping may violate Amazon's Terms of Service
- Use this tool responsibly and respect rate limits
- Consider using Amazon's official Product Advertising API for commercial purposes
- This tool is for educational purposes only

⚠️ **Technical Considerations:**
- Amazon's website structure may change, requiring updates to selectors
- Some products may not have prices displayed, which can cause errors
- The scraper includes basic error handling but may need improvements
- Network issues or slow connections may affect results

## Troubleshooting

### Common Issues

1. **ChromeDriver version mismatch:**
   - Ensure ChromeDriver version matches your Chrome browser version
   - Download the correct version from the ChromeDriver website

2. **Element not found errors:**
   - Amazon's HTML structure may have changed
   - Check and update CSS selectors in the code

3. **Bot detection:**
   - Amazon may block automated requests
   - The stealth mode helps but is not foolproof
   - Consider adding random delays between requests

4. **No data available:**
   - Check your internet connection
   - Verify the product search term is valid
   - Amazon may be blocking your IP temporarily

## Future Enhancements

- [ ] Export data to CSV file automatically
- [ ] Add support for multiple Amazon regions (.com, .uk, etc.)
- [ ] Implement better error handling and logging
- [ ] Add filters for price range, ratings, etc.
- [ ] Create a GUI interface
- [ ] Add data visualization features
- [ ] Implement retry logic for failed requests
- [ ] Add support for product reviews scraping

## Dependencies

- `selenium` - Web browser automation
- `pandas` - Data manipulation and analysis
- `selenium-stealth` - Avoid bot detection
- `time` - Built-in Python module for delays

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is provided as-is for educational purposes only. Use at your own risk and ensure compliance with applicable laws and terms of service.

## Disclaimer

This tool is intended for educational and research purposes only. The authors are not responsible for any misuse or for any damages that may result from using this software. Always respect website terms of service and robots.txt files.

## Contact

For questions or suggestions, please open an issue in the repository.

---

**Note:** Always check and comply with Amazon's Terms of Service and robots.txt file before scraping their website.

