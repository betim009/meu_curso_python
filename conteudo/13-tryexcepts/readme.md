
# Tratamento de Erros em Python

## 📌 O que é um bloco `try/except`?

Os blocos `try/except` são usados para **tratar erros (exceções)** que podem acontecer enquanto o programa está rodando. Eles evitam que o programa quebre com mensagens feias de erro, permitindo que você trate a situação de forma mais amigável ou segura.

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Você digitou algo que não é um número.")
```

---

## 🔁 Diferença entre `try/except`, `if/else` e `return`

### 1. `try/except` — Para tratar **erros inesperados**

```python
try:
    numero = int("abc")
except ValueError:
    print("Erro ao converter para inteiro!")
```

Neste caso, o Python tentou fazer algo que **gerou uma exceção** (`ValueError`) e o bloco `except` tratou isso.

---

### 2. `if/else` — Para tomar **decisões lógicas previsíveis**

```python
texto = "123"
if texto.isdigit():
    numero = int(texto)
else:
    print("Texto não é numérico!")
```

Aqui não tem erro, apenas uma **verificação lógica** antes de executar algo.

---

### 3. `return` — Para **encerrar uma função** e devolver um resultado

```python
def somar(a, b):
    return a + b
```

O `return` serve para devolver um valor, **não tem nada a ver com erro**.

---

## ⚠️ Muita gente confunde...

Muitos pensam que escrever:

```python
if b == 0:
    return "Erro: divisão por zero"
```

É tratamento de erro.  
Mas **isso é apenas uma forma de evitar** o erro, não é um tratamento real de exceção.

---

## ✅ Tratamento real de erro com `try/except`:

```python
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"
```

Aqui sim é tratamento!  
Você deixa o Python tentar e, **se der erro**, você captura e responde.

---

## 📊 Comparação rápida

| Situação                        | Exemplo                                | É tratamento de erro? |
|---------------------------------|-----------------------------------------|------------------------|
| Prevenir erro com `if`          | `if b == 0: return "Erro"`              | ❌ Não                 |
| Retornar `"Erro"` ou `False`   | `return "Erro"` ou `return False`       | ❌ Não                 |
| Usar `try/except`              | `try: ... except:`                      | ✅ Sim                 |

---

## ✅ Conclusão

- Use `if/else` para **prever e evitar** situações problemáticas.
- Use `try/except` para **tratar erros reais que podem acontecer** em tempo de execução.
- `return` é só uma forma de **sair de uma função** com um valor, **não tem relação com tratamento de erro**.

---



# Tipos de Erros (Exceções) em Python

Em Python, quando algo dá errado durante a execução do código, o interpretador lança um **erro**, também chamado de **exceção**. Podemos capturar esses erros usando `try/except`, mas é importante conhecer os **tipos de erros mais comuns** e quando cada um ocorre.

---

## 🔹 1. `ValueError`

Esse erro acontece quando você fornece um **valor inválido**, mesmo que o tipo esteja certo.

### Exemplo:

```python
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
```

🔍 **Por que deu erro?**  
Porque `"abc"` não pode ser convertido para número.

✅ **Quando usar `except ValueError`:**  
Quando você trabalha com **conversão de tipos**, como `int()`, `float()`, etc.

---

## 🔹 2. `ZeroDivisionError`

Erro quando o programa tenta **dividir por zero**, o que não é permitido matematicamente.

### Exemplo:

```python
10 / 0  # ZeroDivisionError: division by zero
```

✅ **Quando usar `except ZeroDivisionError`:**  
Sempre que fizer divisões onde o divisor **pode ser 0**.

---

## 🔹 3. `TypeError`

Erro quando você tenta fazer uma operação entre **tipos incompatíveis**.

### Exemplo:

```python
4 / "1"  # TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

🔍 **Por que deu erro?**  
Porque não dá pra dividir um número por uma string diretamente.

✅ **Quando usar `except TypeError`:**  
Quando seu código envolve tipos que **podem variar** (ex: entrada do usuário, leitura de arquivo).

---

## 🔹 4. `Exception` (erro genérico)

É a **classe base** para quase todos os erros. Usar `except Exception` pega praticamente tudo, com poucas exceções.

### Exemplo:

```python
try:
    resultado = 10 / 0
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

✅ **Quando usar `except Exception`:**  
Quando você quer **capturar qualquer erro** de forma geral, como em blocos críticos de código.

---

## ⚠️ Cuidado com o uso de `except:` sozinho

Evite usar apenas:

```python
except:
```

Isso captura **qualquer erro**, até os que não deveriam ser tratados (como `KeyboardInterrupt`, que ocorre quando o usuário aperta Ctrl+C). Sempre prefira:

```python
except Exception:
```

Ou ainda melhor: **trate erros específicos** sempre que possível.

---

## 📚 Resumo prático

| Tipo de erro         | O que significa                                       | Quando usar                      |
|----------------------|--------------------------------------------------------|----------------------------------|
| `ValueError`         | Valor inválido (mas tipo certo)                        | Conversão de tipos (`int()`)     |
| `ZeroDivisionError`  | Tentativa de divisão por zero                          | Divisões matemáticas             |
| `TypeError`          | Operações com tipos incompatíveis                      | Operações entre tipos diferentes |
| `Exception`          | Captura genérica de erros                              | Blocos críticos / debug geral    |

---

---

## 🔀 Múltiplos tratamentos de erro no mesmo `try`

É possível tratar **mais de um tipo de erro diferente** dentro de um único bloco `try`.  
Isso é útil quando várias exceções podem ocorrer no mesmo trecho de código.

### ✅ Exemplo:

```python
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: não pode dividir por zero"
    except TypeError:
        return "Erro: tipos incompatíveis (ex: número e texto)"
