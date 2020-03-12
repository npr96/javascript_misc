
function average(array){
	summer = 0;
	for(var i in array){
		summer += array[i]/array.length;
	}
	return summer;
}
console.log (average([1,2,3,4,5,6]))
