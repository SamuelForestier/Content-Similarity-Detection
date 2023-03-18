def longest_common_subsequence(string1, string2):
    """
    Calculates the length of the longest common subsequence between two strings.

    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.

    Returns:
        int: The length of the longest common subsequence between the two input strings.
    """
    length1 = len(string1)
    length2 = len(string2)

    table = [[0 for _ in range(length2 + 1)] for _ in range(length1 + 1)]

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if string1[i - 1] == string2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[length1][length2]
