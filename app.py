def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)  # BUG: float semantics; spec wants round-half-up int
