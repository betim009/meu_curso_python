# 08 - Programação Orientada a Objetos em Python

Neste módulo você vai aprender a usar **programação orientada a objetos** para organizar sistemas maiores.

No módulo anterior, você aprendeu a criar classes, objetos, atributos e métodos. Agora vamos evoluir esse conhecimento para um uso mais profissional: separar responsabilidades, proteger dados, melhorar a forma de exibir objetos, reutilizar código e preparar sistemas para crescer sem virar bagunça.

Ao final deste módulo, você será capaz de:

- Revisar classes e objetos com segurança.
- Entender encapsulamento de forma simples.
- Usar métodos especiais como `__str__`.
- Separar responsabilidades entre classes.
- Entender herança sem excesso de teoria.
- Entender a ideia inicial de polimorfismo.
- Criar estruturas reutilizáveis para sistemas reais.
- Construir um sistema simples de pedidos para ecommerce.

## Estrutura do módulo

```text
08-POO/
  README.md
  exemplos/
    01_revisao_classes.py
    02_encapsulamento_cliente.py
    03_metodo_str_produto.py
    04_responsabilidades_pedido.py
    05_heranca_funcionarios.py
    06_polimorfismo_pagamentos.py
  exercicios/
    README.md
    exercicio_01.md
    exercicio_02.md
    exercicio_03.md
    exercicio_04.md
    exercicio_05.md
    exercicio_06.md
    exercicio_07.md
    exercicio_08.md
    exercicio_09.md
    exercicio_10.md
    exercicio_11.md
    exercicio_12.md
    exercicio_13.md
    gabaritos/
      exercicio_01.py
      exercicio_02.py
      exercicio_03.py
      exercicio_04.py
      exercicio_05.py
      exercicio_06.py
      exercicio_07.py
      exercicio_08.py
      exercicio_09.py
      exercicio_10.py
      exercicio_11.py
      exercicio_12.py
      exercicio_13.py
  projeto/
    README.md
    sistema_pedidos.py
```

## 1. Introdução: sistemas grandes ficam desorganizados

Quando um programa é pequeno, é comum resolver tudo com algumas variáveis, listas, dicionários e funções.

Mas um sistema real cresce rápido.

Imagine um ecommerce simples. Ele precisa lidar com:

- clientes;
- produtos;
- pedidos;
- pagamentos;
- descontos;
- estoque;
- status do pedido;
- relatórios.

Se tudo ficar misturado no mesmo arquivo e nas mesmas funções, o código começa a ter problemas:

- uma mudança em produto quebra pedido;
- uma regra de cliente fica espalhada em vários lugares;
- fica difícil encontrar onde alterar;
- fica fácil repetir código;
- o sistema vira difícil de testar;
- novas funcionalidades demoram mais.

POO ajuda a resolver isso organizando o sistema em partes menores.

Cada classe representa uma parte importante do sistema:

```text
Cliente cuida dos dados do cliente.
Produto cuida dos dados do produto.
Pedido cuida dos produtos comprados e do total.
Pagamento cuida da forma de pagamento.
```

Isso não significa criar classes para tudo. Significa criar classes quando elas deixam o sistema mais claro.

## 2. Revisão rápida de classes

Uma classe é um modelo. Um objeto é algo criado a partir desse modelo.

```python
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_dados(self):
        return f"{self.nome} - {self.email}"


cliente = Cliente("Ana Souza", "ana@email.com")
print(cliente.exibir_dados())
```

Nesse exemplo:

- `Cliente` é a classe;
- `cliente` é o objeto;
- `nome` e `email` são atributos;
- `exibir_dados` é um método.

Até aqui, a ideia principal é:

```text
dados relacionados + ações relacionadas = classe
```

POO profissional começa quando você passa a pensar também em organização:

```text
Quem deve guardar esse dado?
Quem deve executar essa regra?
Quem deve conhecer essa informação?
```

Essas perguntas ajudam a evitar classes confusas.

## 3. Encapsulamento

Encapsulamento significa controlar como os dados de um objeto são acessados e alterados.

