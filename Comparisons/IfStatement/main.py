def print_status(player_health):
    if player_health == 0:
        print("dead")
    else:
        print("status check complete")
    

# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(3)


main()