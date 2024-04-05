import os

data=os.environ
# print(data)

for i in data:
    print(f"{i} : {data[i]}")