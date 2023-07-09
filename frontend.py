import sudoku
from flask import Flask, request, render_template, redirect
import config

app = Flask(__name__)

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        for i in range(N):
            for j in range(N):
                grid[i][j] = request.form.get(str(i) + str(j))

    #return f"<h1>{grid}</h2>"

    refresh()

    return render_template("index.html")

@app.route("/test")
def test():
    return f"<h1>{grid}</h2>"

@app.route("/result")
def result():
    sudoku.solve_sudoku(grid)
    return f"<h1>{grid}</h2>"

def refresh():
    # convert all of the values in grid to ints
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '':
                grid[i][j] = 0
            else:
                grid[i][j] = int(grid[i][j])


if __name__ == "__main__":
    N = 9
    grid =[[0 for x in range(N)]for y in range(N)]

    app.run(debug=True)