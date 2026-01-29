const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();

let N = Number(input)

if (N>=90) {
    console.log("A")
} else if (N<90 && N>=80) {
    console.lod("B")
} else if (N<80 && N>=70) {
    console.lod("C")
} else if (N<70 && N>=60) {
    console.lod("D")
} else {
    console.log("F")
}