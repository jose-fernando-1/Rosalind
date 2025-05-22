def needleman_wunsch(seq1: str, seq2: str) -> tuple[str, str, int]:
    match = 1
    mismatch = -1
    gap = -2

    n, m = len(seq1), len(seq2)
    #Dinamic programming matrix
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    #Initializing
    for i in range(n+1):
        dp[i][0] = i * gap
    for j in range(m+1):
        dp[0][j] = j * gap

    #Filling the matrix
    for i in range(1, n+1):
        for j in range(1, m+1):
            if seq1[i-1] == seq2[j-1]:
                score = match
            else:
                score = mismatch
            dp[i][j] = max(dp[i-1][j-1] + score, dp[i-1][j] + gap, dp[i][j-1] + gap)
    best_score = dp[n][m]

    #Backtracking
    i, j = n, m
    alignment1, alignment2 = "", ""
    while i > 0 or j > 0:
        current = dp[i][j]
        if i > 0 and j > 0 and (current == dp[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)):
            alignment1 = seq1[i-1] + alignment1
            alignment2 = seq2[j-1] + alignment2
            i -= 1
            j -= 1
        elif i > 0 and current == dp[i-1][j] + gap:
            alignment1 = seq1[i-1] + alignment1
            alignment2 = "-" + alignment2
            i -= 1
        else:
            alignment1 = "-" + alignment1
            alignment2 = seq2[j-1] + alignment2
            j -= 1
    return alignment1, alignment2, best_score