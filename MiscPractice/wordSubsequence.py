def solution(string1, string2):
    i = 0
    j = 0
    while i < len(string1):
        letter = string1[i]
        while j < len(string2):
            
            letterComp = string2[j]
            if letter == letterComp: # found letter
                i+=1
                j+=1
                break
            j+=1
        
        if i == len(string1):
            return True
        if j == len(string2):
            return False
    return True