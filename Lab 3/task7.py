from flask import Flask

app = Flask(__name__)

@app.route('/reverse/string/<input_string>', methods=['GET'])
def reverse_string(input_string):
    # Đảo ngược chuỗi
    reversed_string = input_string[::-1]
    # Trả về chuỗi đã đảo ngược
    return reversed_string

if __name__ == '__main__':
    app.run(debug=True)
    