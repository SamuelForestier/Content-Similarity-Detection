def levenshtein_distance(string1, string2):
    """
    Calculates the Levenshtein distance between two strings.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    len_s1 = len(string1)
    len_s2 = len(string2)

    dist_matrix = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]

    for i in range(len_s1 + 1):
        dist_matrix[i][0] = i
    for j in range(len_s2 + 1):
        dist_matrix[0][j] = j

    for j in range(1, len_s2 + 1):
        for i in range(1, len_s1 + 1):
            if string1[i - 1] == string2[j - 1]:
                cost = 0
            else:
                cost = 1
            dist_matrix[i][j] = min(
                dist_matrix[i - 1][j] + 1,
                dist_matrix[i][j - 1] + 1,
                dist_matrix[i - 1][j - 1] + cost,
            )

    return dist_matrix[len_s1][len_s2]
