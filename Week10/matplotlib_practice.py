from turtle import color
import matplotlib.pyplot as plt
import os

project_dir = os.path.dirname(os.path.abspath(__file__))  # 适用于 Python 脚本
save_dir = os.path.join(project_dir, "Output")
os.makedirs(save_dir, exist_ok=True)

def basicPractice():
    x = [1,2,3,4,5]
    y = [10,20,25,30,40]

    plt.plot(x, y, marker='o')
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Basic Line Plot")

    save_path = os.path.join(save_dir, "basicPractice.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def barChart():
    categories = ["A", "B", "C", "D"]
    values = [3, 7, 1, 8]
    
    plt.bar(categories, values, color="skyblue")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Bar Chart Example")

    save_path = os.path.join(save_dir, "barChart.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def pieChart():
    categories = ["A", "B", "C", "D"]
    values = [3, 7, 1, 8]

    plt.figure(figsize=(6,6)) 
    plt.pie(values, labels=categories, autopct='%1.1f%%', colors=["skyblue", "lightcoral", "lightgreen", "gold"])
    plt.title("Pie Chart Example")

    save_path = os.path.join(save_dir, "pieChart.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # basicPractice()
    # barChart()
    pieChart()