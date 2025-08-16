import matplotlib.pyplot as plt

folder = "images/"
# -----------------------------
# Chart Functions
# -----------------------------
def generate_pie_chart(labels, values, title="Pie Chart", filename="pie.png"):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
    ax.set_title(title)
    plt.savefig(f'{folder}{filename}')
    plt.close()


def generate_bar_chart(labels, values, title="Bar Chart", filename="bar.png"):
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['skyblue', 'orange', 'green', 'purple'])
    ax.set_title(title)
    ax.set_ylabel("Values")
    plt.savefig(f'{folder}{filename}')
    plt.close()


def generate_line_chart(x, y, title="Line Chart", filename="line.png"):
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='purple')
    ax.set_title(title)
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    plt.savefig(f'{folder}{filename}')
    plt.close()


def generate_scatter_chart(x, y, title="Scatter Plot", filename="scatter.png"):
    fig, ax = plt.subplots()
    ax.scatter(x, y, c='red', alpha=0.7, edgecolors='black')
    ax.set_title(title)
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    plt.savefig(f'{folder}{filename}')
    plt.close()


def generate_multiple_charts(labels, values, filename="combined_charts.png"):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Pie chart
    axs[0].pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    axs[0].set_title("Pie Chart")

    # Bar chart
    axs[1].bar(labels, values, color=['blue', 'orange', 'green'])
    axs[1].set_title("Bar Chart")

    plt.tight_layout()
    plt.savefig(f'{folder}{filename}')
    plt.close()

