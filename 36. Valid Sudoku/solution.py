class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row_numbers = [set() for i in range(9)]
        seen_column_numbers = [set() for i in range(9)]
        for sector in range (3):
            for quadrant in range (3):
                seen_numbers = set()
                for row in range (3):
                    for index in range (3):
                        num = board[row+sector*3][index+quadrant*3]
                        cur_row = sector * 3 + row
                        column = index + quadrant * 3                        
                        if num.isnumeric():
                            if num in seen_row_numbers[cur_row]:
                                print('step 1 fail')
                                return False
                            else:
                                seen_row_numbers[cur_row].add(num)

                            if num in seen_column_numbers[column]:
                                print('step 2 fail')
                                return False
                            else:
                                seen_column_numbers[column].add(num)
                            
                            if num in seen_numbers:
                                print('step 3 fail')
                                return False
                            else:
                                seen_numbers.add(num)
        return True
