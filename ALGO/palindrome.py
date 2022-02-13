# a Palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or level, redivider.



def palindrome(word):
    if word == word[::-1]:
        return (f'True, it is the same word as {word}')
    else:
        return (f'Sorry, not the same word as {word}')



word = "nurses"
print(palindrome(word))