def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
        
    fibonacciSequence = [0, 1]
    for _ in range(2, n):
        next_num = fibonacciSequence[-1] + fibonacciSequence[-2]
        fibonacciSequence.append(next_num)
        
    return fibonacciSequence