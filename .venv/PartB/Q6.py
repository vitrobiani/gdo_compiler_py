#Q6
palindrome_counts = lambda lst: list(map(lambda sublist: len(list(filter(lambda s: s == s[::-1], sublist))), lst))
print("question 6:")
print(palindrome_counts([["madam", "tet", "level"], ["hello", "wow"], ["noon", "civic", "python"]]))

