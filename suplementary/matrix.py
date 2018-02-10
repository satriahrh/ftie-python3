def mul_gf(matrix_a, matrix_b, n):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError(
            "The number of matrix_a's column and the number of matrix_b's column is not matched"
        )

    matrix_return = [
        [0 for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))
    ]

    for i in range(len(matrix_a)):
        # iterate through columns of matrix_b
        for j in range(len(matrix_b[0])):
            # iterate through rows of matrix_b
            for k in range(len(matrix_b)):
                matrix_return[i][j] = (
                    matrix_return[i][j]
                    + (matrix_a[i][k] * matrix_b[k][j])
                    % n
                ) % n

    return matrix_return
