# Exercício 03 - Média do Aluno

## Objetivo

Usar métodos para fazer cálculos.

## Enunciado

Crie uma classe chamada `Aluno`.

A classe deve ter:

- `nome`
- `nota_1`
- `nota_2`

Crie um método chamado `calcular_media()` que retorne a média das duas notas.

Crie outro método chamado `situacao()` que retorne:

- `"Aprovado"` se a média for maior ou igual a 7
- `"Reprovado"` se a média for menor que 7

## Exemplo

```python
aluno = Aluno("Carlos", 8, 6)
print(aluno.calcular_media())
print(aluno.situacao())
```

## Saída esperada

```text
7.0
Aprovado
```
