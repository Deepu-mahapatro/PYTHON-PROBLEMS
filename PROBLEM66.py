#PASCAL'S TRIANGLE PATTERN
#CORE IDEA:
      #EACH ROW STARTS AND ENDS WITH 1
      #MIDDLE ELEMENTS ARE THE SUM
      #OF TWO ELEMENTS FROM THE
      #PREVIOUS ROW
#EDGE CASES:
      #N <= 0 -> RETURN EMPTY LIST
      #N = 1 -> [[1]]
#KEY OBSERVATION:
      #FIRST ELEMENT = 1
      #LAST ELEMENT = 1
      #MIDDLE = UPPER_LEFT + UPPER_RIGHT
#APPROACH:
      #CREATE EMPTY TRIANGLE
      #GENERATE ROWS ONE BY ONE
      #FILL ROW WITH 1'S
      #CALCULATE MIDDLE ELEMENTS
      #USING PREVIOUS ROW
      #ADD ROW TO TRIANGLE
#MAIN FORMULA:
      #CURRENT_ROW[J]
      #=
      #PREVIOUS_ROW[J-1]
      #+
      #PREVIOUS_ROW[J]
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(N²)
#CONCLUSION:
      #BUILD ROWS USING THE
      #PREVIOUS ROW
      #FIRST AND LAST ARE 1
      #MIDDLE ELEMENTS ARE
      #SUMS OF ADJACENT VALUES

#USING ITERATIVE LOOP METHOD
def generate(num):
    if num<=0:
        return []
    triangle=[]
    #BUILD EACH ROW
    for i in range(num):
        #CREATE ROW FILLED WITH 1'S
        row=[1] * (i+1)
        #FILL MIDDLE VALUES
        for j in range(1,i):
            #UPPER_LEFT+UPPER_RIGHT
            row[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
    return triangle
num=int(input("enter a number"))
result=generate(num)
for i in result:
    print(i)
    
#USING NCR MATHEMATICAL METHOD
def generate(numRows):
    """
    Pascal Triangle using nCr
    """
    if numRows <= 0:
        return []
    triangle = []
    for n in range(numRows):
        row = []
        for r in range(n + 1):
            # Compute nCr
            value = 1
            for i in range(r):
                value = value * (n - i) // (i + 1)
            row.append(value)
        triangle.append(row)
    return triangle
numRows=int(input("enter a number"))
result=generate(numRows)
for i in result:
    print(i)