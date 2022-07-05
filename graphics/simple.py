import random
from bokeh.plotting import figure, output_file, show


if __name__ == "__main__":
  output_file("simple.html")
  fig = figure()

  total_values = int(input("Which values do you want to graphic?"))
  x_vals = list(range(total_values))
  y_vals = list(range(random.randint(0, 100)))

  fig.line(x_vals, y_vals, line_width=1)
  show(fig)

