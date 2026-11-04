from implementation import lcs_length, lcs_sequence, lis_length_dp, lis_length_fast, lis_sequence


def is_subsequence(candidate, sequence):
    it = iter(sequence)
    return all(any(value == item for item in it) for value in candidate)


def run_tests():
    assert lcs_length("ABCBDAB", "BDCABA") == 4
    assert lcs_length("AGGTAB", "GXTXAYB") == 4
    assert lcs_length("", "ABC") == 0
    lcs = lcs_sequence("ABCBDAB", "BDCABA")
    assert len(lcs) == 4 and is_subsequence(lcs, "ABCBDAB") and is_subsequence(lcs, "BDCABA")
    print("LCS tests passed")

    sample = [10, 9, 2, 5, 3, 7, 101, 18]
    assert lis_length_dp(sample) == lis_length_fast(sample) == 4
    assert lis_length_fast([]) == 0
    assert lis_length_fast([5, 5, 5]) == 1
    assert lis_length_fast([1, 2, 3, 4]) == 4
    seq = lis_sequence(sample)
    assert len(seq) == 4 and all(seq[i] < seq[i + 1] for i in range(3)) and is_subsequence(seq, sample)
    print("LIS tests passed")
    print("All Day 24 tests passed!")


if __name__ == "__main__":
    print("Example LCS:", lcs_sequence("AGGTAB", "GXTXAYB"))
    print("Example LIS:", lis_sequence([10, 9, 2, 5, 3, 7, 101, 18]))
    run_tests()
