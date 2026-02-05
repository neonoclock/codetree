const fs = require("fs")
let n = fs.readFileSync(0).toString().trim()

let result = "" // 결과를 누적할 빈 결과값 문자열

for (let i=0 ; i<8; i++) { // n을 8번
    result += n;
}

console.log(result) // 결과값 문자열 출력