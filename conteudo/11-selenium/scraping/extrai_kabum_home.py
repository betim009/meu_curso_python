from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def extrair_produtos_kabum_home(chrome_driver_path):
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.kabum.com.br/")
    time.sleep(3)  # Aguarda o carregamento inicial

    # Rola a página várias vezes para carregar mais produtos
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(5):  # Ajuste o range conforme necessário
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Espera explicitamente até que vários produtos estejam presentes
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.productCard"))
    )

    produtos = []
    artigos = driver.find_elements(By.CSS_SELECTOR, "article.productCard")
    for artigo in artigos:
        # Nome do produto
        try:
            nome = artigo.find_element(By.CSS_SELECTOR, "span.nameCard").text.strip()
        except Exception:
            nome = "N/A"
        # Preço do produto
        try:
            preco = artigo.find_element(By.XPATH, ".//span[contains(text(),'R$')]").text.strip()
        except Exception:
            preco = "N/A"
        produtos.append({"nome": nome, "preco": preco})

    driver.quit()
    return produtos

if __name__ == "__main__":
    chrome_driver_path = "chromedriver-mac-arm64/chromedriver"
    lista = extrair_produtos_kabum_home(chrome_driver_path)
    for produto in lista:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']}")
        print("-" * 40)
    print(f"Total de produtos encontrados: {len(lista)}") 