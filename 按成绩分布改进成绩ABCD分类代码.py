score = int(input('please enter your score here:'))
if 60 <= score <=80:
    print('C')
elif 0 <= score < 60:
    print("D")
elif 80 <= score < 90:
    print("B")
elif 90 <= score <= 100:
    print("A")
else:
    print("Error input")

