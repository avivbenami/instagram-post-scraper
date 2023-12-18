<a name="readme-top"></a>
<div align="center">
  <h3 align="center">Instagram Post Scraper</h3>

  <p align="center">
    A Selenium-based scraper for checking if Instagram posts contain sensitive content.
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a Selenium-based scraper designed to check if Instagram posts contain sensitive content. It utilizes headless Chrome to access Instagram post URLs, and verify the presence of sensitive content based on the page source.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [Selenium](https://www.selenium.dev/)
* [Chrome Driver](https://sites.google.com/chromium.org/driver/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* [Python](https://www.python.org/)
* [Chrome Browser](https://www.google.com/chrome/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/avivbenami/instagram-post-scraper.git
   ```

2. Navigate to the project directory
   ```sh
   cd instagram-post-scraper
    ```

3. Create a virtual environment
   ```sh
   python -m venv .venv
    ```

4. Activate the virtual environment
   ```sh
   .\.venv\Scripts\activate
   ```

5. Install dependencies
   ```sh
   pip install -r requirements.txt
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage


   ```python
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
        urls = ["https://www.instagram.com/cristiano/reel/C09VyjZtoyx/", 
        "https://www.instagram.com/reel/C0tWyIktI1Y"]
        print(get_sens(urls))
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Improve error handling
- [ ] Proxy management 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/avivbenami/instagram-post-scraper](https://github.com/avivbenami/instagram-post-scraper)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Selenium Documentation](https://www.selenium.dev/documentation/en/)
* [Python Documentation](https://docs.python.org/3/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
