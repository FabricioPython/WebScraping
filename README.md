
# Web Scraping

**Parte 1:**

Visitar uma plataforma de e-comerce com selenium, buscar produtos (livro de python ou relacionado) por palavra chave e pegar todos os links de produtos por página. Foram 48 páginas encontradas e em média 16 livros por página. Os Links das páginas foram salvos em uma lista python.

Selenium - Pegar o página html.
Bs4 - Parse para identificar as tags link.


**Parte 2:**

Visitar cada link com selenium e pegar as informações alvo: 

* Título
* Autor
* Co-Autor se houver
* Ano
* tipo
* Número de páginas
* Editora
* Nota do  livro
* Total de avaliações (numero total de clientes que avaliaram o produto)


Selenium - Acessar links e pegar html.
Parsel - Parse para pegar cada informação alvo, lista acima.


**Parte 3:**

Pré-processamento dos dados em um arquivo csv com pandas para utilização e tratamento final em power bi.


Detalhes de código:

Gerenciador de contexto para o objeto webdriver.





## Uso/Exemplos
```
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
```


## Screenshots

<img src="/Livros_python_amazom_ptbr/img/print.png">

