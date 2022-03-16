"""
today's question 


Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in the array.

Example 
n = 10
queries = [[1,5,3], [4,8,7], [6,9,1]]

queries are interpreted as follows 
        a b k
        1 5 3
        4 8 7
        6 9 1

index->	 1 2 3  4  5 6 7 8 9 10
        [0,0,0, 0, 0,0,0,0,0, 0]
        [3,3,3, 3, 3,0,0,0,0, 0]
        [3,3,3,10,10,7,7,7,0, 0]
        [3,3,3,10,10,8,8,8,1, 0]

Output   10
"""

n = input().split()
print(n)
queries = []
for k in range(0,int(n[1])):
    queries.append(input().split())
i = 0
arr = [0] * int(n[0])
for j in queries:
    for x in range(int(j[i]-1), int(j[i+1])):
        arr[x] += j[i+2]
print(max(arr))