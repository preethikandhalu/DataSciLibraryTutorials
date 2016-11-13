"""
REFERENCE
https://developers.google.com/edu/python/regular-expressions
https://www.debuggex.com/cheatsheet/regex/python
LOOK AT REFERENCES FOR PATTERNS!

Regular expressions are a powerful language for matching text patterns

"""
import re

def found(match):
    if match:
        x= 'found ' + match.group()
        return x
    else:
        x='did not find'
        return x

#f the search is successful,search() returns a match object. None otherwise


#The 'r' at the start of the pattern string designates a python "raw" string
#which passes through backslashes without change which is very handy for
#regular expressions. USE AT ALL TIMES!

######################BASIC EXAMPLES
#search for 'word' followed by a 3 letter word
stri = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', stri)
print found(match)

#search for 'iii' in 'piiig'
match = re.search(r'iig', 'piiig')
print found(match)

#search for 'igs' in 'piiig'
match = re.search(r'igs', 'piiig')
print found(match)

# . = any char but \n
match = re.search(r'..g', 'piiig')
print found(match)

# \d = 1 digit chat and \w=1 word (a-zA-Z0-9_) char
match = re.search(r'\d\d\d', 'p123g')
print found(match)

match = re.search(r'\w\w\w', '@@abcd!!')
print found(match)

#####################REPETITION EXAMPLES
# i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig')
print found(match)

# Finds the first/leftmost solution, and within it drives the +
# as far as possible (aka 'LEFTMOST AND LARGEST').
# In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii')
print found(match)

# \s* = zero or more whitespace chars
# Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print found(match)

match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')
print found(match)

match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print found(match)

# ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar')
print found(match)

#but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar')
print found(match)

#succeeds in this case
match = re.search(r'^b\w+', 'bsdf')
print found(match)


########################EMAILS EXAMPLE
stri = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', stri)
print found(match)

#search doesn't get the whole email add though
#no take care of '-' or '.' though
match = re.search(r'[\w-]+@[\w.]+', stri)
print found(match)

#########################GROUP EXTRACTION
#The "group" feature of a regular expression allows you to pick
#out parts of the matching text.
#Ex: add parenthesis ( ) around the username and host in the pattern,
#like this: r'([\w.-]+)@([\w.-]+)'
#match.group(1)= 1st left parenthesis text
#match.group(2)= 2nd left parenthesis text
#match.group() = whole match text as usual
print "\nGROUP EXTRACTION"
match = re.search(r'([\w.-]+)@([\w.-]+)', stri)
if match:
    print match.group()
    print match.group(1)
    print match.group(2)

########################FINDALL
#findall() finds *all* the matches and returns a list
stri = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w\.-]+@[\w\.-]+',stri)
print "\nEMAILS"
for email in emails:
    print email

########################FINDALL AND GROUPS
#The parenthesis ( ) group mechanism can be combined with findall().
#If the pattern includes 2 or more parenthesis groups, then
#instead of returning a list of strings, findall() returns a list of *tuples*.    
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', stri)
print tuples

########################OPTIONS
"""
options to modify behavior of pattern match
Ex: re.search(pat, str, re.IGNORECASE)
Can be used with findall as well
IGNORECASE
DOTALL (considers new lines as well)
MULTILINE - Within a string made of many lines, allow ^ and $ to match the
            start and end of each line. Normally ^/$ would just match the
            start and end of the whole string.
"""

######################GREEDY VS. NON-GREEDY
"""
Suppose you have text with tags in it: <b>foo</b> and <i>so on</i>

Suppose you are trying to match each tag with the pattern '(<.*>)'

The result is a little surprising, but the greedy aspect of the .* causes it
to match the whole '<b>foo</b> and <i>so on</i>' as one big match.
The problem is that the .* goes as far as is it can, instead of stopping at
the first > (aka it is "greedy").

There is an extension to regular expression where you add a ? at the end,
such as .*? or .+?, changing them to be non-greedy. Now they stop as soon as
they can. So the pattern '(<.*?>)' will get just '<b>' as the first match,
and '</b>' as the second match
"""

##########################SUBSTITUTION
"""
The re.sub(pat, replacement, str) function searches for all the instances
of pattern in the given string, and replaces them. The replacement string
can include '\1', '\2' which refer to the text from group(1), group(2), and
so on from the original matching text.
"""
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
