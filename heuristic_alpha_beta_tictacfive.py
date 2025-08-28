import math
h = None

def alphabeta_max_h(current_game, _heuristic, depth=3):
    """
        Alpha-beta pruning algorithm for maximizing player.
    """
    global h
    h = _heuristic

    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None

    v = -math.inf
    best_move = None
    moves = current_game.get_moves()
    alpha = -math.inf
    beta = math.inf

    for move in moves:
        score, _ = alphabeta_min_h(move, _heuristic, depth - 1)
        if score > v:
            v = score
            best_move = move
        alpha = max(alpha, v)
        if alpha >= beta:
            break 

    return v, best_move

def alphabeta_min_h(current_game, _heuristic, depth=3):
    """
       Alpha-beta pruning algorithm for minimizing player.
   """
    global h
    h = _heuristic

    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None

    v = math.inf
    best_move = None
    moves = current_game.get_moves()
    alpha = -math.inf
    beta = math.inf

    for move in moves:
        score, _ = alphabeta_max_h(move, _heuristic, depth - 1)
        if score < v:
            v = score
            best_move = move
        beta = min(beta, v)
        if alpha >= beta:
            break  # Alpha cutoff

    return v, best_move

def maximin(current_game, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None

    v = -math.inf
    best_move = None
    moves = current_game.get_moves()

    for move in moves:
        mx, _ = minimax(move, depth - 1)
        if v < mx:
            v = mx
            best_move = move

    return v, best_move

def minimax(current_game, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None

    v = math.inf
    best_move = None
    moves = current_game.get_moves()

    for move in moves:
        mx, _ = maximin(move, depth - 1)
        if v > mx:
            v = mx
            best_move = move

    return v, best_move
