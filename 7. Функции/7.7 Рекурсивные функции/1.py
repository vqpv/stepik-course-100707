N = int(input())

def get_rec_N(n):
    if n > 1:
        get_rec_N(n - 1)
    print(n)
