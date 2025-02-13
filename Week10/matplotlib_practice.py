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
    plt.close()

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
    plt.close()

def pieChart():
    categories = ["A", "B", "C", "D"]
    values = [3, 7, 1, 8]

    plt.figure(figsize=(6,6)) 
    plt.pie(values, labels=categories, autopct='%1.1f%%', colors=["skyblue", "lightcoral", "lightgreen", "gold"])
    plt.title("Pie Chart Example")

    save_path = os.path.join(save_dir, "pieChart.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

def scatterPlot():
    plt.figure()  
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    sizes = [20, 50, 80, 120, 150, 200, 250, 300, 350, 400] 
    colors = range(len(x))  

    plt.scatter(x, y, s=sizes, c=colors, cmap="viridis", alpha=0.7, edgecolors="k")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Scatter Plot Example")
    plt.colorbar(label="Point Index") 

    save_path = os.path.join(save_dir, "scatterPlot.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

if __name__ == "__main__":
    # basicPractice()
    # barChart()
    # pieChart()
    scatterPlot()