import math


def tokenize_string(text):
    """
    Tokenizes a string into a list of lowercased words.

    Args:
        text (str): The text to tokenize.

    Returns:
        list: The list of tokenized words.
    """
    words = text.lower().split()
    return words


def term_frequency(term, document):
    """
    Calculates the term frequency (TF) of a term in a document.

    Args:
        term (str): The term to calculate the frequency of.
        document (list): A list of words representing the document.

    Returns:
        float: The term frequency of the term in the document.
    """
    if len(document) == 0:
        return 0.0
    else:
        return document.count(term) / len(document)


def inverse_document_frequency(term, corpus):
    """
    Calculates the inverse document frequency (IDF) of a term in a corpus.

    Args:
        term (str): The term to calculate the IDF of.
        corpus (list): A list of documents, where each document is represented as a list of words.

    Returns:
        float: The IDF of the term in the corpus.
    """
    if len(corpus) == 0:
        return 0.0
    else:
        count = sum(1 for document in corpus if term in document)
        return math.log(len(corpus) / (1 + count))


def tf_idf(term, document, corpus):
    """
    Calculates the term frequency-inverse document frequency (TF-IDF) score of a term in a document.

    Args:
        term (str): The term to calculate the TF-IDF score of.
        document (list): A list of words representing the document.
        corpus (list): A list of documents, where each document is represented as a list of words.

    Returns:
        float: The TF-IDF score of the term in the document and corpus.
    """
    tf = term_frequency(term, document)
    idf = inverse_document_frequency(term, corpus)
    return tf * idf
