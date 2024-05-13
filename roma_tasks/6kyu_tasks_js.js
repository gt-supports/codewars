//https://www.codewars.com/kata/514b92a657cdc65150000006/train/javascript

function solution(number) {
    let sum = 0;
    if (number < 0) return 0
    for (let i = 1; i < number; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i
        }
    }
    return sum
}


//https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/javascript
function likes(names) {
    if (names.length === 0) {
        return 'no one likes this'
    } else if (names.length === 1) {
        return `${names[0]} likes this`
    } else if (names.length === 2) {
        return `${names[0]} and ${names[1]} like this`
    } else if (names.length === 3) {
        return `${names[0]}, ${names[1]} and ${names[2]} like this`
    }
    return `${names[0]}, ${names[1]} and ${names.length - 2} others like this`
}

//https://www.codewars.com/kata/54da5a58ea159efa38000836/train/javascript
function findOdd(A) {
    const map = A.reduce((acc, cur) => {
        acc[cur] = cur in acc ? acc[cur] + 1 : 1
        return acc
    }, {})

    for (let key in map) {
        if (map[key] % 2 !== 0) {
            return Number(key)
        }
    }
}

//https://www.codewars.com/kata/5264d2b162488dc400000001/train/javascript
function spinWords(string) {
    return string.split(' ').map(item => item.length >= 5 ? item.split('').reverse().join('') : item).join(' ')
}

//https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/javascript
function findOutlier(integers) {
    const oddInts = integers.filter(num => num % 2 !== 0)
    const evenInts = integers.filter(num => num % 2 === 0)
    return oddInts.length > evenInts.length ? evenInts[0] : oddInts[0]
}

//https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/javascript
function isPangram(string) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'
    const strSet = new Set()

    string.split('').forEach(item => {
        if (alphabet.includes(item.toLowerCase())) {
            strSet.add(item.toLowerCase())
        }
    })
    return strSet.size === 26
}

//https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/javascript
function findUniq(arr) {
    return arr.find(item => arr.indexOf(item) === arr.lastIndexOf(item))
}

//https://www.codewars.com/kata/5208f99aee097e6552000148/train/javascript
function solution(string) {
    let result = '';
    for (let i = 0; i < string.length; i++) {
        if (string[i].toUpperCase() === string[i]) {
            result += ' ' + string[i]
        } else {
            result += string[i]
        }
    }
    return result
}