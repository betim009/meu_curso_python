# Material Python

## 1. Variáveis

* [ ] Marcar como lido.

Uma **variável** é um nome que se refere a um valor armazenado na memória do computador. Em Python, a variável é definida automaticamente pelo valor atribuído. Não é necessário declarar o tipo da variável antecipadamente, o Python faz isso de forma dinâmica.

### Exemplos:

```python
nome = "João"  # String
idade = 25  # Inteiro
altura = 1.75  # Float
```

### Quando usar?

Você deve usar variáveis quando precisar armazenar um valor temporário para manipulá-lo ou usá-lo ao longo do seu código. Exemplos incluem:

- Quando precisar realizar cálculos.
- Para armazenar informações temporárias (como nome de usuário, idade, preços, etc.).
- Para reutilizar valores ou resultados ao longo do código sem precisar duplicá-los.

### Por que usar?

Usar variáveis traz várias vantagens, como:

1. **Legibilidade**: O uso de variáveis permite que você dê nomes significativos aos dados, tornando o código mais fácil de entender.
2. **Reusabilidade**: Você pode armazenar um valor em uma variável e reutilizá-lo várias vezes sem precisar duplicá-lo no código.
3. **Facilidade de manutenção**: Caso precise alterar o valor de uma variável, basta modificar em um único lugar.

### Boas Práticas (Nomes de Variáveis)

- **Seja Descritivo**: Escolha nomes que façam sentido e descrevam o propósito da variável.

  - **Correto**: `idade`, `nome_usuario`, `altura_media`
  - **Errado**: `x`, `y`, `a1`

- **Use Notação PEP8**: A convenção do Python sugere o uso de `snake_case` para variáveis. Isso significa usar letras minúsculas e separar palavras com underscores (`_`).

  - **Correto**: `quantidade_produtos`, `preco_total`
  - **Errado**: `quantidadeProdutos`, `precoTotal`

- **Evite Palavras Reservadas**: Não use palavras reservadas do Python (como `class`, `def`, `for`, etc.) como nome de variáveis.
- **Seja Conciso, Mas Claro**: Use nomes curtos, mas que ainda façam sentido. Por exemplo, ao invés de `numero_de_items_na_lista`, use apenas `num_items`.

### Exemplos de boas práticas:

```python
# Variáveis com nomes descritivos
nome_usuario = "Maria"
idade_usuario = 30
altura_usuario = 1.65

# Evitar nomes confusos ou muito genéricos
x = "João"  # Confuso
preco_item = 10.5  # Claro
```

### Evite Variáveis Globais

Sempre que possível, prefira usar variáveis dentro de funções ou blocos específicos. Variáveis globais podem causar confusão e dificultar a manutenção do código.

```python
# Evite
contador = 0  # Variável global
```

### Resumo

- **Quando usar**: Para armazenar e manipular dados temporários.
- **Por que usar**: Torna o código mais legível, reutilizável e fácil de manter.
- **Boas práticas**: Use nomes descritivos, siga a convenção `snake_case`, evite variáveis globais e palavras reservadas.
