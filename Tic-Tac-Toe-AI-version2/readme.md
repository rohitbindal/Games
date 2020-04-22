# Tic Tac Toe AI:version-2

This application is almost similar to <a href="https://github.com/rohitbindal/Games/tree/master/Tic-Tac-Toe-AI-version1" target="blank_">version-1</a> except for a few updates.  

To play the game, type `$ python3 main.py` in shell.   
If the computer is set to go first, it might take a few moments to see the output.

### Updates:
1. Changed the **Minimax** algorithm to **Alpha-Beta Pruning**.  
2. Input handeling improved.  
3. The board is now in a separate file which can be used for other projects. Hence, I won't have to write it again.  


### References:
1. **Alpha Beta Pruning** is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player games (Tic-tac-toe, Chess, Go, etc.). It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes away branches that cannot possibly influence the final decision. (Yes, i copied it from Wikipedia).

2. **Learning Resource**: This video by Sebastian Lague: <a href="https://www.youtube.com/watch?v=l-hh51ncgDI" target="blank_">Algorithms Explained – minimax and alpha-beta pruning</a>
