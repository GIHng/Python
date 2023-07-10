cnt = 0
blank = ' '
star = '*'
N = 5


for i in range(1, N+1):
    cnt +=1
    if i==1 or i==N :
        print(blank * (N - i), star*i, sep='')
    else:
        print(blank * (N - i), star, blank * ((i-1)*2-1), star, sep='')
