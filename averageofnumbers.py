sum=0
n=int(input())
for i in range(n):
    m=int(input())
    sum=sum+m
average=sum/n
#averageround=round(average,2)
print("The average is: {:.2f}".format(average))
