# Introdução ao Selenium

Selenium é uma biblioteca usada para controlar o navegador com Python.

Com ela, podemos automatizar tarefas como abrir uma página, clicar em botões, preencher campos e coletar informações públicas de sites.

---

## O que você vai aprender

- O que é automação de navegador.
- Como abrir uma página com Selenium.
- Como localizar elementos na tela.
- Como extrair textos.
- Quando usar Selenium.
- Quais cuidados tomar.

---

## Explicação simples

Imagine que você sempre faz a mesma tarefa em um site:

1. Abre o navegador.
2. Acessa uma página.
3. Digita uma busca.
4. Copia alguns resultados.

Selenium permite ensinar o Python a fazer parte desse trabalho.

---

## Instalação

Crie um ambiente virtual na sua máquina:

```bash
python -m venv venv
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Este repositório não guarda o ChromeDriver dentro da pasta do curso. Isso evita arquivos grandes e problemas de compatibilidade.

Em versões recentes do Selenium, o próprio Selenium Manager costuma resolver o driver automaticamente quando o navegador está instalado.

---

## Exemplo comentado

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print(driver.title)

driver.quit()
```

Explicando:

- `from selenium import webdriver` importa o recurso que controla o navegador.
- `webdriver.Chrome()` abre uma janela do Chrome.
- `driver.get(...)` acessa um site.
- `driver.title` pega o título da página.
- `driver.quit()` fecha o navegador.

---

## Quando usar Selenium?

Use Selenium quando:

- O site precisa de clique, rolagem ou preenchimento de formulário.
- Os dados aparecem apenas depois que a página carrega.
- Você precisa testar uma aplicação web.
- Você quer automatizar uma tarefa repetitiva no navegador.

Para páginas simples, muitas vezes `requests` e `BeautifulSoup` são mais leves.

---

## Cuidados importantes

- Respeite os termos de uso dos sites.
- Não faça muitas requisições em pouco tempo.
- Não colete dados privados.
- Prefira sites públicos e exemplos controlados para estudar.
- Sempre feche o navegador com `driver.quit()`.

---

## Erros comuns

### 1. Navegador incompatível

Se o Selenium não conseguir abrir o navegador, atualize o Chrome ou instale uma versão compatível.

### 2. Elemento não encontrado

Páginas mudam com frequência. Se um botão ou campo mudar de nome, o código pode parar.

### 3. Esquecer esperas

Às vezes a página demora para carregar. Nesses casos, pode ser necessário usar esperas explícitas.

### 4. Esquecer de fechar o navegador

Sempre finalize com:

```python
driver.quit()
```

---

## Exercícios sugeridos

1. Abra uma página e mostre o título no terminal.
2. Acesse um site de exemplo e colete o texto de um elemento.
3. Pesquise uma palavra em um campo de busca.
4. Salve os resultados encontrados em uma lista.
5. Grave os resultados em um arquivo CSV.

---

## Mini projeto

Crie uma automação simples que:

1. Abre uma página pública.
2. Coleta uma lista de títulos ou produtos.
3. Mostra os dados no terminal.
4. Salva os dados em um arquivo CSV.

---

## Resumo final

- Selenium controla o navegador.
- Ele é útil para sites dinâmicos.
- Deve ser usado com cuidado e responsabilidade.
- Para estudar, comece com páginas simples.
- Sempre feche o navegador no final.
