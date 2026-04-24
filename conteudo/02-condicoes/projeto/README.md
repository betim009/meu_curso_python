# Projeto - Sistema de Validação de Usuário

Neste projeto, você vai criar uma validação simples de acesso.

Esse tipo de regra aparece em sistemas internos, plataformas de clientes, áreas administrativas e cadastros de usuários.

---

## Objetivo

Criar um programa que verifica:

- idade mínima;
- status do usuário;
- senha;
- número de tentativas.

O sistema deve retornar mensagens diferentes conforme a situação.

---

## Regras do sistema

O acesso deve seguir esta ordem:

1. Se o usuário tiver 3 ou mais tentativas, bloquear por tentativas.
2. Se o usuário for menor de 18 anos, bloquear por idade.
3. Se o usuário estiver inativo, bloquear por status.
4. Se a senha estiver errada, negar acesso.
5. Se tudo estiver correto, liberar acesso.

Essa ordem é importante porque sistemas reais costumam validar primeiro os bloqueios mais graves.

---

## Dados usados

O sistema usa:

| Dado | Tipo | Exemplo |
|---|---|---|
| `idade` | `int` | `25` |
| `usuario_ativo` | `bool` | `True` |
| `senha_digitada` | `str` | `"python123"` |
| `senha_cadastrada` | `str` | `"python123"` |
| `tentativas` | `int` | `1` |

---

## Código completo

O código está no arquivo [`validacao_usuario.py`](validacao_usuario.py).

Execute com:

```bash
python validacao_usuario.py
```

---

## Exemplo de cenário aprovado

```python
idade = 25
usuario_ativo = True
senha_digitada = "python123"
senha_cadastrada = "python123"
tentativas = 1
```

Saída:

```text
Acesso liberado.
```

---

## Decisões tomadas

- `tentativas >= 3` vem primeiro porque bloqueio de segurança deve ter prioridade.
- `idade < 18` vem antes da senha porque o usuário nem deveria acessar.
- `not usuario_ativo` deixa claro que estamos tratando usuário inativo.
- A comparação de senha usa `==`.
- O `else` final representa o cenário em que todas as regras foram atendidas.

---

## Melhorias futuras

Depois de estudar os próximos módulos, você poderá melhorar este projeto com:

- `input()` para receber dados digitados;
- `try/except` para tratar idade inválida;
- funções para organizar as validações;
- repetição para permitir novas tentativas;
- banco de dados para armazenar usuários reais.
