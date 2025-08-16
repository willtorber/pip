import json
import charts

# -----------------------------
# Main Script
# -----------------------------
def main():
    # Load data from JSON file
    with open("data.json", "r") as f:
        data = json.load(f)

    # Pie & Bar chart
    labels = data["categories"]
    values = data["values"]

    charts.generate_pie_chart(labels, values, title="Category Distribution", filename="pie.png")
    charts.generate_bar_chart(labels, values, title="Category Values", filename="bar.png")

    # Line chart
    x = data["line"]["x"]
    y = data["line"]["y"]
    charts.generate_line_chart(x, y, title="Line Example", filename="line.png")

    # Scatter chart
    x_scatter = data["scatter"]["x"]
    y_scatter = data["scatter"]["y"]
    charts.generate_scatter_chart(x_scatter, y_scatter, title="Scatter Example", filename="scatter.png")

    # Combined chart
    charts.generate_multiple_charts(labels, values, filename="combined_charts.png")


if __name__ == "__main__":
    main()
