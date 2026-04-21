from api.pokeapi_client import get

def cadena_evolutiva(nombre="charmander"):
    poke = get(f"pokemon/{nombre}")
    if not poke:
        return []

    species = get(poke["species"]["url"])
    chain_data = get(species["evolution_chain"]["url"])

    chain = []
    evo = chain_data["chain"]

    while evo:
        chain.append(evo["species"]["name"])
        evo = evo["evolves_to"][0] if evo["evolves_to"] else None

    return chain


def electricos_sin_evolucion():
    data = get("type/electric")
    result = []

    for p in data["pokemon"]:
        poke = get(p["pokemon"]["url"])
        species = get(poke["species"]["url"])
        chain = get(species["evolution_chain"]["url"])

        if not chain["chain"]["evolves_to"]:
            result.append(poke["name"])

    return result