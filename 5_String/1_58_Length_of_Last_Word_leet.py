def lengthOfLastWord(s):
    letter = 0

    for i in range(len(s)-1, -1, -1):
        if s[i].isalpha() and s[i-1] == " ":
            letter += 1
            return letter
        elif s[i].isalpha():
            letter += 1

        elif s[i] == " ":
            letter = 0
    
    return letter

# "Hello World"  "   fly me   to   the moon  "
s = "luffy is still joyboy" 
res = lengthOfLastWord(s)
print(res)