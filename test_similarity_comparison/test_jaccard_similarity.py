import similarity_comparison.jaccard_similarity as js


def test_tokenize_string():
    text = "Hello world, how are you?"
    expected_output = ["hello", "world,", "how", "are", "you?"]
    assert js.tokenize_string(text) == expected_output

    text = "This is a test, with some special characters: %, &, #, @."
    expected_output = [
        "this",
        "is",
        "a",
        "test,",
        "with",
        "some",
        "special",
        "characters:",
        "%,",
        "&,",
        "#,",
        "@.",
    ]
    assert js.tokenize_string(text) == expected_output

    text = "The price is 100 dollars."
    expected_output = ["the", "price", "is", "100", "dollars."]
    assert js.tokenize_string(text) == expected_output

    text = ""
    expected_output = []
    assert js.tokenize_string(text) == expected_output


def test_jaccard_index_function():
    set1 = set([1, 2, 3])
    set2 = set([2, 3, 4])
    expected_output = 0.5
    assert js.jaccard_index_function(set1, set2) == expected_output

    set1 = set(["apple", "orange", "banana"])
    set2 = set(["orange", "banana", "pear"])
    expected_output = 0.5
    assert js.jaccard_index_function(set1, set2) == expected_output

    set1 = set(["apple", "orange", "banana"])
    set2 = set(["grape", "watermelon"])
    expected_output = 0.0
    assert js.jaccard_index_function(set1, set2) == expected_output

    set1 = set([1, 2, 3])
    set2 = set([1, 2, 3])
    expected_output = 1.0
    assert js.jaccard_index_function(set1, set2) == expected_output


def test_jaccard_index_string_similarity():
    assert (
        js.jaccard_index_string_similarity(
            "The quick brown fox jumps over the lazy dog.",
            "The lazy dog jumps over the quick brown fox.",
        )
        == 0.6
    )
    assert (
        js.jaccard_index_string_similarity(
            "The lazy dog jumps over the quick brown fox.",
            "The quick brown fox jumps over the quick brown dog.",
        )
        == 0.5
    )
    assert (
        js.jaccard_index_string_similarity(
            "The quick brown fox jumps over the quick brown dog.",
            "The quick brown fox jumps over the quick brown dog and the lazy dog.",
        )
        == 0.7
    )
    assert (
        js.jaccard_index_string_similarity(
            "The quick brown fox jumps over the quick brown dog and the lazy dog.",
            "The quick brown fox.",
        )
        == 0.2727272727272727
    )
    assert (
        js.jaccard_index_string_similarity(
            "The quick brown fox.", "The quick brown fox jumps over the lazy fox."
        )
        == 0.5
    )
