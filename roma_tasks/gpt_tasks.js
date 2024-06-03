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

// 3 - 50

const weatherData = [
    {date: '2024-01-01', temperature: 5, humidity: 85, precipitation: 2},
    {date: '2024-01-02', temperature: 6, humidity: 80, precipitation: 0},
    {date: '2024-01-03', temperature: 4, humidity: 78, precipitation: 5},
    {date: '2024-01-04', temperature: 7, humidity: 82, precipitation: 0},
    {date: '2024-01-05', temperature: 3, humidity: 90, precipitation: 1},
];

const getWeatherStats = (data) => {
    const totalDays = data.length;
    const obj = {};
    const avgTemperature = data.reduce((acc, item) => acc + item.temperature, 0) / totalDays;
    const avgHumidity = data.reduce((acc, item) => acc + item.humidity, 0) / totalDays;
    const avgPrecipitation = data.reduce((acc, item) => acc + item.precipitation, 0)
        / totalDays;
    const maxTemperature = Math.max(...data.map(day => day.temperature));
    const minTemperature = Math.min(...data.map(day => day.temperature));

    obj['avgTemperature'] = avgTemperature;
    obj['avgHumidity'] = avgHumidity;
    obj['avgPrecipitation'] = avgPrecipitation;
    obj['maxTemperature'] = maxTemperature;
    obj['minTemperature'] = minTemperature;

    return obj
}

const stats = getWeatherStats(weatherData);
console.log(stats);