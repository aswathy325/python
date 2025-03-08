if __name__ == '__main__':
    N = int(input())
    lists=[]
    for i in range(N):
        row=input().split(' ')
        if row[0]=='insert':
            lists.insert(int(row[1]),int(row[2]))
        elif row[0]=='print':
            print(lists)
        elif row[0]=='remove':
            lists.remove(int(row[1]))
        elif row[0]=='append':
            lists.append(int(row[1]))
        elif row[0]=='sort':
            lists.sort()
        elif row[0]=='pop':
            lists.pop() 
        else:
            lists.reverse()               
