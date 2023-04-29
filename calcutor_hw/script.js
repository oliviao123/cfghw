function calculateSum() {
  var num1 = document.getElementById("num1").value;
  var num2 = document.getElementById("num2").value;

  if (num1 && num2 && !isNaN(num1) && !isNaN(num2)) {
    var sum = parseFloat(num1) + parseFloat(num2);
    document.getElementById("result").innerHTML = "The sum is: " + sum;
  } else {
    document.getElementById("result").innerHTML = "Please enter valid numbers in both fields.";
  }
}

function isNumberKey(evt) {
  var charCode = (evt.which) ? evt.which : event.keyCode;
  if (charCode > 31 && (charCode < 48 || charCode > 57) && (charCode < 46 || charCode > 46)) {
    return false;
  }
  return true;
}
