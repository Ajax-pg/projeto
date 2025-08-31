from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None

    if request.method == "POST":
        try:
            x = float(request.form.get("x", 0))
            y = float(request.form.get("y", 0))
            resultado = x + y
        except ValueError:
            resultado = "Erro: insira apenas números"

    return render_template("home.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
