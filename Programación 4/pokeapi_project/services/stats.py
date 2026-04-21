from api.pokeapi_client import get

def mayor_ataque_johto():
    max_attack = 0
    best = None

    for i in range(152, 252):
        poke = get(f"pokemon/{i}")
        if not poke:
            continue

        for stat in poke["stats"]:
            if stat["stat"]["name"] == "attack":
                if stat["base_stat"] > max_attack:
                    max_attack = stat["base_stat"]
                    best = poke["name"]

    return best, max_attack


def velocidad_max_no_legendario():
    max_speed = 0
    fastest = None

    for i in range(1, 500):
        poke = get(f"pokemon/{i}")
        if not poke:
            continue

        species = get(poke["species"]["url"])
        if species and species["is_legendary"]:
            continue

        for stat in poke["stats"]:
            if stat["stat"]["name"] == "speed":
                if stat["base_stat"] > max_speed:
                    max_speed = stat["base_stat"]
                    fastest = poke["name"]

    return fastest, max_speed