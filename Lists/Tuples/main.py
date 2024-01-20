def get_heroes():
    heroes = [
        "Glorfindel",
        2093,
        True,
        "Gandalf",
        1054,
        False,
        "Gimli",
        389,
        False,
        "Aragorn",
        87,
        False,
    ]
    heroes_v2 = []
    hero_names = heroes[::3]
    hero_power = heroes[1::3]
    hero_bool = heroes[2::3]
    range1 = len(heroes) / 3
    for i in range(3):
        hero = (hero_names[i], hero_power[i], hero_bool[i])
        heroes_v2.append(hero)
    return heroes_v2



# Don't touch below this line


def test():
    heroes = get_heroes()
    for hero in heroes:
        print(f"name: {hero[0]}, age: {hero[1]}, is_elf: {hero[2]}")


def main():
    test()


main()