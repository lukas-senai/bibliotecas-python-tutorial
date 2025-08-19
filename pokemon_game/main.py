from pokemons import get_pokemon
from batalha import batalha

print("=== BATALHA POKÉMON ===")

p1 = get_pokemon("pikachu")
p2 = get_pokemon("charmander")

batalha(p1, p2)
