from functools import reduce
#Q3
cumulative_sums_of_squares = lambda lst: list(
    map(
        lambda sublist: reduce(
            lambda w, x: w + x,
            map(
                lambda y: y ** 2,
                filter(
                    lambda z: z % 2 == 0,
                    sublist
                )
            ),
            0
        ),
        lst
    )
)
print("question 3:")
print(cumulative_sums_of_squares([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

