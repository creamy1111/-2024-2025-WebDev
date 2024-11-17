from flask import Flask
import math

app = Flask(__name__)

@app.route('/factorial/<int:number>')
def calculate_factorial(number):
    if number < 0:
        return f"Không thể tính giai thừa của số âm"
    result = math.factorial(number)
    return f"Giai thừa của {number} là: {result}"

if __name__ == '__main__':
    app.run(debug=True)