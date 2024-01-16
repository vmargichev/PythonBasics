def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# array_names = ["asd", "ass"]
# x = None
# for name in array_names:
#     x = name
# print(x)

# don't touch below this line

print(f"max_health is: {max_health}")
