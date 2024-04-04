// https://www.codewars.com/kata/56853c44b295170b73000007/train/javascript

const isSquare = function (arr) {
    if (arr.length === 0) {
        return undefined
    }
    return arr.filter(num => Number.isInteger(Math.sqrt(num))).length == arr.length
}


// https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/solutions/javascript?filter=me&sort=best_practice&invalids=false
function rowWeights(array) {
    const team1 = array.reduce((sum, value, i) => i % 2 === 0 ? sum + value : sum, 0)
    const team2 = array.reduce((sum, value, i) => i % 2 !== 0 ? sum + value : sum, 0)
    return [team1, team2]
}