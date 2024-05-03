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

//https://www.codewars.com/kata/5558cc216a7a231ac9000022/solutions/javascript?filter=me&sort=best_practice&invalids=false
function duplicates(arr) {
    const map = new Map();
    const finalArr = [];

    for (const el of arr) {
        if (map.has(el)) {
            if (map.get(el) === 1) {
                finalArr.push(el);
            }
            map.set(el, map.get(el) + 1);
        } else {
            map.set(el, 1);
        }
    }

    return finalArr;
}

// https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/javascript
function wordsToMarks(string) {
    const alphabet = {
        a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, g: 7, h: 8,
        i: 9, j: 10, k: 11, l: 12, m: 13, n: 14, o: 15, p: 16,
        q: 17, r: 18, s: 19, t: 20, u: 21, v: 22, w: 23, x: 24,
        y: 25, z: 26
    };

    return Number(string.split('').reduce((acc, item) => acc + alphabet[item], 0))
}


//https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/javascript

function removeDuplicateWords(s) {
    return [...new Set(s.split(' '))].join(' ')
}


//https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/javascript

function adjacentElementsProduct(array) {
    const productArray = []
    for (i = 0; i < array.length - 1; i++) {
        productArray.push(array[i] * array[i + 1])
    }
    return Math.max(...productArray)
}

//https://www.codewars.com/kata/535474308bb336c9980006f2/train/javascript

const greet = function (name) {
    const newName = name.toLowerCase()
    return `Hello ${newName[0].toUpperCase() + newName.slice(1)}!`
};

//https://www.codewars.com/kata/59a8570b570190d313000037/train/javascript

function sumCubes(n) {
    let sum = 0
    for (let i = 1; i <= n; i++) {
        sum += i ** 3
    }
    return sum
}

//https://www.codewars.com/kata/58daa7617332e59593000006/train/javascript

function findLongest(numbers) {
    return numbers.reduce((largest, current) => {
        const largestDigits = largest.toString().length;
        const currentDigits = current.toString().length;

        if (currentDigits > largestDigits) {
            return current;
        } else {
            return largest;
        }
    });
}

//https://www.codewars.com/kata/57f759bb664021a30300007d/train/javascript

function switcheroo(x) {
    return x.split('').map(letter => {
        if (letter === 'a') {
            return 'b'
        } else if (letter === 'b') {
            return 'a'
        }
        return letter
    }).join('')
}

//https://www.codewars.com/kata/57eaec5608fed543d6000021/train/javascript

function divCon(x) {
    const sumNonString = x.reduce((acc, num) => {
        if (typeof num === 'number') {
            return acc + num
        }
        return acc
    }, 0)
    const sumStrings = x.reduce((acc, num) => {
        if (typeof num === 'string') {
            return acc + Number(num)
        }
        return acc
    }, 0)
    return sumNonString - sumStrings
}

//https://www.codewars.com/kata/5aa1bcda373c2eb596000112/train/javascript

function maxTriSum(numbers) {
    const newNums = [...new Set(numbers.sort((a, b) => b - a))]
    return newNums[0] + newNums[1] + newNums[2]
}