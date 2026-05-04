if __name__ == '__main__':
    n = int(input())
    result = [] 


    for _ in range(n):
        name = input()
        score = float(input())
        result.append([name, score]) 


    result.sort(key=lambda x: x[1])


    lowest_score = result[0][1]
    second_lowest_score = None
    
    for student in result:
        if student[1] > lowest_score:
            second_lowest_score = student[1]
            break 
    second_lowest_students = []
    for student in result:
        if student[1] == second_lowest_score:
            second_lowest_students.append(student[0])

    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)