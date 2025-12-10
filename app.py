from flask import Flask, request, render_template

app = Flask(__name__)

# Calculation logic
def calculate(a, b, operation):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b if b != 0 else "Error: divide by zero"
        return "Invalid operation"
    except Exception as e:
        return f"Error: {e}"

# Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    a = b = operation = None

    if request.method == "POST":
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            operation = request.form.get("operation")
            result = calculate(a, b, operation)
        except ValueError:
            result = "Error: invalid input"
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result, a=a, b=b, operation=operation)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
