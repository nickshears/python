def isPalindrome(original_phrase):

    original_phrase = original_phrase.lower()
    
    phrase = ''

    for letter in original_phrase:

        if (letter.isalpha()):

            # use only letters from the phrase and ignore everything else
            phrase += letter

    # compare the newly modified phrase against itself but reversed
    if (phrase == phrase[::-1]):

        return True

    return False
    
result = isPalindrome('Won kiosk. So, I know')
print(result)
