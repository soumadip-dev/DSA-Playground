n = 10

# for i in range(n,0, -1):
#     row = ""
#     for j in range(i):
#         row = row  + str(j + 1)
#     print(row)


# for i in range(n):
#     row = ""
#     toggle = 1
#     for j in range(i+1):
#         row = row + " "+ str(toggle)
#         if(toggle == 1):
#             toggle = 0
#         else:
#             toggle = 1
#     print(row)

toggle = 1
for i in range(n):
    row = ""
    for j in range(i + 1):
        row = row + " " + str(toggle)
        if toggle == 1:
            toggle = 0
        else:
            toggle = 1
    print(row)
