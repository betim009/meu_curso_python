# Projeto Selenium Webscraping

Este projeto é um exemplo de automação e webscraping utilizando Selenium com Python.

## Estrutura do Projeto

```
11-selenium/
├── scraping/            # Scripts de scraping
│   └── exemplo_google.py
├── utils/               # Funções utilitárias
├── chromedriver-mac-arm64/ # ChromeDriver para Mac ARM64
├── venv/                # Ambiente virtual Python
├── requirements.txt     # Dependências do projeto
└── README.md            # Instruções do projeto
```

## Como usar

1. **Crie e ative o ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute o exemplo:**
   ```bash
   python3 scraping/exemplo_google.py
   ```

## Observações
- Certifique-se de que o ChromeDriver está compatível com a versão do seu navegador Chrome.
- O ChromeDriver já está incluso na pasta `chromedriver-mac-arm64/` para Mac ARM64.
- Para outros sistemas, baixe o ChromeDriver correspondente e ajuste o caminho no script.
