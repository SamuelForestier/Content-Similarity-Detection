import similarity_comparison.jaccard_similarity as jaccard_similarity

string1 = "The quick brown fox jumps over the lazy dog."
string2 = "The lazy dog jumps over the quick brown fox."
string3 = "The quick brown fox jumps over the quick brown dog."
string4 = "The quick brown fox jumps over the quick brown dog and the lazy dog."
string5 = "The quick brown fox."
string6 = "The quick brown fox jumps over the quick brown dog."


def test_jaccard_index_string_similarity():
    assert jaccard_similarity.jaccard_index_string_similarity(string1, string2) == 0.6
    assert jaccard_similarity.jaccard_index_string_similarity(string1, string3) == 0.875
    assert jaccard_similarity.jaccard_index_string_similarity(string1, string4) == 0.8
    assert (
        jaccard_similarity.jaccard_index_string_similarity(string1, string5)
        == 0.3333333333333333
    )
    assert jaccard_similarity.jaccard_index_string_similarity(string1, string6) == 0.875

    assert jaccard_similarity.jaccard_index_string_similarity(string2, string3) == 0.5
    assert (
        jaccard_similarity.jaccard_index_string_similarity(string2, string4)
        == 0.6363636363636364
    )
    assert jaccard_similarity.jaccard_index_string_similarity(string2, string5) == 0.5
    assert jaccard_similarity.jaccard_index_string_similarity(string2, string6) == 0.5

    assert jaccard_similarity.jaccard_index_string_similarity(string3, string4) == 0.7
    assert jaccard_similarity.jaccard_index_string_similarity(string3, string5) == 0.375
    assert jaccard_similarity.jaccard_index_string_similarity(string3, string6) == 1.0

    assert (
        jaccard_similarity.jaccard_index_string_similarity(string4, string5)
        == 0.2727272727272727
    )
    assert jaccard_similarity.jaccard_index_string_similarity(string4, string6) == 0.7

    assert jaccard_similarity.jaccard_index_string_similarity(string5, string6) == 0.375


def test_multiple_jaccard_index_string_similarity():
    list_of_strings = [string1, string2, string3, string4, string5, string6]
    jaccard_indices = []
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            jaccard_indices.append(
                jaccard_similarity.jaccard_index_string_similarity(
                    list_of_strings[i], list_of_strings[j]
                )
            )
            print(jaccard_indices)
    average_jaccard_index = sum(jaccard_indices) / len(jaccard_indices)
    assert average_jaccard_index == 0.6028282828282828
