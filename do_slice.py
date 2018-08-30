def trim(s):
    if s=='':
        return s
    
    low = 0
    high = len(s)-1
    while low<=high and s[low]==' ':
        low = low + 1
    
    while high>=0 and s[high]==' ':
        high = high - 1
        #print(high)
    high = high + 1
    if high<=low:
        s = ''
    else:
        s = s[low:high]
    return s