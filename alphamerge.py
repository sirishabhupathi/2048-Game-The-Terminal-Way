"""
***************************************Instructions*************************************
Alpha merge is similar to 2048. Use keys (l/r/u/d) to move the tiles left/right/up/down. 
When two tiles with the same alphabet touch, they merge to form the next alphabet.
Your goal is to get to 'K'. Good luck!
****************************************************************************************
"""
import sys
from board import Board, Move


class User:
    """ Initializes an instance of user. Has method for collecting user preferences for the game.
        Has a dict attribute for keeping track of player history-boards, score.
    """
    def __init__(self, name):
        self.name = name
        self.num_boards = 0
        self.playhist = {}

    def start_board(self):
        if self.num_boards > 0:
            sameboard = str(input('Would you like to keep the same settings ' + str(self.cur_board.size) +'x'+str(self.cur_board.size)+'|('+self.cur_board.difficulty+ ') Y/N? : ')).lower()
            if sameboard == 'y':
                board_size = self.cur_board.size
                difficulty = self.cur_board.difficulty
            else:
                board_size, difficulty = self.get_board_choices()
        else:
            board_size, difficulty = self.get_board_choices()
        self.num_boards += 1
        self.cur_board = Board('B'+str(self.num_boards), board_size, difficulty)
        self.update_userplayhist()
        return self.cur_board

    def get_board_choices(self):
        board_size = str(input('Cool. What board would you like? 4x4(4) | 5x5(5) | 6x6(6) : '))
        while board_size not in ('4','5','6'):
            board_size = str(input("Aw! I don't have that board. How about: 4x4(4) | 5x5(5) | 6x6(6)? : "))
        print('Great. ',str(board_size),'x',board_size,' it is!') 
        difficulty = str(input('Choose difficulty level. easy(e) | medium(m) | hard(h) : ')).lower()
        while difficulty not in ('e','m','h'):
            difficulty = str(input("Sorry. Choose from these difficulty levels please. easy(e) | medium(m) | hard(h) : ")).lower()
        print('Lets play!')
        return int(board_size), difficulty
    
    def update_userplayhist(self):
        self.playhist[str(self.cur_board.name)] = [int(self.cur_board.score) , str(self.cur_board.status)]
    
    def print_userstats(self):
        scores = [self.playhist[key][0] for key in self.playhist.keys()]
        playstatus = [self.playhist[key][1] for key in self.playhist.keys()]
        print('Your stats : ')
        print('Games Played :', self.num_boards,' | Won : ', playstatus.count('Won'),' | Lost : ', playstatus.count('Lost'),' | Quit : ', playstatus.count('Quit'))
        print('Highest Score : ', max(scores), ' | Lowest Score : ', min(scores), ' | Avg Score : ', sum(scores)/len(scores))


def initialize_user():
    print('*******************************')
    print('   Welcome to "ALPHA MERGE!"   ')
    print('*******************************')
    username = str(input('Enter your username : '))
    print('Hi,',username, end=', ')
    input_instructions = str(input('Would you like instructions on how to play? (Y/N) : ')).lower()
    while input_instructions not in ('y','n'):
        input_instructions = str(input('Sorry, is that a yes(y) or no(n) on instructions?'))
    if input_instructions == 'y':
        print(__doc__)
    return username


def play(user):
    board = user.start_board()
    board.print_board()
    move_input = ''
    quit_check = ''
    while board.status.lower() == 'play':
        move_input = str('Available moves: l/r/u/d/q : ').lower()
        while move_input not in ('l','r','u','d','q'):
            move_input = input('Available moves: (l/r/u/d/q) : ')
        if move_input == 'q':
            quit_check = str(input('Are you sure you want to quit? Y/N : ')).lower()
            if quit_check == 'y':
                exit
            else:
                continue
        Move(board,move_input)
        board.print_board()
        user.update_userplayhist()
    if board.status == 'won':
        print('Congratulations. You won!!!')
    elif board.status == 'lost':
        print('Sorry. Better luck next game!')
    another_game = str(input('Would you like to play another game? ')).lower()
    if another_game == 'y':
        play(user)
    else:
        print('Thanks for playing,',user.name, '. See you again!')
    user.update_userplayhist()
    

username = initialize_user()
user = User(username)
play(user)
user.print_userstats()