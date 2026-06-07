#ZIGZAG CONVERSION PATTERN
#CORE IDEA:
      #PLACE CHARACTERS ROW BY ROW
      #MOVE DOWNWARD FIRST
      #THEN MOVE UPWARD DIAGONALLY
      #REPEAT UNTIL ALL CHARACTERS
      #ARE PLACED
#EDGE CASES:
      #EMPTY STRING -> RETURN ""
      #NUM ROWS = 1 -> RETURN STRING
      #NUM ROWS >= LEN(S) -> RETURN STRING
#KEY OBSERVATION:
      #KEEP TRACK OF CURRENT ROW
      #MOVE DOWN UNTIL LAST ROW
      #MOVE UP UNTIL FIRST ROW
      #CHANGE DIRECTION AT
      #TOP AND BOTTOM ROWS
#APPROACH:
      #CREATE ROWS WITH EMPTY STRINGS
      #START FROM FIRST ROW
      #TRAVERSE EACH CHARACTER
      #ADD CHARACTER TO CURRENT ROW
      #CHANGE DIRECTION WHEN
      #TOP OR BOTTOM IS REACHED
      #JOIN ALL ROWS TO GET ANSWER
#MAIN LOGIC:
      #IF CURRENT_ROW == 0
      #MOVE DOWN
      #IF CURRENT_ROW == NUMROWS-1
      #MOVE UP
      #CURRENT_ROW += DIRECTION
#TIME COMPLEXITY:
      #O(N)
#SPACE COMPLEXITY:
      #O(N)
#CONCLUSION:
      #SIMULATE THE ZIGZAG MOVEMENT
      #USING CURRENT ROW AND
      #DIRECTION
      #STORE CHARACTERS IN ROWS
      #JOIN ALL ROWS TO FORM
      #THE FINAL STRING

#SIMPLE METHOD TO UNDERSTAND 
def covert(s,numRows):
    #NO ZIGZAG POSSIBLE
    if numRows<=1 or numRows>=len(s):
        return s
    #CREATE ROWS WITH EMPTY STRINGS
    rows=[""] * numRows
    #START FROM FIRST ROW
    current_row=0
    #DIRECTION :
    # -1 -> UPWARD
    #  1 -> DOWNWARD
    direction=1
    #TRAVERSE EACH CHARACTER
    for ch in s:
        #ADD CHARACTER TO CURRENT ROW
        rows[current_row]+=ch
        #CHANGE DIRECTION AT BOUNDARIES
        if current_row==0:
            direction=1
        elif current_row==numRows-1:
            direction=-1
        #MOVE TO NEXT ROW
        current_row+=direction
    #COMBINE ALL ROWS
    return "".join(rows)
s=input("enter a string")
numRows=int(input("enter a row number"))
result=covert(s,numRows)
print(result)