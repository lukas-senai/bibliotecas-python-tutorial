# Projeto: Batalha Pokémon em Python

Este projetinho foi criado para **ensinar o uso de `import` em Python**,
de forma simples e divertida.\
A ideia é mostrar como separar o código em vários arquivos e depois
juntar tudo no programa principal.

------------------------------------------------------------------------

## 📂 Estrutura do projeto

    pokemon_game/
    ├── pokemons.py
    ├── ataques.py
    ├── batalha.py
    └── main.py

------------------------------------------------------------------------

## 🐉 Arquivo `pokemons.py`

Define os Pokémon e seus atributos.

``` python
def get_pokemon(nome):
    if nome == "pikachu":
        return {"nome": "Pikachu", "vida": 100, "ataque": 40}
    elif nome == "charmander":
        return {"nome": "Charmander", "vida": 90, "ataque": 45}
    else:
        return {"nome": "Pokémon desconhecido", "vida": 50, "ataque": 10}
```

------------------------------------------------------------------------

## ⚔️ Arquivo `ataques.py`

Função que aplica um ataque de um Pokémon no outro.

``` python
def atacar(atacante, defensor):
    dano = atacante["ataque"]
    defensor["vida"] -= dano
    print(f"{atacante['nome']} atacou {defensor['nome']} causando {dano} de dano!")
    print(f"Vida de {defensor['nome']}: {defensor['vida']}")
```

------------------------------------------------------------------------

## 🥊 Arquivo `batalha.py`

Organiza uma batalha simples: cada Pokémon ataca uma vez.

``` python
from ataques import atacar

def batalha(pokemon1, pokemon2):
    print(f"=== BATALHA: {pokemon1['nome']} VS {pokemon2['nome']} ===")
    atacar(pokemon1, pokemon2)
    atacar(pokemon2, pokemon1)
```

------------------------------------------------------------------------

## 🎮 Arquivo `main.py`

Programa principal, que junta tudo usando `import`.

``` python
from pokemons import get_pokemon
from batalha import batalha

print("=== BATALHA POKÉMON ===")

p1 = get_pokemon("pikachu")
p2 = get_pokemon("charmander")

batalha(p1, p2)
```

------------------------------------------------------------------------
