def sum_seq(n):
    result = (n*(n+1))/2
    return result

def sum_range(m,n):
    return sum_seq(n) - sum_seq(m-1) 