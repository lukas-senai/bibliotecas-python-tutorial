"""Retorna informações do Pokémon escolhido."""
def get_pokemon(nome):
    if nome == "pikachu":
        return {"nome": "Pikachu", "vida": 100, "ataque": 40}
    elif nome == "charmander":
        return {"nome": "Charmander", "vida": 90, "ataque": 45}
    else:
        return {"nome": "Pokémon desconhecido", "vida": 50, "ataque": 10}
