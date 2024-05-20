from selenium import webdriver
from rich.console import Console



class Scraping:
    
    def __init__(self, url:str):
        self.url = url
        self.console = Console()
        #self.options = webdriver.ChromeOptions()
        #self.options.add_argument("--headless=new") options=self.options
        
    def __enter__(self):
        self.scraping = webdriver.Chrome()
        self.scraping.implicitly_wait(3)
        self.scraping.get(self.url)
        return self.scraping

    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_type != None:
            self.console.print(f"Erro do tipo:{exc_type} | {exc_value}, {exc_trace}", style="red")
        else:    
            self.scraping.quit()