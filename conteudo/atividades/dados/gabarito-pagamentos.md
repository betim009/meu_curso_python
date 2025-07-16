# ✅ Gabarito Comentado — Exercícios Pagamentos de Salários

---

## 📗 Bloco 1 — Acesso direto e modificação

1. Acesse e imprima o nome do primeiro funcionário na lista `funcionarios`.
```python
print(funcionarios[0]["nome"])  # Ana
```

2. Imprima o salário do terceiro item da lista `pagamentos`, formatando a saída.
```python
print(f"Salário: R$ {pagamentos['salarios'][2]:.2f}")  # Salário: R$ 3900.00
```

3. Altere o tempo de empresa do funcionário 'Bruno'.
```python
funcionarios[1]["tempo_empresa"] = 6
```

4. Mude o departamento do funcionário 'Elisa' na estrutura `pagamentos`.
```python
indice = pagamentos["nomes"].index("Elisa")
pagamentos["departamentos"][indice] = "Diretoria"
```

5. Acesse nome e departamento do funcionário na posição 2.
```python
print(f"Funcionário: {pagamentos['nomes'][2]} | Departamento: {pagamentos['departamentos'][2]}")
# Funcionário: Carla | Departamento: Financeiro
```

---

## 🔄 Bloco 2 — Uso de `for item in ...`

6. Imprima o nome de cada funcionário em `funcionarios`.
```python
for item in funcionarios:
    print(item["nome"])
```

7. Mostre todos os departamentos da estrutura `pagamentos`.
```python
for dept in pagamentos["departamentos"]:
    print(dept)
```

8. Liste todos os salários da lista `funcionarios`.
```python
for item in funcionarios:
    print(item["salario"])
```

9. Nome e tempo de empresa separados por hífen.
```python
for item in funcionarios:
    print(f"{item['nome']} - {item['tempo_empresa']}")
```

10. Funcionários com índice na estrutura `pagamentos`.
```python
for i in range(len(pagamentos["nomes"])):
    print(f"{i} - {pagamentos['nomes'][i]}")
```

11. Salários com aumento de 10%.
```python
for salario in pagamentos["salarios"]:
    print(salario * 1.1)
```

12. Nomes em letras maiúsculas.
```python
for item in funcionarios:
    print(item["nome"].upper())
```

13. Nome e salário separados por dois pontos.
```python
for i in range(len(pagamentos["nomes"])):
    print(f"{pagamentos['nomes'][i]}: {pagamentos['salarios'][i]}")
```

---

## 🔍 Bloco 3 — Uso de `for` com `if`

14. Funcionários com salário maior que 4000.
```python
for item in funcionarios:
    if item["salario"] > 4000:
        print(item["nome"])
```

15. Funcionários com mais de 3 anos de empresa.
```python
for i in range(len(pagamentos["tempo_empresa"])):
    if pagamentos["tempo_empresa"][i] > 3:
        print(pagamentos["nomes"][i])
```

16. Funcionários do departamento 'TI'.
```python
for item in funcionarios:
    if item["departamento"] == "TI":
        print(item["nome"])
```

17. Funcionários com salário abaixo de 3000.
```python
for i in range(len(pagamentos["salarios"])):
    if pagamentos["salarios"][i] < 3000:
        print(pagamentos["nomes"][i])
```

18. Funcionários cujo nome começa com 'C'.
```python
for item in funcionarios:
    if item["nome"].startswith("C"):
        print(item["nome"])
```

19. Funcionários do departamento 'Financeiro' ou 'RH'.
```python
for i in range(len(pagamentos["departamentos"])):
    if pagamentos["departamentos"][i] in ["Financeiro", "RH"]:
        print(pagamentos["nomes"][i])
```

20. Funcionários com tempo de empresa >= 5 anos.
```python
for item in funcionarios:
    if item["tempo_empresa"] >= 5:
        print(item["nome"])
```

---

**Observação:** Existem várias formas corretas de resolver cada exercício. O importante é praticar a lógica e o uso de laços e condições! 