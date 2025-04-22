# '''
# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter
# and ends with a suitable sentence-ending punctuation mark.
# '''

# test that there is a string in the first place
# test making sure the first letter is capital and last letter has a puntuation mark. 
def grammar_text(text):
    if not text:
            return False
    
    if text[0].isupper() and text[-1] in (".!?"):
        return True
    else:
         return False