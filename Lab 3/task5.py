from flask import Flask

app = Flask(__name__)

def is_prime(n):
    # Kiểm tra số âm, 0 và 1
    if n < 2:
        return False
    
    # Kiểm tra số 2 - số nguyên tố nhỏ nhất
    if n == 2:
        return True
    
    # Kiểm tra số chẵn lớn hơn 2
    if n > 2 and n % 2 == 0:
        return False
    
    # Kiểm tra các số lẻ từ 3 đến căn bậc hai của n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

@app.route('/is_prime/<int:number>')
def check_prime(number):
    if is_prime(number):
        return f"{number} là số nguyên tố"
    else:
        return f"{number} không phải là số nguyên tố"

if __name__ == '__main__':
    app.run(debug=True)