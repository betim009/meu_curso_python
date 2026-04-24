# Roteiro de Estudo do `app2.py`

## Visão geral
O `app2.py` demonstra uso de layout com `grid` no `customtkinter`. A janela é dividida em linhas e colunas, e cada `Label` é posicionado por coordenadas (`row`, `column`).

Objetivo principal do arquivo:
- mostrar como configurar pesos de expansão do grid;
- distribuir widgets em células específicas;
- comparar uma linha com 2 colunas e outra com 3 colunas.

---

## Código-base
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x300")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

ctk.CTkLabel(app, text="Coluna 1 da Linha 1").grid(row=0, column=0)
ctk.CTkLabel(app, text="Coluna 2 da Linha 1").grid(row=0, column=1)

ctk.CTkLabel(app, text="Coluna 1 da Linha 2").grid(row=1, column=0)
ctk.CTkLabel(app, text="Coluna 2 da Linha 2").grid(row=1, column=1)
ctk.CTkLabel(app, text="Coluna 3 da Linha 2").grid(row=1, column=2)

app.mainloop()
```

---

## Explicação detalhada por trecho

### 1) Importação
```python
import customtkinter as ctk
```
- Importa a biblioteca de interface gráfica.
- `as ctk` cria um alias curto para facilitar leitura.

---

### 2) Criação da janela principal
```python
app = ctk.CTk()
app.geometry("500x300")
```
- `CTk()` cria a janela raiz.
- `geometry("500x300")` define largura e altura em pixels.

Parâmetro de `geometry`:
- formato `"larguraxaltura"`.

---

### 3) Configuração de colunas do grid
```python
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
```
- Método `grid_columnconfigure(indice, weight=...)` configura comportamento da coluna.
- `indice` = coluna afetada.
- `weight=1` = coluna pode expandir quando a janela cresce.

Como todas as três colunas têm `weight=1`, o espaço extra é dividido de forma equilibrada.

---

### 4) Configuração de linhas do grid
```python
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
```
- Método `grid_rowconfigure(indice, weight=...)` para linhas.
- Ambas as linhas possuem peso igual, então também compartilham expansão vertical.

---

### 5) Widgets na linha 0
```python
ctk.CTkLabel(app, text="Coluna 1 da Linha 1").grid(row=0, column=0)
ctk.CTkLabel(app, text="Coluna 2 da Linha 1").grid(row=0, column=1)
```

Cada linha combina criação + posicionamento em uma única expressão:
- `CTkLabel(app, text=...)` cria um rótulo.
- `.grid(row=0, column=...)` posiciona no grid.

Parâmetros usados:
- `row`: índice da linha.
- `column`: índice da coluna.
- `text`: conteúdo exibido no label.

Observação:
- Na linha 0, a coluna 2 fica vazia (não há widget nela).

---

### 6) Widgets na linha 1
```python
ctk.CTkLabel(app, text="Coluna 1 da Linha 2").grid(row=1, column=0)
ctk.CTkLabel(app, text="Coluna 2 da Linha 2").grid(row=1, column=1)
ctk.CTkLabel(app, text="Coluna 3 da Linha 2").grid(row=1, column=2)
```

- Aqui as 3 colunas são usadas na mesma linha (`row=1`).
- O exemplo evidencia que cada linha pode ter número diferente de widgets ocupando colunas diferentes.

---

### 7) Loop principal
```python
app.mainloop()
```
- Inicia o loop de eventos da interface.
- Mantém a janela aberta e processa interações.

Sem essa linha, a janela fecha imediatamente após abrir.

---

## Parâmetros e métodos essenciais

### Métodos da janela (`app`)
1. `geometry("500x300")`
- Define tamanho inicial da janela.

2. `grid_columnconfigure(coluna, weight=1)`
- Configura distribuição horizontal do grid.

3. `grid_rowconfigure(linha, weight=1)`
- Configura distribuição vertical do grid.

4. `mainloop()`
- Inicia ciclo de eventos da GUI.

### Métodos de widget
1. `CTkLabel(app, text="...")`
- Cria rótulo no widget pai `app`.

2. `.grid(row=?, column=?)`
- Posiciona widget na célula indicada.

---

## Fluxo de execução
1. Biblioteca `customtkinter` é importada.
2. Janela principal é criada.
3. Tamanho da janela é definido.
4. Grid é configurado com 3 colunas e 2 linhas expansíveis.
5. Labels da linha 0 são criados nas colunas 0 e 1.
6. Labels da linha 1 são criados nas colunas 0, 1 e 2.
7. `mainloop()` inicia a execução da interface.

---

## Observações de aprendizado
- `grid` é ideal quando você pensa a interface como tabela (linhas/colunas).
- `weight` é fundamental para layouts responsivos ao redimensionamento.
- Você não deve misturar `pack` e `grid` no mesmo container (`app`) ao mesmo tempo; aqui o código está correto por usar apenas `grid` no container raiz.
