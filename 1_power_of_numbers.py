def pon(n, p):
    if p==0:
        return 1
    if n==0:
        return 0
    if p==1:
        return n
    small_output=n*pon(n, p-1)
    return small_output
a, b = input().split()
print(pon(int(a),int(b)))
