# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  scores. Store them in a list and find the score of the runner-up.

# Sample Input 
# n = 5
# arr = 2 3 6 6 5

# Sample Output 
  5
# Explanation 
# Given list is [2, 3, 6, 6, 5] . The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

# Answer:
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    arr = list(arr)
    new_arr = sorted(arr)
    print(new_arr[-2])
