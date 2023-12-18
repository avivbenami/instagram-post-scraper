from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class InstagramPostScraper:
    def __init__(self, post_url: str) -> None:
        self.post_url = post_url
        self.driver = self._create_driver()

    def _create_driver(self) -> webdriver:
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
        
        # Set logging preferences to ignore INFO level messages
        chrome_options.add_argument('log-level=3')
        
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def get_page_source(self) -> str:
        try:
            self.driver.get(self.post_url)
            time.sleep(5)  # Wait for the page to load

            # Scroll to the bottom of the page to load dynamic content (optional)
            self._scroll_to_bottom()

            # Retrieve the page source
            page_source = self.driver.page_source
            return page_source
        finally:
            self.driver.quit()

    def is_sensitive(self) -> bool:
        page_source = self.get_page_source()
        if ("<title>Sensitive content overlay icon</title>" in page_source):
            return True
        return False
    
    def _scroll_to_bottom(self) -> None:
        # Scroll to the bottom of the page to load dynamic content
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.END)
        time.sleep(2)  # Wait for the content to load


def get_sens(url_list: list) -> list:
    sensitive_urls = []

    for url in url_list:
        # Create an instance of InstagramPostScraper for the current URL
        scraper = InstagramPostScraper(url)

        # Sleep for 2 seconds between requests
        time.sleep(2)

        # Check if the post is sensitive
        if scraper.is_sensitive():
            sensitive_urls.append(url)

    return sensitive_urls

if __name__ == "__main__":
    urls = ["https://www.instagram.com/cristiano/reel/C09VyjZtoyx/", "https://www.instagram.com/reel/C0tWyIktI1Y"]
    print(get_sens(urls))
