from main import *

run_cases = [
    (
        [
            "fireball",
            "eldrich blast",
            "fireball",
            "eldrich blast",
            "water gun",
            "eldrich blast",
            "water gun",
            "water gun",
            "fireball",
            "fireball",
            "sunburst",
            "fireball",
            "fireball",
        ],
        ["eldrich blast", "fireball", "sunburst", "water gun"],
    )
]

submit_cases = run_cases + [
    (["fireball", "fireball", "fireball"], ["fireball"]),
    (
        ["fireball", "eldrich blast", "water gun", "sunburst"],
        ["eldrich blast", "fireball", "sunburst", "water gun"],
    ),
    (["water gun", "water gun", "water gun"], ["water gun"]),
    (["sunburst", "sunburst", "sunburst"], ["sunburst"]),
    ([], []),
    (["eldrich blast", "eldrich blast", "eldrich blast"], ["eldrich blast"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * spells: {input}")
    print(f"Expecting: {expected_output}")
    result = remove_duplicates(input)
    if isinstance(result, list):
        result.sort()
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