game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0], ]


def game_board(player=0,row=0,column=0):

    game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board(2,2,2)


