import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class ProcessUrl:
    """Process URL"""

    def __init__(self, url: str) -> None:
        self.__driver = self.__get_driver()
        self.__driver.get(url)
    
    def get_some_data(self) -> str:
        h1 = self.__driver.find_element_by_tag_name('h1').text
        p = self.__driver.find_element_by_tag_name('p').text
        self.__driver.quit()
        return f'{h1.strip()}\n{p.strip()}'
    
    def get_title(self) -> str:
        """Get tag title of html

        Returns:
            str: title
        """
        title = self.__driver.title
        self.__driver.quit()
        return title

    async def get_screenshot(self, file_name: str) -> str:
        """Sreenshot a webpage using selenuim

        Args:
            url (str): url of a webpage 

        Returns:
            str: location of the screenshot
        """
        path = os.path.join(self.screenshot_location(), file_name + '.png')
        self.__driver.save_screenshot(path)
        self.__driver.quit()

        return path
    
    @staticmethod
    def screenshot_location() -> str:
        """Make screenshot folder location if not exists

        Returns:
            str: folder location
        """
        temp_dir = tempfile.gettempdir()
        dir_path = os.path.join(temp_dir, 'screenshot')

        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            
        return dir_path
        
    @staticmethod
    def __get_driver():
        """Get driver of selenium chrome"""
        chrome_driver = ChromeDriverManager().install()
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        return webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
