import os

dir_path = os.path.join(os.getcwd())
[print(dir) for dir in os.listdir(dir_path)]
