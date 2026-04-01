class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for idx in range(len(board)):
            if not self.isValidGroup(board[idx]):
                print("invalid row " + str(idx) + ": "+str(board[idx]))
                return False
        
        cols = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                cols[j].append(board[i][j])

        for idx in range(len(cols)):
            if not self.isValidGroup(cols[idx]):
                print("invalid col " + str(idx) + ": "+str(cols[idx]))
                return False
        
        boxes = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i < 3 and j < 3:
                    boxes[0].append(board[i][j])
                elif i < 6 and j < 3:
                    boxes[1].append(board[i][j])
                elif i < 9 and j < 3:
                    boxes[2].append(board[i][j]) 
                elif i < 3 and j < 6:
                    boxes[3].append(board[i][j]) 
                elif i < 6 and j < 6:
                    boxes[4].append(board[i][j]) 
                elif i < 9 and j < 6:
                    boxes[5].append(board[i][j]) 
                elif i < 3 and j < 9:
                    boxes[6].append(board[i][j]) 
                elif i < 6 and j < 9:
                    boxes[7].append(board[i][j]) 
                elif i < 9 and j < 9:
                    boxes[8].append(board[i][j]) 

        for idx in range(len(boxes)):
            if not self.isValidGroup(boxes[idx]):
                print("invalid col " + str(idx) + ": "+str(boxes[idx]))
                return False

        return True

    def isValidGroup(self, group: List[str]) -> bool:
        nums = {}
        for num in group:
            if num == '.':
                continue
            if num in nums:
                return False
            else:
                nums[num] = True
        return True