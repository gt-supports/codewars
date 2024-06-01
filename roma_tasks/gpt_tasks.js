// prompt for gpt: middle+ Можешь придумать задачу на JS для собеседования?
// Уровень middle+ (примерно на 50/100 по  сложности)

// 1 - 50
const data = [
    {name: 'John', age: 25, city: 'New York'},
    {name: 'Anna', age: 17, city: 'London'},
    {name: 'Mike', age: 18, city: 'Chicago'},
    {name: 'Sara', age: 20, city: 'Tokyo'}
];

const filterAndTransform = (data) => {
    return data.filter(man => man.age >= 18).map(man => {
        return {
            name: man.name,
            age: man.age
        }
    })
}

const result = filterAndTransform(data);
console.log(result);

// 2 - 50

const groupBy = (items, key) => {
    const obj = {};

    for (let i = 0; i < items.length; i++) {
        const groupKey = items[i][key];
        if (!obj[groupKey]) {
            obj[groupKey] = [];
        }
        obj[groupKey].push(items[i])
    }

    return obj
}

const data2 = [
    {id: 1, category: 'fruit', name: 'apple'},
    {id: 2, category: 'vegetable', name: 'carrot'},
    {id: 3, category: 'fruit', name: 'banana'},
    {id: 4, category: 'vegetable', name: 'potato'},
    {id: 5, category: 'fruit', name: 'orange'}
];

console.log(groupBy(data2, 'category'));