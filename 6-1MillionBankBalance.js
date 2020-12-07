/*
MPMP6: The 1 Million Bank Balance puzzle
https://www.youtube.com/watch?v=ILrqPpLpwpE


Output:
    Max: 19 days
    (144, 154)
 */

function Fib() {
    this.cache = [0, 1, 1];
    this.get = function (n) {
        while (this.cache.length <= n) {
            this.cache.push(this.cache[this.cache.length - 1] + this.cache[this.cache.length - 2]);
        }
        return this.cache[n]
    }
}

var target = 1e6;
var max = 0;
var result = [null, null];
var m = null;

var fib = new Fib();
for (var days = 15; days < 31; days++) {
    let a = fib.get(days);
    let b = fib.get(days - 1);
    for (var x = 1; x < target; x++) {
        let y = (target - (a * x)) / b;
        if (y < 0) {
            break;
        }
        if (y % 1 == 0) {
            max = days;
            m = [x, y];
            result = m;
        }
    }
}

console.log("Max: " + max + " days");
console.log("(" + result.join(", ") + ")");
