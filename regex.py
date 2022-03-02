import re

# 1. Function program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))

# 2. Function that matches a string that has an a followed by zero or more b's
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))

# 3. Function that matches a string that has an a followed by one or more b's
def text_match(text):
        patterns = '^a(b+)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))

# 4. Function that matches a string that has an a followed by zero or one b
def text_match(text):
    patterns = '^a(b?)$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))

# 5. Function that matches a string that has an a followed by three to five b's
def text_match(text):
    patterns = '^a(b{3,5})$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abbb"))
 
# 6. Function that find sequences of lowercase letters joined with a underscore
def text_match(text):
    patterns = '^([a-z]+_[a-z]+)$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

# 7. Function that find the sequences of one upper case letter followed by lower case letters
def text_match(text):
    patterns = '^([A-Z][a-z]+)$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))

# 8. Function that matches a string that has an a followed by anything,ending in b.
def text_match(text):
    patterns = '^a.b$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("acabbd"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))

# 9. Function that matches a word at the end of string, with optional punctuation
def text_match(text):
    patterns = '^.*[.,]$' # .* means any character 0 or more times  
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))

#10. Function that matches a word at the beginning of a string
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))

# 11. Function that matches a word at the end of a string, with optional punctuation
def text_match(text):
    patterns = '^.*[.,]$' # .* means any character 0 or more times  
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))





