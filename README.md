# 2048-Game-The-Terminal-Way
Popular 2048 game built to be played entirely on terminal OOP way

**Objective**
Build 2048 game to be played entirely on terminal. Take user input. Give options. Keep track of win/losses.

**Why?** 
Why not! 
OOP + ASCII coding + and a fun game to boot. Why ever not.

**Choosing Alphabets over 2048**
Step 1: Replace numbers with alphabets, because they are tricky to handle in terminal. Imagine having to code both 2 and 2048 to occupy the same square space on terminal. That means the block size has to be 4 times that was the smallest block 2048. Terminals aren't big enough to display this.

Now alphabets can be coded to occupy exactly the same number of pixels vertically and horizontally. And the merge actions 2 + 2 = 4 will now become A + A = B.
And whats more, we can have 25, twice as many merges as 2048 game which only has 11 until we hit 2048. But fo rthe sake of this game we keep it to 11 merges, until we merge to the alphabet 'K'.

**Playing the game**
Make sure you have all three .py files are copied into the folder.
On your choice of terminal navigate to the folder and run alphamerge.py


**ASCII art**
There is some beatiful ASCII art on the internet. But I designed my own because I need very specific size, shape and coloring-optionality. It was also fun.
As we are using letters A-K we will design all of these and one dummy letter (Z) for blank boxes.
Chek the full list of characters and art in letters_art.py.

A:
"""
            
    ####    
   ##  ##   
  ##    ##  
  ########  
  ##    ##  
            
"""
B:
"""
            
  #######   
  ##    ##  
  #######   
  ##    ##  
  #######   
            
"""

**alphamerge.py**
This py file is the game start code. This has code blocks for initializing a user, gathering his/her preferences, initiazing a board and calling the board code.

This file also has the code block for terminating a game on win/loss depending on the available moved on the board as the play goes on.

**board.py**
This is where the magic happens. A board gets created, tiles are created and populated at random - the start will have two A's.
And print the board if the terminal along with instructions for game play.


And then user moves are captured as the user enters his/her choices: up, down, right, left.
For every move, we execute tile moves and merges and update the board.

The most fun part... once the moves are finished we print the board on to the terminal.

Tiles & Board:
Tile and Board classes were straight forward. Having done Galton’s box code in
the homework, this felt similar. Initially, I planned on deleting and adding new tile
instances whenever merges happened. And moving the same tile instance on the
Board to different positions when tiles slide across.
But I quickly realized, considering there are always fixed number of tiles, it is
simpler to update the value of the tile. So I decided to treat empty spaces on the board
as tiles with empty/dummy character (z). This meant I could initialize the requisite
number of tiles upfront at the time of board creation. I then added methods in the Tile
class to update the value of the tile letter when changes occured.
Moves:
Moves class was a fun one to code. Here, my aim was to keep the number of
lines of code as low as possible. I spent a fair amount of time playing around with
loops. At first it seemed too complex to do all the moves at a time. Once I started to see
board moves as confined changes within rows and columns, it fell into place. I could
breakdown the moves into slide all tiles first, merge where possible and slide all
again-row by row or column by column.
