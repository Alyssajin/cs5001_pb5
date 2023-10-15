"""
Student name: Alyssa Nuanxin Jin
Semester: Fall 2023
Question: ProblemSet 5-5 c
"""


def cal_combination(n: int, r: int) -> int:
    """
    Calculate n choose r
    Equation: nCr = (n - 1)C(r) + (n - 1)C(r -1)

    :param n: int
    :param r: int
    :return: int nCr
    """
    if n <= 1 or r <= 0 or r == n:
        return 1
    elif r == 1:
        return n
    else:
        return cal_combination((n-1), r) + cal_combination((n-1), (r - 1))


def cal_sn_method_1(n: int) -> int:
    """
    Calculate S(n)
    S(n) = nC0 ^ 2 + nC1 ^ 2 + ... + nCn ^2

    :param n: int
    :return: S(n)
    """
    s = 0  # initialize S(n) value
    for num in range(n + 1):
        s += cal_combination(n, num) * cal_combination(n, num)
    return s


def cal_sn_method_2(n: int) -> int:
    """
    Calculate S(n)
    S(n) = nC0 ^ 2 + nC1 ^ 2 + ... + nCn ^2 = (2n)Cn

    :param n: int
    :return: S(n)
    """
    return cal_combination(2 * n, n)


def main():
    n = 6
    s1 = cal_sn_method_1(6)  # s1 = S(n) by using method one
    s2 = cal_sn_method_2(6)  # s2 = S(n) by using method two
    print(f"When n = {n}, S(n) = {s1} by using the first method.")
    print(f"When n = {n}, S(n) = {s2} by using the second method.")


if __name__ == "__main__":
    main()