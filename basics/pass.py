#   for i in range(6):
#     if i==2:
#         pass         #skips the condition  
#     else:
#         print(i)
for i in range(6):
    if i==1:
        continue
    elif i==3 or i==4:
        break
    else:
        print(i)