def mul_gf(A, B, n):
    if len(A[0]) != len(B):
        raise ValueError("The number of A's column and the number of B's column is not matched")

    C = [
        [0 for j in range(len(B[0]))] for i in range(len(A))
    ]

    for i in range(len(A)):
        # iterate through columns of B
        for j in range(len(B[0])):
            # iterate through rows of B
            for k in range(len(B)):
                C[i][j] = (C[i][j] + (A[i][k] * B[k][j]) % n) % n

    return C
