import similarity_comparison.levenshtein_distance as ld


def test_levenshtein_distance():
    assert ld.levenshtein_distance("abc", "abc") == 0
    assert ld.levenshtein_distance("abc", "def") == 3
    assert ld.levenshtein_distance("kitten", "sitting") == 3
    assert ld.levenshtein_distance("The quick brown fox", "The quick lazy dog") == 7
