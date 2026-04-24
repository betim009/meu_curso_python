# Roteiro de Estudo do `app.py`

## Visão geral
O arquivo `app.py` é o ponto de entrada da aplicação gráfica. Ele usa a biblioteca `customtkinter` para criar uma janela simples com um botão. Quando o botão é clicado, uma função de callback é executada e imprime uma mensagem no terminal.

A estrutura geral segue um padrão comum em Python:
1. Importa dependências.
2. Define funções auxiliares (como callback).
3. Define a função principal (`main`) que monta a interface.
4. Executa a aplicação somente quando o arquivo é chamado diretamente.

---

## Explicação detalhada por trecho

### 1) Importação
```python
import customtkinter
```

- `import`: palavra-chave do Python para carregar um módulo.
- `customtkinter`: biblioteca externa para interfaces gráficas, baseada em `tkinter`, com widgets modernos.
- Efeito prático: torna disponíveis classes como `customtkinter.CTk` e `customtkinter.CTkButton`.

---

### 2) Função de callback do botão
```python
def button_callback():
    print("button clicked")
```

#### O que é
Função chamada quando o usuário clica no botão.

#### Assinatura
- Nome: `button_callback`
- Parâmetros: nenhum
- Retorno: implícito `None`

#### Linha interna
- `print("button clicked")`
  - `print`: função nativa do Python para saída no terminal.
  - Parâmetro passado para `print`: string literal `"button clicked"`.
  - Efeito: registra o clique no console (não altera a interface visual).

#### Conceito importante
Essa função é usada como **callback** (função de retorno/chamada). Em GUI, callbacks são funções executadas em resposta a eventos (clique, teclado, mouse etc.).

---

### 3) Função principal de construção da interface
```python
def main():
    app = customtkinter.CTk()
    app.geometry("400x150")

    button = customtkinter.CTkButton(app, text="my button", command=button_callback)
    button.pack(padx=20, pady=20)

    return app
```

#### O que é
`main()` monta a janela e seus componentes, e devolve a instância da aplicação.

#### Assinatura
- Nome: `main`
- Parâmetros: nenhum
- Retorno: objeto `app` (instância de `customtkinter.CTk`)

#### Passo a passo

##### a) Criação da janela principal
```python
app = customtkinter.CTk()
```
- `CTk()`: classe principal de janela no `customtkinter`.
- Sem parâmetros neste caso.
- Resultado: objeto `app`, que representa a janela raiz da aplicação.

##### b) Definição do tamanho da janela
```python
app.geometry("400x150")
```
- `geometry(...)`: método para definir tamanho/posição da janela.
- Parâmetro usado: string `"400x150"`.
  - `400` = largura em pixels.
  - `150` = altura em pixels.
- Neste código, define apenas tamanho (sem posição explícita na tela).

##### c) Criação do botão
```python
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
```
- `CTkButton(...)`: classe de botão.
- Parâmetros usados:
  - `app` (primeiro argumento posicional): widget pai, ou seja, a janela onde o botão será inserido.
  - `text="my button"`: texto exibido no botão.
  - `command=button_callback`: função executada ao clicar no botão.

##### d) Posicionamento do botão
```python
button.pack(padx=20, pady=20)
```
- `pack(...)`: gerenciador de layout do Tkinter para posicionar widgets.
- Parâmetros usados:
  - `padx=20`: espaçamento horizontal externo de 20 pixels.
  - `pady=20`: espaçamento vertical externo de 20 pixels.
- Efeito: o botão é exibido com margem em relação às bordas da janela.

##### e) Retorno da janela
```python
return app
```
- Retorna a instância da aplicação para ser usada fora de `main()`.
- Isso separa a fase de “construção da UI” da fase de “execução do loop da UI”.

---

### 4) Ponto de entrada do programa
```python
if __name__ == "__main__":
    app = main()
    app.mainloop()
```

#### O que significa `if __name__ == "__main__":`
- `__name__` é uma variável especial do Python.
- Quando você roda `python app.py`, o valor dela é `"__main__"`.
- Quando o arquivo é importado por outro módulo, esse bloco não executa.

#### Linhas internas
- `app = main()`
  - Chama a função que monta a interface e recebe a janela pronta.
- `app.mainloop()`
  - Inicia o loop de eventos da GUI.
  - Mantém a janela aberta.
  - Escuta interações do usuário (cliques, teclado, redraw etc.).
  - Sem essa linha, a janela fecharia imediatamente.

---

## Resumo dos elementos técnicos

### Funções definidas no arquivo
1. `button_callback()`
   - Tipo: callback de evento.
   - Entrada: nenhuma.
   - Saída: `None`.
   - Efeito: imprime texto no terminal.

2. `main()`
   - Tipo: função de inicialização da UI.
   - Entrada: nenhuma.
   - Saída: objeto `CTk`.
   - Efeito: cria janela, botão, layout e retorna app.

### Métodos usados de objetos
1. `app.geometry("400x150")`
   - Configura o tamanho da janela.

2. `button.pack(padx=20, pady=20)`
   - Posiciona o botão na janela com margens.

3. `app.mainloop()`
   - Inicia o loop principal da interface gráfica.

### Parâmetros e argumentos relevantes
- `text="my button"`: rótulo visual do botão.
- `command=button_callback`: função associada ao evento de clique.
- `padx=20`, `pady=20`: espaçamento horizontal/vertical externo.
- `"400x150"`: dimensão da janela em pixels.

---

## Fluxo de execução completo
1. Python carrega `customtkinter`.
2. Define as funções `button_callback` e `main`.
3. Entra no bloco `if __name__ == "__main__":` (se rodar diretamente).
4. Executa `main()`, criando a janela e o botão.
5. Executa `mainloop()`, aguardando eventos.
6. Quando o botão é clicado, `button_callback()` roda e imprime `button clicked`.

---

## Observações de aprendizado
- O código está correto para uma primeira interface gráfica.
- A separação em `main()` facilita manutenção e testes.
- O próximo passo natural seria adicionar mais widgets (label, entry) e mover de `print` para atualização visual na própria janela.
