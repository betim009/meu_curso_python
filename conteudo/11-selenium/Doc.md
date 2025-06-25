# Guia Didático: Selenium com Python

Este documento tem como objetivo ensinar, de forma prática e objetiva, conceitos e exemplos de uso da biblioteca Selenium para automação de browsers e webscraping.

---

## Índice
1. O que é Selenium?
2. Instalação
3. Configuração do ChromeDriver
4. Abrindo um navegador
5. Navegando para uma página
6. Encontrando elementos
7. Interagindo com elementos (inputs, botões)
8. Extraindo informações (textos, atributos)
9. Esperas (waits)
10. Fechando o navegador
11. Dicas e boas práticas

---

## 1. O que é Selenium?
Selenium é uma biblioteca que permite automatizar a interação com navegadores web, sendo muito utilizada para testes automatizados e webscraping.

## 2. Instalação
No terminal, com o ambiente virtual ativado:
```bash
pip install selenium
```

## 3. Configuração do ChromeDriver
Baixe o ChromeDriver compatível com seu navegador e sistema operacional. No projeto, já existe um para Mac ARM64.

## 4. Abrindo um navegador
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver-mac-arm64/chromedriver')
browser = webdriver.Chrome(service=service)
```

## 5. Navegando para uma página
```python
browser.get('https://www.google.com')
```

## 6. Encontrando elementos
```python
# Por nome
search_box = browser.find_element('name', 'q')
# Por id
# element = browser.find_element('id', 'meu_id')
# Por classe
# element = browser.find_element('class name', 'minha_classe')
```

## 7. Interagindo com elementos
```python
search_box.send_keys('Python Selenium')
search_box.submit()
```

## 8. Extraindo informações
```python
titulo = browser.title
print(titulo)

# Extrair texto de um elemento
texto = search_box.text
```

## 9. Esperas (waits)
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Espera até que o elemento esteja presente
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)
```

## 10. Fechando o navegador
```python
browser.quit()
```

## 11. Dicas e boas práticas
- Sempre feche o navegador ao final.
- Use esperas explícitas para páginas dinâmicas.
- Mantenha o ChromeDriver atualizado.
- Consulte a [documentação oficial do Selenium](https://selenium-python.readthedocs.io/). 