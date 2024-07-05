def reverse(x):
    return x[::-1]

def pallindrome(x):
    return x.lower() == reverse(x.lower())