```

### Testes:

```python
print(dividir(10, 0))      # 👉 Erro de divisão por zero
print(dividir(10, "abc"))  # 👉 Erro de tipo (número e string)
```

### 📌 Observação:

A ordem dos blocos `except` importa!

Sempre coloque os **erros mais específicos primeiro**, e o `Exception` **por último**, se quiser capturar qualquer outro erro inesperado:

```python
try:
    ...
except ValueError:
    ...
except TypeError:
    ...
except Exception:
    ...
```

---




# Tipos de Erros (Exceções) em Python

Em Python, quando algo dá errado durante a execução do código, o interpretador lança um **erro**, também chamado de **exceção**. Podemos capturar esses erros usando `try/except`, mas é importante conhecer os **tipos de erros mais comuns** e quando cada um ocorre.

---

## 🔹 1. `ValueError`

Esse erro acontece quando você fornece um **valor inválido**, mesmo que o tipo esteja certo.

### Exemplo:

```python
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
```

🔍 **Por que deu erro?**  
Porque `"abc"` não pode ser convertido para número.

✅ **Quando usar `except ValueError`:**  
Quando você trabalha com **conversão de tipos**, como `int()`, `float()`, etc.

---

## 🔹 2. `ZeroDivisionError`

Erro quando o programa tenta **dividir por zero**, o que não é permitido matematicamente.

### Exemplo:

```python
10 / 0  # ZeroDivisionError: division by zero
```

✅ **Quando usar `except ZeroDivisionError`:**  
Sempre que fizer divisões onde o divisor **pode ser 0**.

---

## 🔹 3. `TypeError`

Erro quando você tenta fazer uma operação entre **tipos incompatíveis**.

### Exemplo:

```python
4 / "1"  # TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

🔍 **Por que deu erro?**  
Porque não dá pra dividir um número por uma string diretamente.

✅ **Quando usar `except TypeError`:**  
Quando seu código envolve tipos que **podem variar** (ex: entrada do usuário, leitura de arquivo).

---

## 🔹 4. `Exception` (erro genérico)

É a **classe base** para quase todos os erros. Usar `except Exception` pega praticamente tudo, com poucas exceções.

### Exemplo:

```python
try:
    resultado = 10 / 0
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

✅ **Quando usar `except Exception`:**  
Quando você quer **capturar qualquer erro** de forma geral, como em blocos críticos de código.

---

## ⚠️ Cuidado com o uso de `except:` sozinho

Evite usar apenas:

```python
except:
```

Isso captura **qualquer erro**, até os que não deveriam ser tratados (como `KeyboardInterrupt`, que ocorre quando o usuário aperta Ctrl+C). Sempre prefira:

```python
except Exception:
```

Ou ainda melhor: **trate erros específicos** sempre que possível.

---

## 📚 Resumo prático

| Tipo de erro         | O que significa                                       | Quando usar                      |
|----------------------|--------------------------------------------------------|----------------------------------|
| `ValueError`         | Valor inválido (mas tipo certo)                        | Conversão de tipos (`int()`)     |
| `ZeroDivisionError`  | Tentativa de divisão por zero                          | Divisões matemáticas             |
| `TypeError`          | Operações com tipos incompatíveis                      | Operações entre tipos diferentes |
| `Exception`          | Captura genérica de erros                              | Blocos críticos / debug geral    |

---

📁 Gerado como material didático para iniciantes  
🗓️ Data: 01/07/2025

---

## 🔀 Múltiplos tratamentos de erro no mesmo `try`

É possível tratar **mais de um tipo de erro diferente** dentro de um único bloco `try`.  
Isso é útil quando várias exceções podem ocorrer no mesmo trecho de código.

### ✅ Exemplo:

```python
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: não pode dividir por zero"
    except TypeError:
        return "Erro: tipos incompatíveis (ex: número e texto)"
```

### Testes:

```python
print(dividir(10, 0))      # 👉 Erro de divisão por zero
print(dividir(10, "abc"))  # 👉 Erro de tipo (número e string)
```

### 📌 Observação:

A ordem dos blocos `except` importa!

Sempre coloque os **erros mais específicos primeiro**, e o `Exception` **por último**, se quiser capturar qualquer outro erro inesperado:

```python
try:
    ...
except ValueError:
    ...
except TypeError:
    ...
except Exception:
    ...
