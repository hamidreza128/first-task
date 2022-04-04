matrix = [ [1,0,1,0,1,1],
    [0,0,0,0,1,0],
    [0,1,1,0,1,1],
    [1,1,0,1,0,0],
    [1,0,1,1,1,0],
    [0,0,1,0,1,1]
    ]

for a in range(len(matrix)):
    for b in range(len(matrix[a])):
        mark = matrix[a][b]
        if mark == 0:
            continue
        else:
            if b<1 and a==0:
                if matrix[a][b+1] == 1 or matrix[a+1][b] == 1:
                    continue
                else:
                    matrix[a][b] = 0
            if b>4 and a==0:
                if matrix[a][b-1] == 1 or matrix[a+1][b] == 1:
                    continue
                else:
                    matrix[a][b] = 0
            if b<1 and a>4:
                if matrix[a-1][b] == 1 or matrix[a][b+1] == 1:
                    continue
                else:
                    matrix[a][b] = 0
            if b>4 and a>4:
                if matrix[a][b-1] == 1 or matrix[a-1][b] == 1:
                    continue
                else:
                    matrix[a][b] = 0
            if (b>0 and b<5)and(a==0):
                if matrix[a][b-1] == 1 or matrix[a][b+1] == 1 or matrix[a+1][b] == 1:
                    continue
                else:
                    matrix[a][b] = 0
            if (b==0)and (a>0 and a<5):
                if matrix[a-1][b] == 1 or matrix[a][b+1] == 1 or matrix[a+1][b] == 1:
                    continue
                else:
                    matrix[a][b] = 0
            if (b>0 and a<5)and(a == 5):
                if matrix[a-1][b] == 1 or matrix[a][b-1] == 1 or matrix[a][b+1] == 1:
                    continue
                else:
                    matrix[a][b] = 0
            if (b==5)and(a>0 and a<5):
                if matrix[a-1][b] == 1 and matrix[a][b-1] == 1 or matrix[a+1][b] == 1:
                    continue
                else:
                    matrix[a][b] = 0
            if (a<0 and a>5)and(b>0 and b<5):
                if matrix[a-1][b] == 1 or matrix[a][b-1] == 1 or matrix[a][b+1] == 1 or matrix[a+1][b]:
                    continue
                else:
                    matrix[a][b] = 0

print(matrix)