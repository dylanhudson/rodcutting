
// Rod cutting algorithm
var n = 10;

var prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30];

var optimal_sub = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

var optimal_string = ["", "", "", "", "", "", "", "", "", "", ""];

var cost_per_cut = 0;

// initialize variables
// optimal_sub.map(function() {
//   return 0;
// });
//
// optimal_string.map(function() {
//   return "";
// });

for(var j = 1; j <= n; j++) {
    var q = -10000000; //

    for(var i = 1; i <= j; i++) {
      var string = "";

      // build string visual
      for(var s = 1; s <= i; s++) {
        string = string + "-";
      }
      string = string + "|";

      if (q < prices[i] + optimal_sub[j-i]) {

        optimal_string[j] = string + optimal_string[j-i];

      }
      console.log(string + optimal_string[j-i] + "\n");

      if((j - i) == 0) {
        q = Math.max(q, (prices[i] + optimal_sub[j-i]));
      }
      else {
        q = Math.max(q, (prices[i] + optimal_sub[j-i] - cost_per_cut));
      }

      console.log(prices[i] + optimal_sub[j-i]);

    }

    console.log("\n * ");
    optimal_sub[j] = q;
}

console.log(optimal_sub[n]);
