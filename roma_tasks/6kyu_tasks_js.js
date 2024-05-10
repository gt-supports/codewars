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