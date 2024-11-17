// Hàm chuyển từ Fahrenheit sang Celsius
function fahrenheitToCelsius(f) {
    return (f - 32) * 5 / 9;
  }
  
  // Hàm chuyển từ Celsius sang Fahrenheit
  function celsiusToFahrenheit(c) {
    return (c * 9 / 5) + 32;
  }
  
  // Sử dụng thử
  let fahrenheit = 100;
  let celsius = fahrenheitToCelsius(fahrenheit);
  console.log(`${fahrenheit}°F is equal to ${celsius.toFixed(2)}°C`);
  
  let celsiusVal = 37.78;
  let fahrenheitVal = celsiusToFahrenheit(celsiusVal);
  console.log(`${celsiusVal}°C is equal to ${fahrenheitVal.toFixed(2)}°F`);
  