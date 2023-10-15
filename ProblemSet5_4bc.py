"""
Student name: Alyssa Nuanxin Jin
Semester: Fall 2023
Question: ProblemSet 5-4 b & 5-4 c
"""


def cal_combination(n: int, r: int) -> int:
    """
    n choose r.
    Equation: nCr = (n-1)Cr + (n-1)C(r-1)

    :param n: int
    :param r: int
    :return: int
    """
    if n <= 1 or r <= 0 or r == n:
        return 1
    elif r == 1:
        return n
    else:
        return cal_combination((n-1), r) + cal_combination((n-1), (r - 1))


def cal_rect(col: int, row: int, r_col: int, r_row: int) -> int:
    """
    Calculate how many rectangles can be formed by col columns and row rows.

    :param col: the number of columns
    :param row: the number of rows
    :param r_row: choose r_row out of row rows.
    :param r_col: choose r_col out of col columns
    :return: the number of rectangles
    """
    return cal_combination((col + 1), r_col) * cal_combination((row + 1), r_row)


def main():
    # ProblemSet 5-4 b
    column = 8  # 8 by 8 boards
    row = 8
    num_rect_8 = cal_rect(col=column, row=row, r_row=2, r_col=2)
    column = 7  # remove one corner. column - 1, row - 1
    row = 7
    num_rect_1 = cal_rect(col=column, row=row, r_row=1, r_col=1)
    num_rect = num_rect_8 - num_rect_1
    print(f"There are {num_rect}, when removing one corner "
          f"from 8 by 8 board.")
    # ProblemSet 5-4 c
    num_rect_remove_4 = num_rect_1 * 4
    num_rect = num_rect_8 - num_rect_remove_4
    print(f"There are {num_rect}, when removing all four "
          f"corner from 8 by 8 board.")


if __name__ == "__main__":
    main()
