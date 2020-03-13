const array1 = ['a', 'b', 'c'];
const array2 = ['1', '2', '3'];

let holder
combos = () =>{
    
    for(var i in array1){
	    for(var j in array2){
		    let addition = [array1[i], array2[j]]
		    var array3 = `[${holder}, [${addition}]]`
		    holder = `${holder}, [${addition}]`
	    }
    }
	return  `[${array3.slice(12)}`
}

console.log(combos());