Pense em uma conta bancária.

O saldo não deveria ser alterado livremente assim:

```python
conta.saldo = -9999
```

Isso quebraria a regra do sistema.

Uma forma melhor é permitir que o saldo mude apenas por métodos:

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito precisa ser positivo.")
            return

        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque precisa ser positivo.")
            return

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return

        self._saldo -= valor

    def consultar_saldo(self):
        return self._saldo
```

O atributo `_saldo` começa com um sublinhado. Em Python, isso é uma convenção que significa:

```text
Este atributo é interno. Evite mexer diretamente nele.
```

Python não impede totalmente o acesso, mas a convenção ajuda outros programadores a entenderem a intenção.

O ponto mais importante é: regras importantes devem ficar em métodos.

## 4. Métodos especiais

Métodos especiais são métodos que o Python reconhece por causa do nome com dois sublinhados.

Você já viu um deles:

```python
__init__
```

Ele é executado quando um objeto é criado.

Outro método muito útil é:

```python
__str__
```

Ele define como o objeto aparece quando usamos `print`.

Sem `__str__`:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto = Produto("Teclado", 150.00)
print(produto)
```

A saída será parecida com:

```text
<__main__.Produto object at 0x...>
```

Isso não ajuda o usuário nem o programador.

Com `__str__`:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


produto = Produto("Teclado", 150.00)
print(produto)
```

Saída:

```text
Teclado - R$ 150.00
```

Esse método deixa a saída mais organizada e facilita depuração.

## 5. Organização de código

Em POO, uma das decisões mais importantes é separar responsabilidades.

Veja este exemplo ruim:

```python
class Sistema:
    def cadastrar_cliente(self):
        pass

    def calcular_total_pedido(self):
        pass

    def aplicar_desconto_produto(self):
        pass

    def calcular_salario_funcionario(self):
        pass
```

Essa classe faz coisas demais.

Uma organização melhor:

```python
class Cliente:
    pass


class Produto:
    pass


class Pedido:
    pass


class Funcionario:
    pass
```

Cada classe cuida de uma parte.

Exemplo prático:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco

        return total
```

O produto sabe seu nome e preço. O pedido sabe quais produtos foram adicionados e como calcular o total.

Essa divisão deixa o código mais fácil de entender e evoluir.

## 6. Introdução leve a herança

Herança permite criar uma classe a partir de outra.

Pense em funcionários de uma empresa:

- todo funcionário tem nome e salário;
- um vendedor também tem comissão;
- um gerente também tem bônus.

Podemos criar uma classe base:

```python
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario
```

E classes mais específicas:

```python
class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao

    def calcular_pagamento(self):
        return self.salario + self.comissao
```

`Vendedor` herda de `Funcionario`.

O `super().__init__` chama o `__init__` da classe base para reaproveitar a criação de `nome` e `salario`.

Use herança quando uma frase fizer sentido:

```text
Vendedor é um Funcionário.
Gerente é um Funcionário.
ProdutoDigital é um Produto.
```

Evite herança quando a relação não for "é um".

Por exemplo:

```text
Pedido não é um Cliente.
Pedido pertence a um Cliente.
```

Nesse caso, use um atributo:

```python
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
```

## 7. Polimorfismo: introdução simples

Polimorfismo significa usar objetos diferentes de forma parecida.

O nome parece difícil, mas a ideia é simples.

Imagine diferentes formas de pagamento:

- cartão de crédito;
- pix;
- boleto.

Cada uma processa o pagamento de um jeito. Mas o sistema pode chamar o mesmo método:

```python
pagamento.processar(valor)
```

Exemplo:

```python
class PagamentoCartao:
    def processar(self, valor):
        return f"Pagamento de R$ {valor:.2f} no cartão aprovado."


class PagamentoPix:
    def processar(self, valor):
        return f"Pagamento de R$ {valor:.2f} via Pix aprovado."


pagamentos = [PagamentoCartao(), PagamentoPix()]

for pagamento in pagamentos:
    print(pagamento.processar(100))
```

