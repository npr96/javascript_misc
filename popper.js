var array = [1,2,3,4,5]
function popper(){
	if (array.length % 2 === 0){
		return array.pop()
	}
	else{
		return array.shift()
	}
}

while(array.length > 0){
    console.log(popper(array))
}
