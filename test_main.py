# test_main.py 可以添加路径验证
import os

if __name__ == '__main__':
    print('Current working directory:', os.getcwd())
    os.makedirs("output", exist_ok=True)
    with open("output/test.txt", "w") as f:
        f.write("Hello World!")
    print("File created at:", os.path.abspath("test.txt"))