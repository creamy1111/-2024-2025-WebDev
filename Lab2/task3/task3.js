function checkOddEven() {
    // Khai báo biến để lưu kết quả
    let result = '';
    
    // Vòng lặp từ 1 đến 15
    for (let i = 1; i <= 15; i++) {
        // Kiểm tra số chẵn lẻ bằng toán tử modulo
        if (i % 2 === 0) {
            result += i + " is even\n";
        } else {
            result += i + " is odd\n"; 
        }
    }
    
    // In kết quả
    console.log(result);
}

// Gọi hàm để chạy chương trình
checkOddEven();