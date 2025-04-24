import random

class Grid:
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def make_grid(self, size):
        grid =[0 * size for i in range(size)]
        val = 1
        for i in range(size-1, -1, -1):
            for j in range(size):
                grid[i][j] = val
                val += 1

        print(grid)

    def invalidMove(self, player, grid, size, player_position):
        prev_pos = player_position[player][-1]
        player_position[player].append(prev_pos)
        print("Move is not Valid")

    def cutMove(self, prevPlayer, curPlayer, grid, size, player_position, score):
        player_position[prevPlayer].append(0)
        player_position[curPlayer].append(score)
        

    def move(self, score, grid, pos_row, pos_col, size, player, player_position):

        if((grid[pos_row][pos_col] + score) > size*size):
            self.invalidMove()

        sc_p = (grid[pos_row][pos_col] + score)
        if(sc_p in player_position[0]):
            self.cutMove(0, player, grid, size, player_position, sc_p)
        elif(sc_p in player_position[1]):
            self.cutMove(1,player, grid, size, player_position, sc_p)
        elif(sc_p in player_position[2]):
            self.cutMove(2,player, grid, size, player_position, sc_p)

        
        prev_pos = player_position[player][-1]
        player_position[player].append(prev_pos+score)

        if(prev_pos+score == size*size):
            print("WINNER player:", player)



if __name__ == "__main__":
    grid_size = int(input("Enter the grid size:"))
    board =Grid(3)
    player_count = 3
    player_position = [[]]*3
    print(player_position)
    board.make_grid(grid_size)
    while(True):
        dice_score = random.randrange(1, 6, 1)
        print(dice_score)
        for player in range(3):
            board.move(dice_score, grid_size, player, player_position)

 