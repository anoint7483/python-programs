# if __name__ == '__main__':
#     students = []
#     scores = []

#     for i in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#         scores.append(score)

#     # Remove duplicate scores (optional)
#     unique_scores = sorted(set(scores))
#     name.sort()
#     # Check if there are at least two unique scores
#     if len(unique_scores) >= 2:
#         # Find the second lowest score
#         second_lowest_score = unique_scores[1]

#         # Find and print the names associated with the second lowest score
#         for name, score in students:
#             if score == second_lowest_score:
#                 print(name)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    average = sum(student_marks[name])/3
    print(round(average,2))
    print(f"{average:.2f}")