def find_sum_below(n):
    """
    Function that returns sum of 3 and 5 under an integer n
    @param n: integer
    @return: sum of all multiples of 3 and 5 under n
    """

    return sum([x for x in range(n) if (x%3==0 or x%5==0)])


if __name__ == '__main__':

    n = 1000

    solution = find_sum_below(n)
    print(solution)


