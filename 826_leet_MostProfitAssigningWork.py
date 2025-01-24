def maxProfitAssignment(difficulty, profit, worker):
    """
    :type difficulty: List[int]
    :type profit: List[int]
    :type worker: List[int]
    :rtype: int
    """
    """
     Time Complexity - O(n logn)
     Space Complexity - O(n)
    """
    pair_vals = zip(difficulty, profit)  # zip the difficulty and profit to easily identify
    pair_vals = sorted(pair_vals)
    worker = sorted(worker)
    i = 0  # start with index 0 in pair_vals zipped list to check each worker capability to work and find maximum
    Sum = 0  # Total maximum profit
    maxProfit = 0  # for check each difficulty's profit and to take maximum one
    for work in worker:
        while i < len(pair_vals) and work >= pair_vals[i][0]:
            maxProfit = max(maxProfit, pair_vals[i][1])
            i += 1  # increment until pair_vals[i] <= work to find all possible maximum profit
        Sum += maxProfit  # finally add the maximum one
    return Sum


Difficulty = list(map(int, input().rstrip().split()))
Profit = list(map(int, input().rstrip().split()))
Worker = list(map(int, input().rstrip().split()))
print(maxProfitAssignment(Difficulty, Profit, Worker))
