n = int(input("enter number of rows you want: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
#   output:
#   1
#   2 2
#   3 3 3
#   4 4 4 4
#   5 5 5 5 5