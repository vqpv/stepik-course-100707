def get_rec_sum(n):
    if len(n) == 1:
        return n[0]
    return n[0] + get_rec_sum(n[1:])


nums = list(map(int, input().split()))

print(get_rec_sum(nums))
