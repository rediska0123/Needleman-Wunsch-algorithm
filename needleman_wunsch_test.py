import pytest
from needleman_wunsch import get_max_score_alignment
import numpy as np


def test_get_max_score_alignment():
    m = np.array([[10, -1, -3, -4],
                  [-1, 7, -5, -3],
                  [-3, -5, 9, 0],
                  [-4, -3, 0, 8]])
    tests = [
        ("GTTACAA", "GACGTTT", -5, 1.0, "GTTACAA--", "G--ACGTTT"),
        ("G", "G", 10, 20.0, "-G", "G-"),
        ("G", "", -5, -5, "G", "-"),
    ]
    for dna1, dna2, d, expected_score, aligned_dna1, aligned_dna2 in tests:
        assert get_max_score_alignment(dna1, dna2, m, d) == (expected_score, aligned_dna1, aligned_dna2)
