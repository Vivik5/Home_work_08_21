//Home Work #7

//https://www.codewars.com/kata/51f41b98e8f176e70d0002a8/train/javascript
sortme = function( names ){
    return names.sort()
}

//https://www.codewars.com/kata/56f3f6a82010832b02000f38/train/javascript
c="You're a"
function describeAge(age) {
    return age <= 12 ? c+"(n) kid"
        : age >= 13 && age <= 17 ? c+"(n) teenager"
            : age >= 18 && age <= 64 ? c+"(n) adult"
                : c+"(n) elderly"
}

function describeAge(a) {
    return `You're a(n) ${a <= 12 ? "kid": a <= 17 ? "teenager": a <= 64 ? "adult" : "elderly"}`
}
var describeAge=a=>`You're a(n) ${a<13?"kid":a<18?"teenager":a<65?"adult":"elderly"}`;

//https://www.codewars.com/kata/58d248c7012397a81800005c/train/javascript
var cubeChecker = function(volume, side){
    return Math.pow(side, 3) === volume && side > 0;
};

var cubeChecker = function(v, s){
    return s>0&&v==s*s*s;
};

//https://www.codewars.com/kata/568dc69683322417eb00002c/train/javascript
const tripleX = str => {
    let x = str.indexOf('x')
    return x > -1 && x === str.indexOf('xxx')
}

//https://www.codewars.com/kata/5704aea738428f4d30000914/train/javascript
function tripleTrouble(one, two, three) {
    var result = "";
    for (let i = 0; i < one.length; i++) {
        result += one.charAt(i) + two.charAt(i) + three.charAt(i);
    }
    return result;
}

//https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/javascript
function countBy(x, n) {
    var z = []
    for (var i = 1; i <= n; i++) {
        z.push(x* i);
    }
    return z
}

const countBy = (x, n) => Array.from({length: n}, (v, k) => (k + 1) * x)

//https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/javascript
function move (position, roll) {
    return position + roll * 2
}

const move = (p, r) => p + r * 2;


//Home Work #6

//www.codewars.com/kata/57356c55867b9b7a60000bd7/train/javascript
function basicOp(operation, value1, value2){
    if (operation == '+') return value1 + value2;
    if (operation == '-') return value1 - value2;
    if (operation == '*') return value1 * value2;
    if (operation == '/') return value1 / value2;
}
function basicOp(operation, value1, value2) {
    return eval(value1 + operation + value2);
}//короткий код

//www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/javascript
function expressionMatter(a, b, c) {
    let values = [
        a + b + c,
        a + b * c,
        (a + b) * c,
        a * b * c,
        a * b + c,
        a * (b + c)
    ];

    return Math.max(...values);
}
expressionMatter(2, 2, 2);  // 8
expressionMatter(1, 2, 3);  // 9
function expressionMatter(a, b, c) {
    return Math.max(a+b+c, a*b*c, (a+b)*c, a*(b+c));
}//короткий код

//www.codewars.com/kata/5772da22b89313a4d50012f7/train/javascript
function greet (name, owner) {
    return name === owner ? 'Hello boss' :  'Hello guest';
}

//www.codewars.com/kata/5772da22b89313a4d50012f7/train/javascript
function fixTheMeerkat(arr) {
    return arr.reverse();
}


//www.codewars.com/kata/55cbc3586671f6aa070000fb/train/javascript
function checkForFactor (base, factor) {
    if (base%factor==0){
        return true
    }
    else {
        return false
    }
}

function checkForFactor (base, factor) {
    return base % factor === 0;
}//короткий код

//www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/javascript
function century(year) {
    return Math.floor(year/100) + ((year%100) ? 1 : 0)
}