```

---


---

## ❓ Quantos tipos de erro existem em Python?

Python possui **dezenas de tipos de exceções**, todas herdando da classe-base `BaseException`.

As mais comuns herdam de `Exception`, e são as que geralmente tratamos com `try/except`.

### 📚 Tabela com os principais erros:

| Tipo de erro         | Quando acontece                                         |
|----------------------|----------------------------------------------------------|
| `ValueError`         | Valor inválido para a operação                          |
| `TypeError`          | Tipos incompatíveis                                     |
| `ZeroDivisionError`  | Divisão por zero                                        |
| `IndexError`         | Índice fora do intervalo de uma lista                   |
| `KeyError`           | Chave não encontrada em um dicionário                   |
| `FileNotFoundError`  | Arquivo não encontrado ao tentar abrir                  |
| `PermissionError`    | Sem permissão para acessar um recurso                   |
| `AttributeError`     | Objeto não tem o atributo acessado                      |
| `NameError`          | Variável não definida                                   |
| `ImportError`        | Problema ao importar módulo                             |
| `RuntimeError`       | Erro genérico de execução                               |

---

## ⚡ Tratamento de Erros melhora a performance?

### ❌ Mito: `try/except` deixa a aplicação mais rápida

> Não! O tratamento de erros **não melhora a performance**.  
> Ele apenas deixa seu código **mais estável e seguro**.

### ✅ Verdade: Ele protege sua aplicação

- Impede que o programa quebre com erros feios
- Permite lidar com falhas de forma amigável
- Garante uma **boa experiência para o usuário**

---

### 🧠 Então por que não usar sempre?

Porque o `try/except` é mais **pesado** que um simples `if/else`.  
Se puder **prever o erro**, use `if`.  
Deixe `try/except` só para casos **imprevisíveis**.

### ❌ Ruim:
```python
try:
    numero = int("123")
except:
    numero = 0
```

### ✅ Melhor:
```python
if "123".isdigit():
    numero = int("123")
else:
    numero = 0
```

---

## 🧾 Conclusão

- Use `try/except` para tratar **erros reais e imprevisíveis**
- Use `if/else` para validar condições previsíveis
- Não confunda “tratar erro” com “retornar um erro como texto”
- Não espere ganho de performance — o foco aqui é **robustez**, não velocidade

---




# Tratamento de Erros em APIs Python (Flask)

Ao construir APIs com Flask, é essencial tratar erros corretamente para garantir segurança, clareza nas respostas e uma boa experiência para o consumidor da API.

---

## ✅ 1. Use `try/except` nos pontos críticos

Envolva blocos que podem falhar com `try/except`, especialmente quando trabalhar com:

- Entrada de dados do usuário
- Conexões com banco de dados
- Requisições externas (ex: APIs de terceiros)
- Conversões de dados

### Exemplo:

```python
@app.route("/usuario/<int:id>")
def get_usuario(id):
    try:
        usuario = buscar_usuario_por_id(id)
        return jsonify(usuario)
    except ValueError:
        return jsonify({"erro": "ID inválido"}), 400
    except Exception:
        return jsonify({"erro": "Erro interno no servidor"}), 500
```

---

## 📮 2. Use códigos de status HTTP corretos

| Código | Nome                        | Quando usar                                     |
|--------|-----------------------------|-------------------------------------------------|
| 200    | OK                          | Sucesso                                         |
| 201    | Created                     | Recurso criado com sucesso                      |
| 400    | Bad Request                 | Dados enviados estão incorretos                 |
| 401    | Unauthorized                | Falta autenticação                              |
| 403    | Forbidden                   | Acesso negado                                   |
| 404    | Not Found                   | Recurso não encontrado                          |
| 422    | Unprocessable Entity        | Dados com estrutura errada                      |
| 500    | Internal Server Error       | Erro inesperado do servidor                     |

---

## 📋 3. Padronize as respostas de erro

Enviar mensagens amigáveis e em formato padrão facilita o uso da API por outras aplicações:

```json
{
  "erro": "Usuário não encontrado",
  "codigo": 404
}
```

Evite enviar mensagens como `TypeError`, `Traceback`, ou qualquer erro cru do Python para o cliente.

---

## 🧱 4. Tratamento global de erros com Flask

Você pode usar um **handler global** para capturar qualquer erro não tratado:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(Exception)
def erro_geral(e):
    return jsonify({"erro": "Erro interno no servidor"}), 500
```

### Também pode capturar erros específicos:

```python
@app.errorhandler(404)
def nao_encontrado(e):
    return jsonify({"erro": "Rota não encontrada"}), 404
```

---

## 🧾 5. Registre erros com `logging`

Guardar os erros no servidor ajuda a identificar e corrigir falhas:

```python
import logging

logging.error("Erro ao acessar recurso", exc_info=True)
```

---

## ✅ Conclusão

| Boas práticas               | Por que usar?                                      |
|-----------------------------|----------------------------------------------------|
| `try/except`                | Evita falhas não tratadas                          |
| Códigos HTTP corretos       | Informam corretamente o tipo de erro               |
| Respostas padronizadas      | Melhoram a experiência do consumidor da API        |
| Handlers globais (`errorhandler`) | Centralizam o tratamento de exceções        |
| Registro com `logging`      | Facilita a manutenção e rastreio de erros          |

---

