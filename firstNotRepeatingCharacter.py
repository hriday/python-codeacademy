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



def firstNotRepeatingCharacter(s):
    slen = len(s)
    k = []
    l = ''
    chosen = "_"
    x = 0
    m = 0
    if slen == 1:
        chosen = s
        return (chosen)
    else:  
        for i in range (1,slen+1):
           k.append(s[i-1:i:1])
        for j in range (0,slen-1):
            print ("searching for " + k[j] + " from " + k[j+1])
            x = s.find(k[j],j+1)
            if (x>0):
                l += str(k[j])
            print (x)
            print (j+1)
            print (slen-1)
            if ((l.find(k[j]) == -1) & (x == -1)):
                print (k[j])
                return (k[j])
    return (chosen)
