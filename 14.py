def alphabeta(depth, index, alpha, beta, maximizingPlayer, values):
    if depth == 3:
        return values[index]

    if maximizingPlayer:
        maxEval = float('-inf')
        for i in range(2):
            eval = alphabeta(depth + 1, index * 2 + i, alpha, beta, False, values)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for i in range(2):
            eval = alphabeta(depth + 1, index * 2 + i, alpha, beta, True, values)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

values = [3, 5, 6, 9, 1, 2, 0, -1]
result = alphabeta(0, 0, float('-inf'), float('inf'), True, values)
print("Best value:", result)
