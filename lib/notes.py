# # As a user
# So that I can find my tasks among all my notes
# I want to check if a line from my notes includes the string `#TODO`.

# >>> includes_todo("#TODO buy milk")
# True
# >>> includes_todo("drink tea")
# False
# >>> includes_todo("learn to test-drive my code #TODO")
# True
def find_TODO(line):
    if "TODO" in line:
        return True
    else:
        return False

my_notes = ("is milk TODO")
print(find_TODO(my_notes))