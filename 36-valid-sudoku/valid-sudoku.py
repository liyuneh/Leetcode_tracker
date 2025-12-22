class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        as_it_is = True
        for i in range(len(board)):
            count1 = board[i].count(".")
            if len(set(board[i])) != len(board[i]) - count1 + 1:
                as_it_is = False
                break
        transpose = []
        for j in range(len(board[0])):
            ans = []
            for i in range(len(board)):
                ans.append(board[i][j])
            transpose.append(ans)
        transposed = True
        for i in range(len(transpose)):
            count1 = transpose[i].count(".")
            if len(set(transpose[i])) !=len(transpose[i])- count1 + 1:
                transposed = False
                break
        def get_all_subboxes(board):
            sub_boxes = []

            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    box = []
                    for i in range(3):
                        for j in range(3):
                            box.append(board[box_row + i][box_col + j])
                    sub_boxes.append(box)
            return sub_boxes
        ans = get_all_subboxes(board)
        sub_boxes = True
        for i in range(len(ans)):
            count1 = ans[i].count(".")
            if len(set(ans[i])) != len(ans[i]) - count1 + 1:
                sub_boxes = False
                break
        return as_it_is and transposed and sub_boxes