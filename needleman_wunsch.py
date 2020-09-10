import numpy as np


supported_letters = ['A', 'G', 'C', 'T']


def get_max_score_alignment(s1: str, s2: str, matrix: np.ndarray, d: int):
    """Returns the highest score alignment for two dna sequences: <dna1>, <dna2>.
    Uses <matrix> and <d> as a scoring system."""
    for i in s1 + s2:
        if i not in supported_letters:
            raise(Exception(i + " is not from " + ','.join(supported_letters)))
    f = np.zeros((len(s1) + 1, len(s2) + 1))
    f[:, 0] = np.arange(start=0, stop=(len(s1) + 1) * d, step=d)
    f[0, :] = np.arange(start=0, stop=(len(s2) + 1) * d, step=d)

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            f[i, j] = max(
                f[i - 1, j - 1] + matrix[supported_letters.index(s1[i - 1]),
                                         supported_letters.index(s2[j - 1])],
                f[i - 1, j] + d,
                f[i, j - 1] + d
            )

    i, j = len(s1), len(s2)
    s1_aligned, s2_aligned = '', '';
    while i > 0 or j > 0:
        symb1, symb2 = s1[i - 1] if i != 0 else '-', s2[j - 1] if  j != 0 else '-'
        if i != 0 and f[i, j] == f[i - 1, j] + d:
            i = i - 1
            symb2 = '-'
        elif j != 0 and f[i, j] == f[i, j - 1] + d:
            j = j - 1
            symb1 = '-'
        else:
            i, j = i - 1, j - 1
        s1_aligned = symb1 + s1_aligned
        s2_aligned = symb2 + s2_aligned
    return f[len(s1), len(s2)], s1_aligned, s2_aligned


if __name__ == "__main__":
    fin = open("input.txt", "r")
    matrix = [[] for i in range(len(supported_letters))]
    for i in range(len(supported_letters)):
        matrix[i] = list(map(int, fin.readline().split(' ')))
    matrix = np.array(matrix)

    d = int(fin.readline())
    dna1 = fin.readline().strip()
    dna2 = fin.readline().strip()

    highest_score, aligned_dna1, aligned_dna2 = get_max_score_alignment(dna1, dna2, matrix, d)

    print("Score: ", highest_score)
    print(aligned_dna1)
    print(aligned_dna2)