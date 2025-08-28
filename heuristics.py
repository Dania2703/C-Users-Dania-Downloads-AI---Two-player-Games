def base_heuristic(curr_state):
    board = curr_state.get_grid()
    max_length = 5
    score_player1 = total_player_score(board,max_length,1)
    score_player2 = total_player_score(board,max_length,2)
    return score_player1 - score_player2


def total_player_score(board,max_length,player_id):
    """
        Calculates the total heuristic score for a given player by analyzing beneficial sequences on the board.
    """
    directions = [
        (0, 1),  # Horizontal
        (1, 0),  # Vertical
        (1, 1),  # Diagonal (Top-Left to Bottom-Right)
        (1, -1)  # Diagonal (Top-Right to Bottom-Left)
    ]
    seen = set()
    total_score = 0
    n,m=board.shape

    for row in range(n):
        for col in range(m):
            if board[row, col] == player_id:
                for dir_x,   dir_y in directions:
                    if (row, col, dir_x, dir_y) not in seen:
                        seq_length, open_ends = search(board,seen, row, col, dir_x, dir_y, player_id,max_length)
                        if seq_length == 4 and open_ends > 0:
                            total_score += 1
                        elif seq_length == 3 and open_ends == 2:
                            total_score += 1

    return total_score


def search(board,seen, start_x, start_y, dir_x, dir_y, player_id,max_length):
    """
    search for sequence starting from a specific position and direction to calculate its length and open ends.
    """
    n, m = board.shape
    seq_len = 1
    open_ends = [False, False]  # [open_start, open_end]
    path = [(start_x, start_y)]

    # Forward direction
    for step in range(1, max_length):
        move_x = start_x + step * dir_x
        move_y =  start_y + step * dir_y
        if 0 <= move_x < n and 0 <= move_y < m:
            if board[move_x, move_y] == player_id:
                seq_len += 1
                path.append((move_x, move_y))
            elif board[move_x, move_y] == 0:
                open_ends[1] = True
                break
            else:
                break
        else:
            break

    for step in range(1, max_length):
        prev_x, prev_y = start_x - step * dir_x, start_y - step * dir_y
        if 0 <= prev_x < n and 0 <= prev_y < m:
            if board[prev_x, prev_y] == player_id:
                seq_len += 1
                path.append((prev_x, prev_y))
            elif board[prev_x, prev_y] == 0:
                open_ends[0] = True
                break
            else:
                break
        else:
            break

    for p in path:
        seen.add((p[0], p[1], dir_x, dir_y))

    return seq_len, sum(open_ends)





def advanced_heuristic(curr_state):
    """
        Calculates a more advanced heuristic score by combining beneficial sequences
    """
    board = curr_state.get_grid()
    max_length = 5
    score_player1 = (
            total_player_score(board,max_length,1)
            + center_control(board,1)
            + potential_threats(board,1)
    )

    score_player2 = (
            total_player_score(board,max_length,2)
            + center_control(board,2)
            + potential_threats(board,2)
    )

    return score_player1 - score_player2


def center_control(board,player_id):
    """
    Rewards a player for controlling the central columns of the board.
    """
    center_col = board.shape[1] // 2
    center_score = 0

    for row in range(board.shape[0]):
        if board[row, center_col] == player_id:
            center_score += 3
        if board.shape[1] % 2 == 0 and board[row, center_col - 1] == player_id:
            center_score += 3

    return center_score

def potential_threats(board,player_id):
    """
    Penalizes a player for allowing potential threats by the opponent.
    """
    opponent_id = 1 if player_id == 2 else 2
    threat_score = 0

    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if board[row, col] == opponent_id:
                for dir_x, dir_y in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                    seq_length, open_ends = search(board, set(),row, col, dir_x, dir_y, opponent_id,5)
                    if seq_length == 3 and open_ends == 2:
                        threat_score -= 5

    return threat_score
