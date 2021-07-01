phrase = input("Set a phrase: ")


def test_short_phrase():
    try:
        assert len(phrase) != 0 and len(phrase) <= 15, \
            f"Set phrase is longer than 15 characters. It contains {len(phrase)} characters"
    except EOFError:
        assert False, f"Set phrase is empty {len(phrase)}"
