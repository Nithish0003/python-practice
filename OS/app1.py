import os

# os.mkdir("D:\\vscode\\python-practice\\OS\\NewFolder")

data=os.walk("D:\\vscode\\python-practice\\")

for root, dirs, files in data:
    print(f"Directory: {root}")
    for direct in dirs:
        print(f"**{direct}**")
    for filename in files:
        print(f"--->{filename}")