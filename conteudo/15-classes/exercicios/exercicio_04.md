# Exercício 04 - Conta Bancária

## Objetivo

Praticar atributos, métodos e validações.

## Enunciado

Crie uma classe chamada `ContaBancaria`.

A classe deve ter:

- `titular`
- `saldo`

Crie os métodos:

- `depositar(valor)`
- `sacar(valor)`
- `mostrar_saldo()`

Regras:

- Não permita depósito menor ou igual a zero.
- Não permita saque menor ou igual a zero.
- Não permita saque maior que o saldo.

## Exemplo

```python
conta = ContaBancaria("Joao", 100)
conta.depositar(50)
conta.sacar(30)
print(conta.mostrar_saldo())
```

## Saída esperada

```text
Saldo atual: R$ 120.00
```
