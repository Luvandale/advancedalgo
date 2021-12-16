
def find(N):
    # initialize a variable and set it zero
    sum=0
    # loop through the number and its consecutive numbers
    for i in range(1, N+1):
        sum=sum+i
    print(sum)
find(10)
find(10000)
find(1000000)
find(100000000)