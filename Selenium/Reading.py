import selenium
import selenium.webdriver as driver
import os 
from selenium.webdriver.firefox.options import Options
import time

class parser:
    def set_browser(self):
        foptions = Options()
        foptions.add_argument('--no-sandbox')
        self.driver = driver.Firefox(executable_path= os.path.join(self.root_dir, "geckodriver.exe"), options=foptions)

    def main(self):
        self.root_dir = os.path.dirname(__file__)
        self.set_browser()

        self.driver.get("http://www.fish-text.ru")
        elem = self.driver.find_element_by_xpath('//div[@id=\"result-container\"]')
        text_elem = getattr(elem, "text")
        print(f"[TEXT BEFORE UPDATE]:\n{text_elem}\n\n")
        btn = self.driver.find_element_by_id("renew-text")
        time.sleep(1)
        btn.click()
        elem2 = self.driver.find_element_by_xpath('//div[@id=\"result-container\"]')
        text_elem2 = getattr(elem2, "text")
        print(f"[TEXT AFTER UPDATE]:\n{text_elem2}\n\n")

        self.driver.close()

obj = parser()
obj.main()