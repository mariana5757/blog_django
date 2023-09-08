var boton = document.getElementById("boton");
boton.addEventListener("click", function(){
	//'https://jsonplaceholder.typicode.com/todos/1'

	alert("hola mundo")
	fetch('https://jsonplaceholder.typicode.com/posts/99',
	{
		method:'DELETE',
		
	}
	
	)
	.catch(error=>{
		console.log(error.message);
	})
	.then(respuesta=>{
		console.log(respuesta.status)
		return respuesta.json();
	})
	.then(datos=>{
		console.log(datos);
	})
	


});

