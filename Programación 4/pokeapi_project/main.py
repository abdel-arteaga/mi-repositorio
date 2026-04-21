from services import tipos, evoluciones, stats, extras

def main():
    print("\n--- TIPOS ---")
    print("Fuego en Kanto:", tipos.fuego_en_kanto())
    print("Agua altura >10:", tipos.agua_altura_mayor_10())

    print("\n--- EVOLUCIONES ---")
    print("Cadena Charmander:", evoluciones.cadena_evolutiva())
    print("Eléctricos sin evolución:", evoluciones.electricos_sin_evolucion())

    print("\n--- STATS ---")
    print("Mayor ataque Johto:", stats.mayor_ataque_johto())
    print("Velocidad max no legendario:", stats.velocidad_max_no_legendario())

    print("\n--- EXTRAS ---")
    print("Hábitat más común (planta):", extras.habitat_mas_comun_planta())
    print("Pokémon más liviano:", extras.pokemon_mas_liviano())


if __name__ == "__main__":
    main()