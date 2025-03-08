maxprof=0
minso=float('inf')
price=[215,265,250,200,240,260,230]
for i in price:
    minso=min(minso,i)
    maxprof=max(maxprof,i-minso)
print(maxprof)
    
