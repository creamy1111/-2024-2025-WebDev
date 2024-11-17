// function checkPasswords() {
//     const password = document.getElementById('password').value;
//     const confirmPassword = document.getElementById('confirm-password').value;
  
//     if (password === confirmPassword) {
//       alert('Passwords match! Form submitted successfully.');
//       // You can call form submission logic here
//       document.getElementById('signup-form').submit();
//     } else {
//       alert('Passwords do not match. Please try again.');
//     }
//   }

const checkPwdMatch = function() {
	if (
		document.getElementById("pwd").value == 
		document.getElementById("pwd-retype").value
	) {
		alert("Match");
	} else {
		alert("Not match");
	}
};

document.getElementById("submit").addEventListener("click", checkPwdMatch);
  