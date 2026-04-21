from api.pokeapi_client import get

def fuego_en_kanto():
    data = get("type/fire")
    count = 0

    for p in data["pokemon"]:
        poke = get(p["pokemon"]["url"])
        if poke and poke["id"] <= 151:
            count += 1

    return count


def agua_altura_mayor_10():
    data = get("type/water")
    result = []

    for p in data["pokemon"]:
        poke = get(p["pokemon"]["url"])
        if poke and poke["height"] > 10:
            result.append(poke["name"])

    return result