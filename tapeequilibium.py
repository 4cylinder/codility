'''
A non-empty zero-indexed array A consisting of N integers is given. 

Array A represents numbers on a tape. Any integer P, such that 0 < P < N, 
splits this tape into two non-empty parts: 
A[0], A[1], ..., A[P − 1] and 
A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: 
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the 
first part and the sum of the second part.

For example, consider array A such that  
	A[0] = 3,  A[1] = 1,  A[2] = 2,  A[3] = 4,  A[4] = 3

We can split this tape in four places:
•	P = 1, difference = |3 − 10| = 7 
•	P = 2, difference = |4 − 9| = 5 
•	P = 3, difference = |6 − 7| = 1 
•	P = 4, difference = |10 − 3| = 7 

Write a function that, given a non-empty zero-indexed array A of N integers, 
returns the minimal difference that can be achieved.

In the previous example, the function should return 1.

Assume that N is an integer within the range [2..100,000], and that each element 
of array A is an integer within the range [−1,000..1,000].
Expected worst-case time complexity is O(N).
Expected worst-case space complexity is O(N), beyond input storage 
(not counting the storage required for input arguments).

'''

def solution(A):
    if len(A)==2:
        return abs(A[1]-A[0])
    sumLeft = A[0]
    sumRight = sum(A[1:])
    diff = abs(sumLeft-sumRight);
    
    for P in range(1,len(A)):
        diff = min(abs(sumLeft-sumRight),diff)
        sumLeft += A[P]
        sumRight -= A[P]
        if diff==0: return 0
    
    return diff