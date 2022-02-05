# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal

# Sample Input 0
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output 0
# 56.00

# Sample Input 1
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh

# Sample Output 1
# 26.50

# Answer: 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() # *line means take everything what is not taken
        scores = list(map(float, line)) # map iterate through a sequence and transform in to a float
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        score = student_marks.get(query_name)
        average_score = sum(score) / len(score)
        print("%.2f" % average_score)
