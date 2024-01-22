def count_enemies(enemy_names):
    enemy_names_dict = {}
    for name in enemy_names:
        print(name)
        if name not in enemy_names_dict:
            print("added")
            enemy_names_dict[name] = 1
        else:
            print("counted")
            enemy_names_dict[name] += 1
    return enemy_names_dict
