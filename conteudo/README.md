# Guia dos Módulos

Esta pasta contém o conteúdo principal do curso.

Cada módulo deve ajudar o aluno a responder quatro perguntas:

1. O que estou aprendendo?
2. Por que isso é útil?
3. Como uso isso em Python?
4. Quais erros devo evitar?

---

## Ordem recomendada

| Ordem | Pasta | Tema |
|---|---|---|
| 1 | `01-tipos_dados` | Variáveis, textos, números, listas e dicionários |
| 2 | `02-condicoes` | Decisões com `if`, `elif` e `else` |
| 3 | `03-repeticoes` | Repetição com `for` e `while` |
| 4 | `04-funcoes` | Organização do código com funções |
| 5 | `05-tryexcepts` | Tratamento de erros |
| 6 | `06-arquivos` | Leitura e escrita de arquivos |
| 7 | `07-classes` | Classes e objetos |
| 8 | `08-POO` | Exemplos mais avançados de orientação a objetos |
| 9 | `09-pandas` | Manipulação de tabelas e CSV |
| 10 | `10-requests` | Requisições para APIs |
| 11 | `11-plots` | Criação de gráficos |
| 12 | `12-MySQL` | Banco de dados MySQL |
| 13 | `13-flask` | Aplicações web com Flask |
| 14 | `14-streamlit` | Dashboards com Streamlit |
| 15 | `15-customtkinter` | Interfaces gráficas desktop |
| 16 | `16-CTK` | Projetos adicionais com CustomTkinter |
| 17 | `17-selenium` | Automação com navegador |
| 18 | `atividades` | Exercícios, simulados e desafios |

---

## Padrão recomendado para cada aula

Todo módulo deve seguir, sempre que possível, esta estrutura:

```text
README.md
exemplos/
exercicios/
exercicios/gabaritos/
projeto/
```

O `README.md` de cada módulo deve conter:

1. Explicação simples.
2. Exemplos comentados linha por linha.
3. Quando usar.
4. Por que usar.
5. Erros comuns.
6. Exercícios sugeridos.
7. Mini projeto.
8. Resumo final.

---

## Como estudar um módulo

1. Leia a explicação.
2. Rode os exemplos.
3. Altere valores nos exemplos.
4. Resolva os exercícios sem olhar o gabarito.
5. Compare sua solução com o gabarito.
6. Faça o mini projeto.

O objetivo é entender o raciocínio, não apenas copiar código.

---

## O que não deve ficar nesta pasta

Para manter o curso leve e profissional, esta pasta não deve conter:

- `venv/`
- `__pycache__/`
- `.DS_Store`
- arquivos `.pyc`
- binários de navegador, como `chromedriver`
- arquivos temporários gerados durante testes

Esses itens são ferramentas locais, não conteúdo de aula.
