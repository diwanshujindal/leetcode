from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        #row
        rows=defaultdict(set)
        cols=defaultdict(set)
        subboxs=defaultdict(set)

        for row in range(9):
            for col in range(9):
                element=board[row][col]
                if element !='.':

                    if element in rows[row] or element in cols[col] or element in subboxs[(row//3,col//3)]:
                        return False
                    else:
                        rows[row].add(element)
                        cols[col].add(element)
                        subboxs[(row//3,col//3)].add(element)
        return True




        