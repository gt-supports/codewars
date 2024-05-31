// prompt for gpt: middle+ Можешь придумать задачу на JS для собеседования?
// Уровень middle+ (примерно на 50/100 по  сложности)

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

