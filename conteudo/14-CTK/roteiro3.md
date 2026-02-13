# Roteiro de Estudo do `app3.py`

## Visão geral
O `app3.py` mostra uma interface organizada em blocos usando `Frame` + `grid` no container principal e `pack` dentro de cada frame. A tela possui:
- coluna esquerda: formulário;
- coluna direita: área de resultado;
- linha inferior: rodapé ocupando toda a largura.

Esse arquivo é um ótimo exemplo de layout híbrido bem estruturado:
- `grid` para macroestrutura;
- `pack` para organização interna de cada bloco.

---

## Código-base
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("700x400")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=0)

frame_form = ctk.CTkFrame(app)
frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame_resultado = ctk.CTkFrame(app)
frame_resultado.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

frame_footer = ctk.CTkFrame(app)
frame_footer.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

app.mainloop()
```

---

## Explicação detalhada por trecho

### 1) Importação e janela
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("700x400")
```
- Importa biblioteca com alias `ctk`.
- Cria janela principal.
- Define tamanho inicial de 700x400 px.

---

### 2) Grid principal (container raiz)
```python
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=0)
```

#### Colunas
- Coluna 0 (`weight=1`) e coluna 1 (`weight=1`) crescem de forma equilibrada na horizontal.

#### Linhas
- Linha 0 (`weight=1`) cresce e ocupa a maior parte da altura.
- Linha 1 (`weight=0`) não recebe expansão extra, mantendo altura mínima (ideal para rodapé).

---

### 3) Frame 1: formulário (lado esquerdo)
```python
frame_form = ctk.CTkFrame(app)
frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
```

#### Criação
- `CTkFrame(app)` cria um container visual dentro da janela principal.

#### Posicionamento (`grid`)
Parâmetros usados:
- `row=0`, `column=0`: canto superior esquerdo da macroestrutura.
- `padx=10`, `pady=10`: espaçamento externo.
- `sticky="nsew"`: estica o frame em todas as direções da célula.
  - `n`: norte (topo)
  - `s`: sul (base)
  - `e`: leste (direita)
  - `w`: oeste (esquerda)

#### Widgets internos
```python
label = ctk.CTkLabel(frame_form, text="Digite algo:")
label.pack(pady=10)

entry = ctk.CTkEntry(frame_form)
entry.pack(pady=10)

button = ctk.CTkButton(frame_form, text="Buscar")
button.pack(pady=10)
```

- Todos têm `frame_form` como pai.
- Layout interno usa `pack`, com espaçamento vertical.
- O botão ainda não possui `command`, então não executa ação ao clicar.

---

### 4) Frame 2: resultado (lado direito)
```python
frame_resultado = ctk.CTkFrame(app)
frame_resultado.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
```

- Ocupa a célula superior direita (`row=0`, `column=1`).
- Mesmo padrão de preenchimento e margens do frame esquerdo.

#### Widgets internos
```python
titulo = ctk.CTkLabel(
    frame_resultado,
    text="Resultado da sua busca",
    font=("Arial", 18)
)
titulo.pack(pady=10)
```

Parâmetros relevantes:
- `text`: conteúdo do título.
- `font=("Arial", 18)`: fonte e tamanho.

```python
paragrafo = ctk.CTkLabel(
    frame_resultado,
    text="Aqui aparecerá o resultado da sua busca.\nExemplo de texto qualquer.",
    wraplength=250,
    justify="left"
)
paragrafo.pack(pady=10)
```

Parâmetros relevantes:
- `wraplength=250`: quebra linha automática em ~250 px.
- `justify="left"`: alinha múltiplas linhas à esquerda.

---

### 5) Frame 3: rodapé (linha inferior)
```python
frame_footer = ctk.CTkFrame(app)
frame_footer.grid(
    row=1,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=10,
    pady=10
)
```

Parâmetros de destaque:
- `row=1`: segunda linha do grid principal.
- `column=0`: começa na primeira coluna.
- `columnspan=2`: ocupa as duas colunas do layout.
- `sticky="ew"`: estica apenas horizontalmente.

Widget interno:
```python
rodape = ctk.CTkLabel(frame_footer, text="2026")
rodape.pack(pady=5)
```

---

### 6) Loop principal
```python
app.mainloop()
```
- Inicia ciclo de eventos da interface.
- Mantém a aplicação aberta.

---

## Organização do layout (mapa mental)
- Linha `0`, Coluna `0`: `frame_form`
- Linha `0`, Coluna `1`: `frame_resultado`
- Linha `1`, Colunas `0-1`: `frame_footer` (`columnspan=2`)

Representação:
```text
+-------------------+-------------------+
|   Frame Form      |  Frame Resultado  |
| (label/entry/bt)  | (titulo/paragrafo)|
+---------------------------------------+
|              Frame Footer             |
+---------------------------------------+
```

---

## Métodos e parâmetros-chave
1. `grid_columnconfigure(indice, weight=...)`
- Controla expansão horizontal por coluna.

2. `grid_rowconfigure(indice, weight=...)`
- Controla expansão vertical por linha.

3. `widget.grid(...)`
- Posiciona no grid do container pai.

4. `widget.pack(...)`
- Organiza internamente widgets dentro de um frame.

5. `columnspan=N`
- Faz widget ocupar múltiplas colunas.

6. `sticky="..."`
- Define direções de esticamento/alinhamento.

7. `wraplength` e `justify`
- Controlam quebra e alinhamento de texto multilinha.

---

## Fluxo de execução
1. Janela principal é criada.
2. Grid principal é configurado com 2 colunas e 2 linhas.
3. `frame_form` é criado na esquerda.
4. `frame_resultado` é criado na direita.
5. `frame_footer` é criado na linha inferior ocupando largura total.
6. Widgets internos são adicionados com `pack` em cada frame.
7. `mainloop()` inicia a aplicação.

---

## Melhorias naturais para esse app
1. Adicionar `command` no botão `Buscar` para ler `entry` e atualizar `paragrafo`.
2. Substituir fonte fixa (`Arial`) por estilo consistente do `customtkinter`.
3. Definir `app.title(...)` para melhorar identificação da janela.
4. Extrair construção de cada frame para funções, facilitando manutenção.