Os objetos são diferentes, mas respondem ao mesmo método `processar`.

Isso ajuda o sistema a crescer. Se amanhã entrar boleto, você cria uma nova classe com o método `processar`.

## 8. Boas práticas

### Crie classes com responsabilidade clara

Uma classe deve ter um motivo principal para existir.

Boas classes:

- `Cliente`
- `Produto`
- `Pedido`
- `Funcionario`
- `PagamentoPix`

Classes confusas:

- `Coisas`
- `Dados`
- `SistemaGeral`
- `ProcessadorDeTudo`

### Prefira nomes que expliquem o domínio

Domínio é a área do sistema.

Em ecommerce, nomes como `Pedido`, `Carrinho`, `Produto` e `Pagamento` fazem sentido.

Em RH, nomes como `Funcionario`, `FolhaPagamento` e `Cargo` fazem sentido.

### Comece simples

Não tente usar todos os conceitos de POO ao mesmo tempo.

Muitas vezes, uma boa solução usa apenas:

- classes;
- atributos;
- métodos;
- listas de objetos;
- validações simples.

### Use herança com cuidado

Herança é útil, mas pode deixar o sistema difícil se for usada cedo demais.

Antes de usar herança, pergunte:

```text
Essa classe realmente é um tipo da outra?
```

Se a resposta for não, use composição: uma classe contendo outra como atributo.

## 9. Erros comuns

### Exagerar na complexidade

Não crie dez classes para resolver um problema de duas funções.

POO deve simplificar o sistema, não deixá-lo mais difícil.

### Criar classes desnecessárias

Evite classes sem dados e sem comportamento relevante.

```python
class Calculadora:
    pass
```

Se a classe não representa uma entidade, regra ou responsabilidade clara, talvez uma função seja suficiente.

### Misturar responsabilidades

Evite colocar cadastro, relatório, pagamento, estoque e funcionário na mesma classe.

Isso deixa a manutenção difícil.

### Proteger dados sem criar métodos úteis

Não adianta usar `_saldo` se o sistema não oferece métodos como `depositar`, `sacar` e `consultar_saldo`.

Encapsulamento não é só esconder. É controlar o uso.

### Usar herança onde deveria usar atributo

Errado:

```text
Pedido herda de Cliente
```

Pedido não é um cliente.

Melhor:

```text
Pedido tem um Cliente
```

## 10. Mini desafios

1. Crie uma classe `Cliente` com `__str__`.
2. Crie uma classe `Produto` com atributo `_preco` e método `alterar_preco`.
3. Crie uma classe `Pedido` que recebe um `Cliente`.
4. Faça `Pedido` adicionar vários produtos em uma lista.
5. Faça `Pedido` calcular o total.
6. Crie uma classe `Funcionario` e uma classe `Vendedor` herdando dela.
7. Faça `Vendedor` calcular salário com comissão.
8. Crie duas formas de pagamento com o método `processar`.
9. Crie uma lista com pagamentos diferentes e chame `processar` em todos.
10. Revise uma classe que você já criou e pergunte: ela tem responsabilidade clara?

## 11. Resumo

- POO ajuda a organizar sistemas maiores.
- Classes devem representar entidades ou responsabilidades reais.
- Encapsulamento controla como dados importantes são alterados.
- `__str__` melhora a forma como objetos aparecem em textos e prints.
- Separar responsabilidades deixa o código mais fácil de manter.
- Herança permite reaproveitar código quando uma classe é um tipo de outra.
- Polimorfismo permite tratar objetos diferentes por meio de métodos com o mesmo nome.
- O objetivo não é usar conceitos avançados por obrigação. O objetivo é escrever código mais claro, reutilizável e preparado para crescer.

## Próximos passos

1. Estude os exemplos em [`exemplos`](exemplos).
2. Resolva os exercícios em [`exercicios`](exercicios).
3. Compare suas soluções com os gabaritos em [`exercicios/gabaritos`](exercicios/gabaritos).
4. Faça o projeto em [`projeto`](projeto).
