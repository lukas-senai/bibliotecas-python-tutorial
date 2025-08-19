import random

print("=== Exemplo de uso da biblioteca random ===")

numero = random.randint(1, 10)
print(f"Número sorteado entre 1 e 10: {numero}")

pokemons = ["Pikachu", "Charmander", "Bulbasaur"]
escolhido = random.choice(pokemons)
print(f"O Pokémon sorteado foi: {escolhido}")
