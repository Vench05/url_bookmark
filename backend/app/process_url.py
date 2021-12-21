import os
import tempfile
from typing import List
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


class ProcessUrl:
    """Process URL"""

    def __init__(self, url: str):
        self.__driver = self.__get_driver()
        self.__driver.get(url)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__driver.quit()

    def get_some_data(self, tags: List[str] = ['h1', 'p']) -> str:
        info = []
        for tag in tags:
            try:
                info.append(self.__driver.find_element_by_tag_name(tag).text)
            except NoSuchElementException as e:
                print(f'Error: {e}')
        return ' '.join(info)

    def get_title(self) -> str:
        """Get tag title of html

        Returns:
            str: title
        """
        title = self.__driver.title
        return title

    def get_screenshot(self, file_name: str) -> str:
        """Sreenshot a webpage using selenuim

        Args:
            url (str): url of a webpage 

        Returns:
            str: location of the screenshot
        """
        path = os.path.join(self.screenshot_location(), file_name + '.png')
        self.__driver.save_screenshot(path)

        return path

    # @staticmethod
    # def screenshot_location() -> str:
    #     """Make screenshot folder location if not exists

    #     Returns:
    #         str: folder location
    #     """
    #     temp_dir = tempfile.gettempdir()
    #     dir_path = os.path.join(temp_dir, 'screenshot')

    #     if not os.path.isdir(dir_path):
    #         os.makedirs(dir_path)

    #     return dir_path
    
    @staticmethod
    def screenshot_location() -> str:
        """Make screenshot folder location if not exists

        Returns:
            str: folder location
        """
        dir_path = os.path.abspath(os.path.join(os.pardir, 'frontend', 'src', 'image'))

        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

        return dir_path

    def __get_driver(self):
        """Get driver of selenium chrome"""
        chrome_driver = ChromeDriverManager().install()
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        return webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)

    def __get_driver_in_docker(self):
        """Get driver of selenium chrome in docker"""
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        return webdriver.Remote("http://chrome:4444", options=options, desired_capabilities=DesiredCapabilities.CHROME)
