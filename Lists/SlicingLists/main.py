def get_champion_slices(champions):
    inverse_champs = champions[2:]
    third_champ    = champions[0:-2]
    even_champs    = champions[0::+2]
    return inverse_champs, third_champ, even_champs
