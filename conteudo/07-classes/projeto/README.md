# Projeto - Sistema de cadastro orientado a objetos

## Objetivo

Criar um sistema simples de cadastro de clientes usando classes.

Este projeto simula uma parte comum de sistemas de empresas: cadastrar clientes, validar informações, listar registros e localizar um cliente pelo e-mail.

O foco não é criar uma tela bonita nem salvar em banco de dados. O foco é entender como classes ajudam a organizar dados e comportamentos.

## O que você vai praticar

- Criar classes com `class`.
- Usar `__init__` para iniciar atributos.
- Criar métodos para validação.
- Criar métodos para exibição de dados.
- Usar uma classe para representar uma entidade real.
- Usar outra classe para gerenciar uma lista de objetos.

## Visão do sistema

O sistema terá duas classes principais:

```text
Cliente
  - representa um cliente da empresa
  - guarda nome, idade, email e status
  - valida dados do próprio cliente
  - exibe os próprios dados

SistemaCadastro
  - gerencia vários clientes
  - cadastra clientes
  - lista clientes
  - busca cliente por email
  - desativa cliente
```

## Passo 1 - Criar a classe Cliente

Começamos pela entidade principal do sistema.

Um cliente precisa ter:

- `nome`
- `idade`
- `email`
- `ativo`

```python
class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.ativo = True
```

O atributo `ativo` começa como `True` porque um cliente recém-cadastrado normalmente entra ativo no sistema.

## Passo 2 - Criar métodos de validação

Antes de cadastrar um cliente, o sistema precisa verificar se os dados fazem sentido.

```python
def email_valido(self):
    return "@" in self.email and "." in self.email


def idade_valida(self):
    return self.idade >= 18
```

Esses métodos ficam dentro de `Cliente` porque são regras relacionadas ao próprio cliente.

## Passo 3 - Criar método para exibir dados

```python
def exibir_dados(self):
    status = "ativo" if self.ativo else "inativo"
    return f"{self.nome} | {self.idade} anos | {self.email} | {status}"
```

Esse método evita repetir a mesma formatação em várias partes do código.

## Passo 4 - Criar a classe SistemaCadastro

Agora criamos uma classe para controlar a lista de clientes.

```python
class SistemaCadastro:
    def __init__(self):
        self.clientes = []
```

Ela começa com uma lista vazia porque, ao iniciar o sistema, nenhum cliente foi cadastrado ainda.

## Passo 5 - Cadastrar clientes

```python
def cadastrar_cliente(self, cliente):
    if not cliente.email_valido():
        print(f"Erro: e-mail inválido para {cliente.nome}.")
        return

    if not cliente.idade_valida():
        print(f"Erro: {cliente.nome} precisa ser maior de idade.")
        return

    self.clientes.append(cliente)
    print(f"Cliente cadastrado com sucesso: {cliente.nome}")
```

Repare no fluxo:

1. Valida o e-mail.
2. Valida a idade.
3. Se estiver tudo certo, adiciona na lista.

## Passo 6 - Listar, buscar e desativar

Um sistema real precisa permitir operações básicas sobre os cadastros.

- Listar todos os clientes.
- Buscar cliente por e-mail.
- Desativar um cliente sem apagar o registro.

Desativar é mais realista do que apagar, porque empresas geralmente precisam manter histórico.

## Código completo

O código completo está em [`sistema_cadastro.py`](sistema_cadastro.py).

## Como executar

Abra o terminal na pasta do curso e execute:

```bash
python conteudo/07-classes/projeto/sistema_cadastro.py
```

## Decisões tomadas

### Por que existe uma classe `Cliente`?

Porque cliente é uma entidade real do sistema. Ele tem dados próprios e regras próprias.

### Por que existe uma classe `SistemaCadastro`?

Porque a lista de clientes e as operações de cadastro pertencem ao sistema, não a um cliente individual.

Um cliente sabe validar os próprios dados. O sistema sabe gerenciar vários clientes.

### Por que validar dentro da classe?

Porque a regra fica perto dos dados que ela usa.

Isso deixa o código mais fácil de entender e manter.

### Por que desativar em vez de remover?

Em sistemas reais, apagar dados pode causar problemas. Uma venda antiga, um atendimento ou um histórico financeiro pode depender daquele cliente.

Por isso, é comum marcar como `inativo`.

## Desafios extras

Depois de entender a versão principal, tente melhorar o projeto:

1. Impedir cadastro de e-mails repetidos.
2. Permitir atualizar o e-mail de um cliente.
3. Listar apenas clientes ativos.
4. Criar uma classe `Empresa`.
5. Salvar os clientes em um arquivo `.csv`.
