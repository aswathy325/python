if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if(n>=2 and n<=10):
        avg=0
        marks=[]
        marks=student_marks[query_name]
        l=len(marks)
        m=sum(marks)
        s=(m/l)
        su=format(s,".2f")
        print(su)
