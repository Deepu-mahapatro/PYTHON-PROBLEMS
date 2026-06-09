#BOUNDARY METHOD

n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    #CREATE N*N MATRIX FILLED WITH 0
    matrix=[[0]* n for _ in range(n)]
    top=0
    bottom=n-1
    left=0
    right=n-1
    num=1
    while top<=bottom and left<=right:
        #LEFT->RIGHT
        for col in range(left,right+1):
            matrix[top][col]=num
            num+=1
        top+=1
        #TOP->BOTTOM
        for row in range(top,bottom+1):
            matrix[row][right]=num
            num+=1
        right-=1
        #RIGHT->LEFT
        if top<=bottom:
            for col in range(right,left-1,-1):
                matrix[bottom][col]=num
                num+=1
            bottom-=1
        #BOTTOM->TOP
        if left<=right:
            for row in range(bottom,top-1,-1):
                matrix[row][left]=num
                num+=1
            left+=1
    #PRINT MATRIX
    for i in matrix:
        print(*i)
        
#RECURSIVE SPILL METHOD
def spiral(matrix, top, bottom, left, right, num):
    if top > bottom or left > right:
        return num
    # LEFT->RIGHT
    for col in range(left, right + 1):
        matrix[top][col] = num
        num += 1
    # TOP->BOTTOM
    for row in range(top + 1, bottom + 1):
        matrix[row][right] = num
        num += 1
    #RIGHT->LEFT
    if top < bottom:
        for col in range(right - 1, left - 1, -1):
            matrix[bottom][col] = num
            num += 1
    #BOTTOM->TOP
    if left < right:
        for row in range(bottom - 1, top, -1):
            matrix[row][left] = num
            num += 1
    return spiral(
        matrix,
        top + 1,
        bottom - 1,
        left + 1,
        right - 1,
        num
    )
n = 4
matrix = [[0] * n for _ in range(n)]
spiral(matrix, 0, n - 1, 0, n - 1, 1)
for row in matrix:
    print(*row)