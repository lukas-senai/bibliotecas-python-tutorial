# Explicando Imports em Python

## 📌 Ideia geral

O `import` em Python serve para trazer **módulos** (arquivos de código)
e **bibliotecas** (coleções de módulos prontos) para dentro do programa.

Uma boa comparação é com **caixas de ferramentas**:
- O Python já vem com várias caixas prontas.
- Quando precisamos de uma ferramenta que não está na nossa mesa, usamos
`import` para trazer a caixa.

Exemplo do mundo real:
Imagine que você tem um kit de LEGO. As peças básicas já estão com você,
mas para construir um carro você precisa do conjunto de rodas. Então
você pede a caixa de rodas (`import`).

------------------------------------------------------------------------

## 📦 Tipos de importações

### 1. Importar uma biblioteca inteira

``` python
import math
print(math.sqrt(25))  # usa a função de raiz quadrada
```

➡️ Estou trazendo a caixa inteira e usando a ferramenta dentro dela.

### 2. Importar apenas uma parte

``` python
from math import sqrt
print(sqrt(25))
```

➡️ Estou pegando só a chave de fenda da caixa, em vez de trazer tudo.

### 3. Usar apelido

``` python
import numpy as np
```

➡️ É como dar um apelido para a caixa, para não precisar falar o nome
grande toda hora.

------------------------------------------------------------------------

## 📂 Imports de arquivos próprios

Podemos criar nossos módulos (arquivos `.py`) e importar:

**meu_modulo.py**

``` python
def saudacao():
    print("Olá, mundo!")
```

**main.py**

``` python
import meu_modulo
meu_modulo.saudacao()
```

➡️ É como dividir o código em pastas e puxar só o que precisamos.

------------------------------------------------------------------------

## 🎯 Por que usar `import`?

-   Evita **repetição de código**
-   Permite **organizar programas grandes** em arquivos menores
-   Aproveita **bibliotecas prontas** da comunidade

------------------------------------------------------------------------

## 🧰 Analogia final

`import` é como abrir uma mochila com materiais escolares:
- `import biblioteca` ➝ pegar a mochila inteira.
- `from biblioteca import item` ➝ pegar só um lápis da mochila.
- `import biblioteca as apelido` ➝ escrever seu nome na mochila para não
confundir.
