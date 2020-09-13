const {evaluate, multiply, sum} = require('mathjs')

const ALFA = 1, BETA = 1, a = -1, b = 1, p = -1, q = 1, m = n = 1000;

function f_x(x) {
    return evaluate(`e^(i*${BETA}*${x})`);
}

function K_eps_x(eps, x) {
    return evaluate(`e^(-${ALFA} * abs(${x} + i*${eps}))`);
}
const h_x = (b - a) / n;
function x_k(k) {
    return a + k * h_x;
}

function findF_eps(eps) {
    // [0, 1, ..., n - 1]
    const kArray = Array.apply(null, {length: n - 1}).map(Number.call, Number);
    return kArray.reduce((prevSum, k) => {
        return sum(prevSum, multiply(K_eps_x(eps,x_k(k)), f_x(x_k(k)), h_x) )
    }, 0)
}

console.log(findF_eps(0))