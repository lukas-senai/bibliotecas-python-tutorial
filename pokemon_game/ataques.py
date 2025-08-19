"""Um Pokémon ataca o outro uma vez."""
def atacar(atacante, defensor):
    dano = atacante["ataque"]
    defensor["vida"] -= dano
    print(f"{atacante['nome']} atacou {defensor['nome']} causando {dano} de dano!")
    print(f"Vida de {defensor['nome']}: {defensor['vida']}")
