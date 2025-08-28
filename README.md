# Two-Player Game AI – Minimax, Alpha-Beta Pruning & Heuristics

This project implements classic **game tree search algorithms** (Minimax and Alpha-Beta pruning) along with **heuristic evaluation functions** for two-player, turn-based games such as Connect Four or similar board games.

## Overview
- **Minimax:** Explores the full game tree to find the optimal move assuming both players play perfectly.
- **Alpha-Beta Pruning:** An optimized version of Minimax that cuts off branches that cannot affect the final decision, making the search faster.
- **Heuristics:** When the game tree is too large to search fully, heuristics provide an approximate evaluation of non-terminal board states:
  - *Base heuristic* – counts sequences of length 3 or 4 that can lead to a win.
  - *Advanced heuristic* – combines sequence analysis, center control, and detection of potential threats.

## Applications
- Connect Four AI agents  
- General two-player turn-based board games  
- Teaching and experimenting with adversarial search  

## Requirements
- Python 3.8+  
- NumPy  

## Final Result
- Running **Alpha-Beta or Minimax** returns a numeric value (evaluation of the position) and the best move chosen for the current player.  
- Running **heuristics** returns an integer score showing how favorable the board is for one player over the other:  
  - Positive score = better for Player 1  
  - Negative score = better for Player 2  
  - Larger values = stronger advantage  
## License
-This project is open-source and available under the MIT License. 
