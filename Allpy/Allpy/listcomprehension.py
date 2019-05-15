if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    myval =[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    if not([i,j,k] in myval):
                       myval.append([i,j,k])
    print((myval))

