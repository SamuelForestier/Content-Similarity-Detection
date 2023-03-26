import similarity_comparison.term_frequency as tf
import math


def test_tokenize_string():
    text = "Hello world, how are you?"
    expected_output = ["hello", "world,", "how", "are", "you?"]
    assert tf.tokenize_string(text) == expected_output

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
    assert tf.tokenize_string(text) == expected_output

    text = "The price is 100 dollars."
    expected_output = ["the", "price", "is", "100", "dollars."]
    assert tf.tokenize_string(text) == expected_output

    text = ""
    expected_output = []
    assert tf.tokenize_string(text) == expected_output


def test_term_frequency():
    document = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    term = "fox"
    assert tf.term_frequency(term, document) == 1 / 9

    document = [
        "the",
        "quick",
        "brown",
        "fox",
        "jumps",
        "over",
        "the",
        "lazy",
        "dog",
        "fox",
    ]
    term = "fox"
    assert tf.term_frequency(term, document) == 2 / 10

    document = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    term = "cat"
    assert tf.term_frequency(term, document) == 0.0

    document = []
    term = "fox"
    assert tf.term_frequency(term, document) == 0.0


def test_inverse_document_frequency():
    corpus = [
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        ["the", "lazy", "dog", "jumps", "over", "the", "brown", "fox", "again"],
    ]
    term = "the"
    assert tf.inverse_document_frequency(term, corpus) == math.log(2 / 2)

    corpus = [
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        ["the", "lazy", "dog", "jumps", "over", "the", "brown", "fox", "again"],
        ["this", "is", "a", "completely", "different", "document"],
    ]
    term = "completely"
    assert tf.inverse_document_frequency(term, corpus) == math.log(3 / 1)

    corpus = [
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        ["the", "lazy", "dog", "jumps", "over", "the", "brown", "fox", "again"],
    ]
    term = "cat"
    assert tf.inverse_document_frequency(term, corpus) == 0.0

    corpus = []
    term = "the"
    assert tf.inverse_document_frequency(term, corpus) == 0.0


def test_tf_idf():
    corpus = [
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        ["the", "lazy", "dog", "jumps", "over", "the", "brown", "fox", "again"],
    ]
    document = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    term = "the"
    assert tf.tf_idf(term, document, corpus) == (2 / 9) * math.log(2 / 2)

    corpus = [
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        ["the", "lazy", "dog", "jumps", "over", "the", "brown", "fox", "again"],
        ["this", "is", "a", "completely", "different", "document"],
    ]
    document = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    term = "the"
    assert tf.tf_idf(term, document, corpus) == (2 / 9) * math.log(3 / 2)

    corpus = [
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        ["the", "lazy", "dog", "jumps", "over", "the", "brown", "fox", "again"],
    ]
    document = ["this", "document", "has", "completely", "different", "words"]
    term = "cat"
    assert tf.tf_idf(term, document, corpus) == 0.0

    corpus = []
    document = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    term = "the"
    assert tf.tf_idf(term, document, corpus) == 0.0
