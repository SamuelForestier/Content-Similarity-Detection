import similarity_comparison.longest_common_subsequence as lcs


def test_longest_common_subsequence():
    assert lcs.longest_common_subsequence("", "") == 0
    assert lcs.longest_common_subsequence("fox", "dog") == 1
    assert lcs.longest_common_subsequence("abcde", "bcd") == 3
    assert lcs.longest_common_subsequence("hello", "hello") == 5
    assert lcs.longest_common_subsequence("AGGTAB", "GXTXAYB") == 4
