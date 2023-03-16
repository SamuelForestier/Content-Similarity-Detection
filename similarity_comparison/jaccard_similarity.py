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


def jaccard_index_function(set1, set2):
    """
    Calculates the Jaccard Index between two sets.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        float: The Jaccard Index between the two sets.
    """
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    jaccard_index = len(intersection) / len(union)
    return jaccard_index


def jaccard_index_string_similarity(string1, string2):
    """
    Calculates the Jaccard Index between two strings by first tokenizing them.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        float: The Jaccard Index between the two strings.
    """
    set1 = set(tokenize_string(string1))
    set2 = set(tokenize_string(string2))
    jaccard_index = jaccard_index_function(set1, set2)
    return jaccard_index
