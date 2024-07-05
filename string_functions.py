# reverse of string
def reverse(x):
    return x[::-1]

# pallindrome test
def pallindrome(x):
    return x.lower() == reverse(x.lower())

# case conversion to lowercase
def convert_lower(x):
    return x.lower()
