# https://www.codewars.com/kata/57b06f90e298a7b53d000a86

def queue_time(customers: list[int], n: int):
    if not customers:
        return 0
    if n == 1:
        return sum(customers)
    if len(customers) == 1:
        return customers[0]
    if len(customers) <= n:
        return max(customers)

    queue_, customers = customers[:n], customers[n:]
    for i in range(len(customers)):
        min_ = min(queue_)
        idx = queue_.index(min_)
        queue_[idx] += customers[i]

    return max(queue_)


if __name__ == "__main__":
    assert queue_time([], 1) == 0
    assert queue_time([5], 1) == 5
    assert queue_time([2], 5) == 2
    assert queue_time([1, 2, 3, 4, 5], 1) == 15
    assert queue_time([1, 2, 3, 4, 5], 100) == 5
    assert queue_time([2, 2, 3, 3, 4, 4], 2) == 9

    """
    def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
    
    def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)
    """
