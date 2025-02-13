import matplotlib.pyplot as plt
import os

project_dir = os.path.dirname(os.path.abspath(__file__))  # 适用于 Python 脚本
save_dir = os.path.join(project_dir, "Output")
save_path = os.path.join(save_dir, "sin_function.png")

def basicPractice():
    x = [1,2,3,4,5]
    y = [10,20,25,30,40]

    plt.plot(x, y, marker='o')
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Basic Line Plot")

    os.makedirs(save_dir, exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()


if __name__ == "__main__":
    basicPractice()