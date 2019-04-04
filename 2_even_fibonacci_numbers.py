def get_fibonacci_sequence(n):
    """

    @param n: integer, maximum value of fibonacci list generated
    @return: list, of fibonacci numbers below n
    """

    sequence = [1, 2]
    while sequence[-1] < n:
        sequence.append(sequence[-1]+sequence[-2])

    return sequence


def get_sum_of_even_numbers(n):
    """

    @param n: integer maximum value of fibonacci sequence
    @return: sum of even fibonacci numbers below n
    """
    sequence = get_fibonacci_sequence(n)

    return sum([x for x in sequence if x%2==0])


if __name__ == '__main__':

    n = 4000000

    solution = get_sum_of_even_numbers(n)
    print(solution)
