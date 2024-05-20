//1 https://www.codewars.com/kata/514b92a657cdc65150000006/train/javascript

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


//2 https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/javascript
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

//3 https://www.codewars.com/kata/54da5a58ea159efa38000836/train/javascript
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

//4 https://www.codewars.com/kata/5264d2b162488dc400000001/train/javascript
function spinWords(string) {
    return string.split(' ').map(item => item.length >= 5 ? item.split('').reverse().join('') : item).join(' ')
}

//5 https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/javascript
function findOutlier(integers) {
    const oddInts = integers.filter(num => num % 2 !== 0)
    const evenInts = integers.filter(num => num % 2 === 0)
    return oddInts.length > evenInts.length ? evenInts[0] : oddInts[0]
}

//6 https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/javascript
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

//7 https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/javascript
function findUniq(arr) {
    return arr.find(item => arr.indexOf(item) === arr.lastIndexOf(item))
}

//8 https://www.codewars.com/kata/5208f99aee097e6552000148/train/javascript
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

//9 https://www.codewars.com/kata/54b724efac3d5402db00065e/train/javascript
decodeMorse = function (morseCode) {
    const morseCodeClean = morseCode.trim();

    const words = morseCodeClean.split('   ');

    return words.map(word =>
        word.split(' ').map(letter => MORSE_CODE[letter.trim()]).join('')
    ).join(' ');
}

//10 https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/javascript

function sortArray(array) {
    const oddSortedArr = array.filter(item => item % 2 !== 0).sort((a, b) => a - b);

    let oddIndex = 0;

    return array.map(item => item % 2 !== 0 ? oddSortedArr[oddIndex++] : item)
}

//11 https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/javascript
function towerBuilder(nFloors) {
    const finalArr = [];

    for (let i = 0; i < nFloors; i++) {
        const stars = i * 2 + 1;

        const spaces = nFloors - i - 1;

        let str = ' '.repeat(spaces) + '*'.repeat(stars) + ' '.repeat(spaces);

        finalArr.push(str)
    }

    return finalArr
}

//12 https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

function high(x) {
    const words = x.toLowerCase().split(' ');
    let maxSum = 0;
    let maxScoreIndex = 0;
    for (const index in words) {
        let sum = 0;
        for (const letter of words[index]) {
            sum += letter.charCodeAt(0) - 96;
        }
        if (sum > maxSum) {
            maxSum = sum;
            maxScoreIndex = index;
        }
    }
    return words[maxScoreIndex]
}

//13 https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/javascript

function deleteNth(arr, n) {
    const finalArr = [];
    for (const i in arr) {
        if (finalArr.filter(item => item === arr[i]).length === n) {
            continue
        } else {
            finalArr.push(arr[i])
        }
    }
    return finalArr
}

//14 https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/javascript

function count(string) {
    const map = {}
    for (const value of string) {
        if (value in map) {
            map[value] += 1;
        } else {
            map[value] = 1;
        }
    }
    return map;
}

// 15 https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

function inArray(array1, array2) {
    const finalArr = []
    for (const value1 of array1) {
        for (const value2 of array2) {
            if (value2.includes(value1)) {
                finalArr.push(value1)
            }
        }
    }
    return [...new Set(finalArr.sort())]
}

//16 https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python
function validBraces(braces) {
    const stack = [];

    const pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for (const brace of braces) {
        if (pairs[brace]) {
            stack.push(brace);
        } else {
            let last = stack.pop();
            if (brace !== pairs[last]) {
                return false;
            }
        }
    }

    return stack.length === 0;
}