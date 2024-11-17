from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sort', methods=['GET'])
def sort_numbers():
    # Lấy tham số 'numbers' từ URL query
    numbers = request.args.get('numbers')
    
    if not numbers:
        return jsonify({"error": "No numbers provided"}), 400

    try:
        # Chuyển chuỗi các số ngăn cách bởi dấu phẩy thành danh sách các số nguyên
        numbers_list = [int(num) for num in numbers.split(',')]
        # Sắp xếp danh sách số
        sorted_numbers = sorted(numbers_list)
        # Trả về danh sách đã sắp xếp dưới dạng phản hồi JSON
        return jsonify({"sorted_numbers": sorted_numbers})
    
    except ValueError:
        return jsonify({"error": "Invalid input, please provide a list of numbers"}), 400

if __name__ == '__main__':
    app.run(debug=True)
