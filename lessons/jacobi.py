def jacobi(A, b, x0, tol=1e-3, max_iter=1000):
    n = len(A)
    x = x0.copy()

    for iter in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]

        residual = [b[i] - sum(A[i][j] * x_new[j] for j in range(n)) for i in range(n)]
        if all(abs(residual[i]) < tol for i in range(n)):
            print(f'The Jacobi method converges after {iter + 1} iteration')
            return x_new

        x = x_new
        print(f'Iteration {iter + 1}: {x}')

    print('The Jacobi method did not converge within the maximum number of iterations')
    return x


A = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]
b = [4, 7, 3]
x0 = [0, 0, 0]
solution = jacobi(A, b, x0)
print('Solution:', solution)
