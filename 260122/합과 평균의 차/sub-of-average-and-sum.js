const fs = require("fs");
const input = fs.readFileSync(0, 'utf-8').toString().trim().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

let hap = a + b + c;
let avg = (a + b + c)/3;
let d = hap - avg;

console.log(hap);
console.log(avg);
console.log(d);