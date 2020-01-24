'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # keep the count of "th" occurrences
    if len(word) <= 1:
        return 0
    # start with the indexes 0 and 1
    # split the word into a list
    x = list(word)

    if x[0] == "t" and x[1] == "h":
        x.remove(x[0])
        return 1 + count_th("".join(x))
    else:
        x.remove(x[0])
        return 0 + count_th("".join(x))

# This is a O(n) solution since the loop will run as many times as the length of n.
