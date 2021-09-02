class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1.
        for row in board:
            seen_numbers = set()
            for num in row:
                if num.isnumeric():
                    if num in seen_numbers:
                        print('step 1 fail')
                        return False
                    else:
                        seen_numbers.add(num)
        #2.
        for column in range(9):
            seen_numbers = set()
            for index in range(9):
                num = board[index][column]
                print(num)
                if num.isnumeric():
                    if num in seen_numbers:
                        print('step 2 fail')
                        return False
                    else:
                        seen_numbers.add(num)
        #3.
        for sector in range (3):
            for quadrant in range (3):
                seen_numbers = set()
                for row in range (3):
                    for index in range (3):
                        num = board[row+sector*3][index+quadrant*3]
                        if num.isnumeric():
                            if num in seen_numbers:
                                print('step 3 fail')
                                return False
                            else:
                                seen_numbers.add(num)
        return True
