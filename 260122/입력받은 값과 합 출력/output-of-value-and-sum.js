const fs = require("fs")
const input = fs.readFileSync(0, 'utf-8').toString().trim().split(" ");

let A = Number(input[0]);
let B = Number(input[1]);
let C = A + B;

console.log(A, B, C);