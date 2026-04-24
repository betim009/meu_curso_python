# Roteiro de Estudo do `app1.py`

## Visão geral
O arquivo `app1.py` cria uma interface gráfica mais completa com `customtkinter` (apelidado como `ctk`). Ele demonstra vários widgets comuns em aplicações desktop:
- `Label`
- `Entry`
- `Textbox`
- `OptionMenu`
- `Switch`
- `Slider`
- `Button`

Além de criar os componentes, o código também mostra como ligar eventos de interação (callbacks) para reagir a cliques, seleção de opções e movimento do slider.

---

## Estrutura geral do arquivo
1. Importa a biblioteca como alias `ctk`.
2. Define a função principal `main()`.
3. Configura aparência e janela principal.
4. Cria widgets em sequência e liga callbacks.
5. Inicia o loop da interface com `mainloop()`.
6. Executa `main()` apenas quando o arquivo é rodado diretamente.

---

## Explicação detalhada por trecho

### 1) Importação com alias
```python
import customtkinter as ctk
```

- `import`: carrega um módulo no Python.
- `customtkinter`: biblioteca de UI.
- `as ctk`: cria um apelido para reduzir verbosidade.

Benefício prático: em vez de escrever `customtkinter.CTkButton`, você escreve `ctk.CTkButton`.

---

### 2) Função principal
```python
def main():
```

- Ponto central de montagem da interface.
- Não recebe parâmetros.
- Não tem `return` explícito (retorna `None`).
- Dentro dela, toda a UI é criada e executada.

---

### 3) Aparência global
```python
ctk.set_appearance_mode("dark")
```

- Função global do `customtkinter`.
- Parâmetro: `"dark"`.
- Efeito: tema escuro para widgets e janela.

Modos comuns: `"light"`, `"dark"`, `"system"`.

---

### 4) Janela principal
```python
app = ctk.CTk()
app.title("Widgets CTk")
app.geometry("800x800")
```

#### `app = ctk.CTk()`
- Cria a janela raiz da aplicação.

#### `app.title("Widgets CTk")`
- Método que define o título da janela.
- Parâmetro: string exibida na barra superior.

#### `app.geometry("800x800")`
- Método que define tamanho da janela.
- Parâmetro: `"larguraxaltura"` em pixels.
- Aqui: 800 px de largura e 800 px de altura.

---

### 5) Label
```python
label = ctk.CTkLabel(app, text="Digite seu nome:")
label.pack(pady=10)
```

#### Criação
- Classe: `CTkLabel`.
- Parâmetros:
  - `app`: widget pai (janela).
  - `text="Digite seu nome:"`: texto visível.

#### Layout
- `pack(pady=10)`: posiciona o widget com espaçamento vertical externo de 10 px.

---

### 6) Campo de entrada (`Entry`)
```python
entry = ctk.CTkEntry(app, placeholder_text="Seu nome")
entry.pack(pady=10)
```

#### Criação
- Classe: `CTkEntry`.
- Parâmetros:
  - `app`: pai.
  - `placeholder_text="Seu nome"`: texto de dica antes da digitação.

#### Layout
- `pack(pady=10)`: margem vertical.

Uso futuro no código:
- `entry.get()` para ler o texto.
- `entry.delete(0, "end")` para limpar o campo.

---

### 7) Área de texto (`Textbox`)
```python
textbox = ctk.CTkTextbox(app, height=100)
textbox.pack(pady=10)
```

#### Criação
- Classe: `CTkTextbox`.
- Parâmetros:
  - `app`: pai.
  - `height=100`: altura da caixa em pixels (largura usa valor padrão).

#### Layout
- `pack(pady=10)`.

Uso futuro no código:
- `textbox.insert("end", ...)` para adicionar texto no final.

---

### 8) Menu de opções (`OptionMenu`) + callback
```python
def opcao_escolhida(valor):
    print(f"Opção: {valor}\n")
```

#### Função `opcao_escolhida`
- Callback executada quando a seleção muda.
- Parâmetro:
  - `valor`: string da opção escolhida.
- Efeito: imprime a opção no terminal.

```python
option_menu = ctk.CTkOptionMenu(
    app,
    values=["Aluno", "Professor", "Administrador"],
    command=opcao_escolhida
)
option_menu.pack(pady=10)
```

#### Criação do `OptionMenu`
- Classe: `CTkOptionMenu`.
- Parâmetros:
  - `app`: pai.
  - `values=[...]`: lista de opções disponíveis.
  - `command=opcao_escolhida`: callback chamada quando o valor muda.

#### Layout
- `pack(pady=10)`.

---

### 9) Switch + callback
```python
def switch_event():
    estado = switch.get()
    print(f"Switch: {estado}\n")
```

#### Função `switch_event`
- Callback executada quando o switch é alternado.
- Sem parâmetros.
- Lê estado com `switch.get()`.

`switch.get()` normalmente retorna:
- `1` (ligado)
- `0` (desligado)

