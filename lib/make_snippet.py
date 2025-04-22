# take a string as an argument
# returns the first five words if the string is less than 5 or equal to five words
# if longer than 5 words, it returns the first five words + ...

def make_snippet(string):
    words = string.split(" ")
    if len(words) > 5:
        first_five = words[:5]
        snippet = " ".join(first_five)
        return snippet + "..."
    else:
        return string
print(make_snippet("i AM THE BEST DRIVER IN THE ENTIRE WORLD"))