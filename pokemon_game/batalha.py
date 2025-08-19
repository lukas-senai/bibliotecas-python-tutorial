from ataques import atacar

"""Cada Pokémon ataca uma vez."""
def batalha(pokemon1, pokemon2):
    print(f"\n=== BATALHA: {pokemon1['nome']} VS {pokemon2['nome']} ===\n")

    atacar(pokemon1, pokemon2)  # primeiro ataque
    atacar(pokemon2, pokemon1)  # contra-ataque
