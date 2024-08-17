if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l1=list(student_marks[query_name])
    add=sum(l1)
    res=add/len(l1)
    print('%.2f'%res)
