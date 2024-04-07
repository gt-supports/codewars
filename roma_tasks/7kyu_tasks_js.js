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

//https://www.codewars.com/kata/597d75744f4190857a00008d/train/javascript
const paintLetterboxes = function (start, end) {
    // Your code here
    const arr = Array(10).fill(0);

    for (let i = start; i <= end; i++) {
        let numStr = i.toString();

        for (let j = 0; j <= numStr.length; j++) {
            arr[parseInt(numStr[j])] += 1
        }
    }
    return arr
}

// https://www.codewars.com/kata/557af4c6169ac832300000ba/train/javascript
function removeRotten(bagOfFruits) {
    return bagOfFruits && bagOfFruits.length > 0 ? bagOfFruits.map(el => el.slice(0, 6) == 'rotten'
        ? (el.slice(6)).toLowerCase() : el) : []
}