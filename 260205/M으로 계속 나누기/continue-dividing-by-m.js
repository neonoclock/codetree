const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(" ");

let N = Number(input[0])
let M = Number(input[1])

while(N>0) {
    console.log(N)
    N= Math.floor(N/M)
}