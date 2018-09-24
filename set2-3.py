mai = int(input())
if mai > 1:
    for i in range(2, mai):
        if (mai % i) == 0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
