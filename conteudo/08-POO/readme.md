# Programação Orientada a Objetos

Esta pasta contém exemplos de programação orientada a objetos em Python.

Antes de estudar estes arquivos, faça primeiro o módulo [`07-classes`](../07-classes). Ele apresenta a base: classe, objeto, atributo, método e `__init__`.

Aqui os exemplos avançam para ideias como:

- Classes representando produtos.
- Métodos para calcular valores.
- Classes de estoque.
- Herança.
- Classes abstratas.

---

## Por que estudar POO?

POO significa **programação orientada a objetos**.

Esse jeito de programar ajuda a organizar sistemas maiores. Em vez de deixar todos os dados soltos, agrupamos informações e ações dentro de classes.

Exemplo:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_preco(self):
        return f"R$ {self.preco:.2f}"
```

Nesse caso:

- `Produto` é a classe.
- `nome` e `preco` são atributos.
- `mostrar_preco()` é um método.

---

## Ordem sugerida dos arquivos

Estude nesta ordem:

1. `app_1.py`: primeira classe `Produto`.
2. `app_2.py`: classe `Produto` junto com classe `Estoque`.
3. `app_3.py`: herança com tipos diferentes de produto.
4. `app_4.py`: classes abstratas com `ABC`.
5. `app_5.py`: espaço para continuação ou novo exemplo.

---

## Quando usar POO?

Use POO quando o programa tem entidades com dados e comportamentos.

Exemplos:

- Produto tem nome, preço e quantidade.
- Aluno tem nome, notas e média.
- Conta bancária tem titular, saldo, depósito e saque.
- Estoque tem produtos e ações de cadastro/listagem.

---

## Erros comuns

### 1. Usar POO cedo demais

Se o problema é pequeno, uma função pode ser suficiente.

Use classes quando elas deixarem o código mais organizado.

### 2. Criar classes sem comportamento

Se a classe só guarda dados e não tem nenhuma ação, pense se um dicionário resolveria melhor.

### 3. Misturar responsabilidades

Uma classe deve ter uma responsabilidade clara.

Exemplo:

- `Produto` cuida dos dados de um produto.
- `Estoque` cuida da lista de produtos.

---

## Mini projeto sugerido

Crie um sistema de estoque com:

- Classe `Produto`.
- Classe `Estoque`.
- Cadastro de produtos.
- Listagem de produtos.
- Cálculo do valor total em estoque.
- Busca por nome.

Depois, evolua o projeto criando tipos específicos:

- `Alimento`
- `Bebida`
- `Limpeza`

---

## Resumo final

- POO ajuda a organizar projetos maiores.
- Classes agrupam dados e comportamentos.
- Objetos são criados a partir de classes.
- Herança permite reaproveitar código.
- Classes abstratas ajudam a criar regras para classes filhas.