```python
switch = ctk.CTkSwitch(
    app,
    text="Modo Ativo",
    command=switch_event
)
switch.pack(pady=10)
```

#### Criação do `Switch`
- Classe: `CTkSwitch`.
- Parâmetros:
  - `app`: pai.
  - `text="Modo Ativo"`: texto ao lado do switch.
  - `command=switch_event`: callback no toggle.

#### Layout
- `pack(pady=10)`.

---

### 10) Slider + callback + label de feedback
```python
def slider_event(valor):
    label_slider.configure(text=f"Volume: {int(valor)}")
```

#### Função `slider_event`
- Callback acionada ao mover o slider.
- Parâmetro:
  - `valor`: número (float) da posição atual.
- Efeito:
  - Converte para inteiro: `int(valor)`.
  - Atualiza texto do label com `label_slider.configure(...)`.

```python
slider = ctk.CTkSlider(
    app,
    from_=0,
    to=100,
    command=slider_event
)
slider.pack(pady=10)
```

#### Criação do `Slider`
- Classe: `CTkSlider`.
- Parâmetros:
  - `app`: pai.
  - `from_=0`: valor mínimo.
  - `to=100`: valor máximo.
  - `command=slider_event`: callback no movimento.

Observação:
- O nome `from_` termina com `_` porque `from` é palavra reservada do Python.

```python
label_slider = ctk.CTkLabel(app, text="Volume: 0")
label_slider.pack()
```

#### Label de apoio
- Mostra visualmente o valor atual do slider.
- Inicializa em `Volume: 0`.

---

### 11) Botão "Enviar" + callback
```python
def enviar():
    nome = entry.get()
    textbox.insert("end", f"Nome digitado: {nome}\n")
    entry.delete(0, "end")
```

#### Função `enviar`
- Callback do botão.
- Sem parâmetros.
- Passo a passo:
  1. `entry.get()`: captura texto digitado.
  2. `textbox.insert("end", ...)`: adiciona texto no final da caixa de texto.
  3. `entry.delete(0, "end")`: limpa o campo de entrada.

Parâmetros importantes:
- `"end"`: índice especial do Tkinter para final do conteúdo.
- `0`: início do texto no `Entry`.

```python
button = ctk.CTkButton(app, text="Enviar", command=enviar)
button.pack(pady=20)
```

#### Criação do botão
- Classe: `CTkButton`.
- Parâmetros:
  - `app`: pai.
  - `text="Enviar"`: rótulo do botão.
  - `command=enviar`: callback de clique.

#### Layout
- `pack(pady=20)` com margem vertical maior.

---

### 12) Loop de eventos
```python
app.mainloop()
```

- Inicia o loop principal da GUI.
- Mantém a janela aberta.
- Processa interações em tempo real.

Sem essa linha, a aplicação abriria e fecharia imediatamente.

---

### 13) Ponto de entrada do script
```python
if __name__ == "__main__":
    main()
```

- Garante execução de `main()` apenas quando `app1.py` é rodado diretamente.
- Se importado em outro arquivo, não abre a janela automaticamente.

---

## Resumo das funções do arquivo
1. `main()`
- Monta e executa toda a interface.

2. `opcao_escolhida(valor)`
- Callback do `OptionMenu`.
- Recebe a opção selecionada.

3. `switch_event()`
- Callback do `Switch`.
- Lê estado com `switch.get()`.

4. `slider_event(valor)`
- Callback do `Slider`.
- Atualiza `label_slider` com o valor atual.

5. `enviar()`
- Callback do botão.
- Lê `Entry`, escreve no `Textbox` e limpa o campo.

---

## Resumo dos principais parâmetros usados
- `text`: texto exibido em label/switch/button.
- `placeholder_text`: dica em campo de entrada.
- `height`: altura do textbox.
- `values`: opções do option menu.
- `command`: função chamada quando ocorre evento.
- `from_` e `to`: intervalo mínimo/máximo do slider.
- `pady`: margem vertical ao usar `pack`.

---

## Fluxo de execução completo
1. Python importa `customtkinter` como `ctk`.
2. `main()` é chamada no bloco principal.
3. Tema escuro é aplicado.
4. Janela é criada e configurada (`title`, `geometry`).
5. Widgets são criados e empacotados (`pack`).
6. Callbacks ficam registrados em `command`.
7. `mainloop()` entra no ciclo de eventos.
8. Interações do usuário disparam callbacks:
- troca de opção chama `opcao_escolhida`;
- toggle chama `switch_event`;
- movimento do slider chama `slider_event`;
- clique no botão chama `enviar`.

---

## Observações técnicas importantes
- Callbacks definidos dentro de `main()` conseguem acessar variáveis locais (`entry`, `textbox`, `switch`, `label_slider`) por fechamento (closure), o que é intencional nesse estilo.
- A ordem de criação importa: por exemplo, `switch_event` só funciona corretamente quando `switch` já existe no momento do clique.
- O projeto já cobre um bom conjunto de widgets básicos para treinamento de interface com `customtkinter`.
