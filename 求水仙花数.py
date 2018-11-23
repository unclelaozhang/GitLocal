# for x in range(100, 1000):
#     bai = x // 100
#     shi = x % 100 // 10
#     ge = x % 10
#     if x == bai**3 + shi**3 + ge**3:
#         # print(x)

for x in range(100, 1000):
    s = str(x)
    bai = int(s[0])
    shi = int(s[1])
    ge  = int(s[2])

    if x == bai**3 + shi**3 + ge**3:
        print(x)