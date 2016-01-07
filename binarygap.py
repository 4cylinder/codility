'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros 
that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 
and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of 
length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function: that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.

E.g., given N = 1041 the function should return 5, because N has binary representation 10000010001 
and so its longest binary gap is of length 5.

Assume that N is an integer within the range [1..2,147,483,647].

Expected worst-case time complexity is O(log(N)); Expected worst-case space complexity is O(1).
'''

def solution(N):
    if N<5: return 0
    bin = "{0:b}".format(N)
    left = 0
    right = len(bin)-1
    while left<right and not(bin[left]=='1' and bin[left+1]=='0'):
        left += 1
    while right > left and not(bin[right]=='1' and bin[right-1]=='0'):
        right -= 1
    gap = 0
    while left <= right:
        mid = (left+right)/2
        potential = 0
        hasOne = 0
        for i in range(left+1,right):
            if bin[i]=='1':
                hasOne = i
                break
        if hasOne:
            potential = hasOne-left-1
            gap = max(potential,gap)
            if hasOne <=mid:
                left = hasOne
            else:
                right = hasOne
        else:
            potential = right-left-1
            gap = max(potential,gap)
            return gap
    
    return gap
