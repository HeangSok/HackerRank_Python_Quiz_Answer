# Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Input Format

# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.


# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. 
# If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 
# Berry
# Harry

# Explanation 

# There are  students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# The lowest grade of 37.2 belongs to Tina. 
# The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

# Answer:

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    scores = set()
    for record in records:
        scores.add(record[1])
    scores = list(scores)
    sorted_scores = sorted(scores)
    
    names = []
    for record in records:
        if sorted_scores[1] in record:
            names.append(record[0])
    
    sorted_name = sorted(names)
    
    for i in sorted_name:
        print(i)
