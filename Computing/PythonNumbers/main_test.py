from main import *

run_cases = [
    (3, 5, 2, 1, 4, (15, 3)),
    (5, 5, 5, 5, 5, (25, 5)),
]

submit_cases = run_cases + [
    (1, 2, 3, 4, 5, (15, 3)),
    (0, 0, 0, 0, 10, (10, 2)),
    (0, 0, 0, 0, 0, (0, 0)),
    (10, 20, 30, 40, 50, (150, 30)),
    (2, 2, 2, 2, 2, (10, 2)),
    (1, 1, 1, 1, 1, (5, 1)),
]


def test(sword, arrow, spear, dagger, fire, expected_output):
    print("---------------------------------")
    print(f"Inputs: {sword}, {arrow}, {spear}, {dagger}, {fire}")
    print(f"Expecting: {expected_output}")
    result = calculate_damage(sword, arrow, spear, dagger, fire)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()