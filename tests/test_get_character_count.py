from ..src.stats import *

cases = [
    ("test", {"t": 2, "e": 1, "s": 1}),
    ("aaaa", {"a": 4}),
    (
        "test aaaa",
        {
            "t": 2,
            "e": 1,
            "s": 1,
            " ": 1,
            "a": 4,
        },
    ),
    ("", {}),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_character_count(input1)
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


test_cases = cases

main()
