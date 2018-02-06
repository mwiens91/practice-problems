function findDay(myDate) {
  // Return day for date myDate(MM/DD/YYYY)
  // Note that myDate contains the date in string format
  var date = new Date(myDate);

  var weekday = new Array(7);
  weekday[0] = "Sunday";
  weekday[1] = "Monday";
  weekday[2] = "Tuesday";
  weekday[3] = "Wednesday";
  weekday[4] = "Thursday";
  weekday[5] = "Friday";
  weekday[6] = "Saturday";

  console.log(weekday[date.getDay()]);
}

// tail starts here
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
  _input += input;
});

process.stdin.on("end", function () {
  var dates = _input.split('\n');

  for (var i = 0; i < dates.length - 1; i++) {
     findDay(dates[i]);
  }
});
