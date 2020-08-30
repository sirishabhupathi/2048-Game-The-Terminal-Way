import sys
import random
from termcolor import colored
import letters_art

upgrade_dict = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','z':'z'}
score_dict = {'a':4,'b':8,'c':16,'d':32,'e':64,'f':128,'g':256,'h':512,'i':1024,'j':2048,'z':0}
moves = {'l':'Left','r':'Right','u':'Up','d':'Down','q':'Quit'}
class Tile:
    """ Creates an instance for tiles on the board. With a specic alphabet value. 
        Has methods for upgrading when merge/clear and for fetching letter art for display.
    """
    def __init__(self,name, letter='a'):
        self.name = name
        self.letter = letter
        self.row_pos = 0
        self.col_pos = 0
    
    def get_letterart(self):
        self.art_text = str(letters_art.get_letterart_txt(self.letter))
        self.art_color = letters_art.get_letterart_col(self.letter)
        return [self.art_text,self.art_color]
    
    def upgrade(self):
        self.letter = upgrade_dict[self.letter]
    
    def clear(self):
        self.letter = 'z'
    
    def __str__(self):
        return str(self.art_text)

class Board:
    """ Creates an instance of game board after taking size and difficulty. Creates and slots in nxn tiles.
        Has methors/attributes for keeping track of scores, moves, game conditions.
        includes method for printing the board with letter art and colors as per tile attributes.
    """
    def __init__(self,name,size=4,difficulty='e'):
        self.name = name
        self.size = size
        self.difficulty = difficulty
        self.tiles = {}
        for i in range(size):
            for j in range(size):
                new_tile = Tile('T'+str(i)+str(j),'z')
                new_tile.row_pos = i
                new_tile.col_pos = j
                self.tiles['T'+str(i)+str(j)] = new_tile
        self.num_moves = 0
        self.score = 0
        self.last_move = '-'
        self.status = 'Play' #play/won/lost
        self.generate_tiles()
    
    def update_score(self,tile):
        self.score += score_dict[tile.letter]
    
    def empty_tiles(self):
        empty_tiles = [tile for tile in self.tiles.values() if tile.letter == 'z']
        return empty_tiles
    
    def generate_tiles(self):
        if self.difficulty == 'e':
            a_freq = 0.75
            b_freq = 0.25
            c_freq = 0
        elif self.difficulty == 'm':
            a_freq = 0.5
            b_freq = 0.5
            c_freq = 0
        elif self.difficulty == 'h':
            a_freq = 0.4
            b_freq = 0.3
            c_freq = 0.3
        
        if self.num_moves == 0:
            tiles_selected = random.sample(self.empty_tiles(),2)
            for tile in tiles_selected:
                tile.letter = 'a'
        else:
            tiles_selected = random.sample(self.empty_tiles(),1)
            for tile in tiles_selected:
                num = random.random()
                if num <= a_freq:
                    tile.letter = 'a'
                elif num <= a_freq + b_freq:
                    tile.letter = 'b'
                elif num <= a_freq + b_freq + c_freq:
                    tile.letter = 'c'
    
    def update_board_status(self,move_dir):
        if move_dir == 'q':
            self.status = 'Quit'
        elif self.board_win() == 'y':
            self.status = 'Won'
        elif self.board_movepossible() == 'n':
            self.status = 'Lost'
        else:
            self.status = 'Play'
    
    def board_win(self):
        win = 'n'
        for tile in self.tiles.values():
            if tile.letter == 'k':
                win = 'y'
        return win
    
    def board_movepossible(self):
        movespossible = 'n'
        for i in range(self.size):
            for j in range(self.size-1):
                if self.tiles['T'+str(i)+str(j)].letter == self.tiles['T'+str(i)+str(j+1)].letter or self.tiles['T'+str(j)+str(i)].letter == self.tiles['T'+str(j+1)+str(i)].letter:
                    movespossible = 'y'
        return movespossible

    def update_boardlastmove(self,move_dir):
        self.last_move = moves[move_dir]

    def print_board(self):
        width = self.size * 14 -2
        print()
        print('*' * width)
        print(' ' * int((width-24)/2),end='')
        print(colored('- A L P H A   M E R G E -', attrs=['bold']))
        print('*' * width)
        print('Game:',self.name.replace('B',''), '| Score:', self.score,'| Moves:', self.num_moves, '| Last Move:', self.last_move)
        tile_height = 8
        for i in range(self.size):
            for h in range(tile_height):
                for j in range(self.size):
                    line = self.tiles['T'+str(i)+str(j)].get_letterart()[0].split('\n')[h].rstrip('\n')
                    color = self.tiles['T'+str(i)+str(j)].get_letterart()[1][0]
                    color_bk = self.tiles['T'+str(i)+str(j)].get_letterart()[1][1]
                    for char in line:
                        if char ==" ":
                            print(colored(' ',color_bk,'on_'+color_bk),  end='')
                        elif char =='@':
                            print(colored(' '), end='')
                        else:
                            print(colored(' ', color,'on_'+ color), end='')
                    print('  ', end ='')

                print()
        print()
        print('(l)eft, (r)ight, (u)p, (d)own, (q)uit')

class Move:
    """ Takes in board and move direction and moves all the tiles as indicated.
        performance merge and slide operations and updates board status and scores.
    """
    def __init__(self,board,move_dir):
        self.move_dir = move_dir
        if self.move_dir in ('r','d'):
            self.jstart = board.size-1
            self.jend = -1
            self.jstep = -1
        else:
            self.jstart = 0
            self.jend = board.size
            self.jstep = 1
        self.slides = 0
        self.make_moves(board)
    
    def make_moves(self,board):
        if self.move_dir == 'q':
            exit
        else:
            self.slide_tiles(board)
            self.merge_tiles(board)
            self.slide_tiles(board)
        board.num_moves += 1
        board.update_board_status(self.move_dir)
        board.update_boardlastmove(self.move_dir)
        if board.status.lower() == 'play' and self.slides > 0:
            board.generate_tiles()
    
    def slide_tiles(self,board):
        for i in range(0,board.size):
            for j in range(self.jstart,self.jend,self.jstep):
                if self.move_dir in ('u','d'):
                    tile1 = board.tiles['T'+str(j)+str(i)]
                else:
                    tile1 = board.tiles['T'+str(i)+str(j)]
                if tile1.letter == 'z':
                    for k in range(j+self.jstep,self.jend,self.jstep):
                        if self.move_dir in ('u','d'):
                            tile2 = board.tiles['T'+str(k)+str(i)]
                        else:
                            tile2 = board.tiles['T'+str(i)+str(k)]
                        if tile2.letter != 'z':
                            tile1.letter = tile2.letter
                            tile2.clear()
                            self.slides = +1
                            break
    
    def merge_tiles(self,board):
        for i in range(0,board.size):
            for j in range(self.jstart,self.jend-self.jstep,self.jstep):
                if self.move_dir in ('u','d'):
                    tile1 = board.tiles['T'+str(j)+str(i)]
                    tile2 = board.tiles['T'+str(j+self.jstep)+str(i)]
                else:
                    tile1 = board.tiles['T'+str(i)+str(j)]
                    tile2 = board.tiles['T'+str(i)+str(j+self.jstep)]
                if tile1.letter == tile2.letter:
                    tile1.upgrade()
                    board.update_score(tile1)
                    tile2.clear()
    
    def move_quit(self, board):
        quit_check = str(input('Are you sure you want to quit? Y/N : ')).lower()
        if quit_check == 'y':
            board.update_board_status(self.move_dir)

