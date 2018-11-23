# x, y, z = 6, 5, 4
# if x < y:
#     small = x
#     if z < small:
#         small = z
# elif y < z:
#     small = y
# else:
#     small = z
x, y, z = 6, 5, 4

small = x if (x < y and x < z) else (y if y < z else z )

print(small)