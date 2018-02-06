function processData(myArray) {
  // Find second largest element in array
  myArray.sort(function (a, b) {return a - b});

  var max = myArray[myArray.length - 1];
  for (i = myArray.length - 2; myArray[i] === max; i--) {
  }

  console.log(myArray[i]);
}


// HackerRank stuff starts here
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
  _input += input;
});

process.stdin.on("end", function () {
 processData(_input.split('\n')[1].split(' ').map(Number));
});
