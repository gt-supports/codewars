// https://www.codewars.com/kata/56853c44b295170b73000007/train/javascript

const isSquare = function (arr) {
    if (arr.length === 0) {
        return undefined
    }
    return arr.filter(num => Number.isInteger(Math.sqrt(num))).length == arr.length
}