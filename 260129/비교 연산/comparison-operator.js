const fs = require("fs");
let N = fs.readFileSync(0).toString().trim().split(" ");


let A = Number(N[0]);
let B = Number(N[1]);

if (A>=B) {
    console.log("1")
} else {
    console.log("0")
}

if (A>B) {
    console.log("1")
} else {
    console.log("0")
}

if (B>=A) {
    console.log("1")
} else {
    console.log("0")
}

if (B>A) {
    console.log("1")
} else {
    console.log("0")
}

if (B===A) {
    console.log("1")
} else {
    console.log("0")
}

if (B!=A) {
    console.log("1")
} else {
    console.log("0")
}