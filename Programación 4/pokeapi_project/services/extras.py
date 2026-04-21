from api.pokeapi_client import get
from collections import Counter

def habitat_mas_comun_planta():
    data = get("type/grass")
    habitats = []

    for p in data["pokemon"]:
        poke = get(p["pokemon"]["url"])
        species = get(poke["species"]["url"])

        if species and species["habitat"]:
            habitats.append(species["habitat"]["name"])

    if not habitats:
        return None

    return Counter(habitats).most_common(1)[0]


def pokemon_mas_liviano():
    min_weight = float("inf")
    lightest = None

    for i in range(1, 500):
        poke = get(f"pokemon/{i}")
        if not poke:
            continue

        if poke["weight"] < min_weight:
            min_weight = poke["weight"]
            lightest = poke["name"]

    return lightest, min_weight