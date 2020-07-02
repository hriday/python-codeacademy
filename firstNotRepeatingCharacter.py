# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
# If there is no such character, return '_'.
# Example

# For s = "abacabad", the output should be
# firstNotRepeatingCharacter(s) = 'c'.

# There are 2 non-repeating characters in the string: 'c' and 'd'. 
# Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# firstNotRepeatingCharacter(s) = '_'.

# There are no characters in this string that do not repeat. 

# Hriday : 2020/07/02

# first got the length and if it was only one character, I printed it.
# If not, I pushed the elements into and array because it was easier to work with than 
# a string. I compared the current element with all the future elements in the string.
# If there was a match, I recorded it in another string. In the end, if an element wasn't 
# matched in furute elements in the string, and there was to recond of it in the second string 
# used to record previously seen elements, we had the answer.

def firstNotRepeatingCharacter(s):
    slen = len(s)
    k = []
    l = ''
    chosen = "_"
    x = 0
    if slen == 1:
        chosen = s
        return (chosen)
    else:  
        for i in range (1,slen+1):
           k.append(s[i-1:i:1])
        for j in range (0,slen-1):
            x = s.find(k[j],j+1)
            if (x>0):
                l += str(k[j])
            if ((l.find(k[j]) == -1) & (x == -1)):
                print (k[j])
                return (k[j])
    return (chosen)
