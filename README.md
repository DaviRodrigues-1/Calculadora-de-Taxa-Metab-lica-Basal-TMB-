# Calculadora-de-Taxa-Metab-lica-Basal-TMB-
---

Este é um simples script em Python que calcula a Taxa Metabólica Basal (TMB) de uma pessoa, ou seja, a quantidade de calorias que o corpo queima em repouso para manter suas funções vitais. A TMB é um parâmetro importante para quem deseja controlar a alimentação e o gasto energético, como no caso de dietas ou planos de exercícios.

## Como Funciona

- O programa solicita ao usuário as seguintes informações:
  - **Sexo** (M para masculino, F para feminino)
  - **Peso** em quilogramas
  - **Altura** em centímetros
  - **Idade** em anos

- Com base nesses dados, a TMB é calculada usando as fórmulas específicas para cada sexo:
  - Para homens:  
    `TMB = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)`
  - Para mulheres:  
    `TMB = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)`

- O resultado da TMB será exibido em calorias por dia.

## Como Usar

1. Execute o script em seu ambiente Python.
2. O programa pedirá que você insira o seu sexo, peso, altura e idade.
3. Após a inserção dos dados, o valor da TMB será calculado e mostrado na tela.
4. Pressione Enter para finalizar o programa.

## Exemplo de Execução

```text
\t[Calculadora de TMB]

Digite o seu sexo (M para masculino, F para feminino): M
Digite o seu peso em kg: 70
Digite a sua altura em cm: 175
Digite sua idade: 25

Sua Taxa Metabólica Basal (TMB) é: 1754.40 calorias/dia.
Pressione Enter para sair...
```

## Requisitos

- Python 3.x ou superior.
