
const getAverage = arr => {
	const reducer = (total,currentValue) => total + currentValue;
	const sum = arr.reduce(reducer)/arr.length;
	return sum;
}

console.log(getAverage([1,2,3,4,5]));
