function cambiarAno()
{
	var ley
	if (document.getElementById("leydhont").className == "leysel")
	{
		ley = "dhont"
	}
	if (document.getElementById("droop").className == "leysel")
	{
		ley = "manoli"
	}
	if (document.getElementById("hare").className == "leysel")
	{
		ley = "manoli"
	}
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=" + ley;
	draw_scene(query);
}


function seleccionarLeyDhont(){
	document.getElementById("leydhont").className = "leysel";	
	document.getElementById("droop").className = "ley";
	document.getElementById("hare").className = "ley";
	document.getElementById("imperiali").className = "ley";	
	document.getElementById("descripcioncorta").innerHTML ="<h2>Ley d'hont</h2>" + 
	"<p>El sistema de D'Hondt es una fórmula electoral, creada por Victor d'Hondt, que permite obtener el número de cargos electos asignados a las candidaturas, en proporción a los votos conseguidos.</p>";
	
	document.getElementById("descripcionmas").innerHTML = "<p>Tras escrutar todos los votos, se calcula una serie de divisores para cada lista. La fórmula de los divisores es V/N, donde V representa el número total de votos recibidos por la lista, y N representa cada uno de los números enteros de 1 hasta el número de cargos electos de la circunscripción objeto de escrutinio. Una vez realizadas las divisiones de los votos de cada candidatura por cada uno de los divisores desde 1 hasta N, la asignación de cargos electos se hace ordenando los cocientes de las divisiones de mayor a menor y asignando a cada uno un escaño hasta que éstos se agoten.</p>" +
	"<p>El orden en que se repartan los cargos electos a los individuos de cada lista no está dado por este sistema: puede ser una decisión interna del partido (en un sistema de listas cerradas) o puede que los votantes ejerzan alguna influencia (en un sistema de listas abiertas).</p>" +
	"<p>A veces, las leyes electorales fijan un porcentaje mínimo de votos tal que los partidos que no consigan alcanzar ese umbral quedan excluidos del cuerpo deliberante. En España, ese porcentaje es de 3%, aplicado a cada circunscripción electoral, provincia.</p>"

	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=dhont";
	draw_scene(query);
}

function seleccionarDroop(){
	document.getElementById("leydhont").className = "ley";	
	document.getElementById("droop").className = "leysel";
	document.getElementById("hare").className = "ley";
	document.getElementById("imperiali").className = "ley";	
	document.getElementById("descripcioncorta").innerHTML ="<h2>Cociente Droop</h2>" + 
	"<p>El cociente de Droop es una de los cocientes que se puede uitlizar en el Método del resto mayor. "+
	"El método del resto mayor o sistema de cociente y residuo electoral es un sistema electoral que se utiliza, generalmente, para repartir los escaños de un cuerpo colegiado (p. ej. un parlamento o congreso), de modo más proporcional a los votos obtenidos por las candidaturas que otros métodos. " +
	"La fórmula del cociente Droop se utiliza para calcular el número mínimo (o cuota) de votos que se requieren para obtener un escaño en algunos países que utilizan el sistema electoral de representación proporcional de tipo método del resto mayor o voto único transferible.</p>"
	document.getElementById("descripcionmas").innerHTML = "<p>El cociente de Droop tiene la característica de ser el que teóricamente permite la distribución de un número mayor de cargos sin llegar nunca a repartir más de los que correspondan a la respectiva circunscripción. En otras palabras, es el divisor más pequeño utilizable sin peligro de adjudicar más puestos que los sometidos a elección. Algunas leyes electorales han adoptado cocientes aun menores, pero esto las ha obligado a prever correctivos para el caso de que se presente este problema.</p>" +
	"<p>En la actualidad el cociente de Droop sirve de base al Sistema del Voto Unico Transferible en Irlanda, Malta y Australia (senado).</p>"
	
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=Droop";
	draw_scene(query);
}

function seleccionarHare(){
	document.getElementById("leydhont").className = "ley";	
	document.getElementById("droop").className = "ley";
	document.getElementById("hare").className = "leysel";
	document.getElementById("imperiali").className = "ley";	
	document.getElementById("descripcioncorta").innerHTML ="<h2>Cociente de Hare</h2>" +
	"<p>El cociente de Hare es una de los cocientes que se puede uitlizar en el Método del resto mayor. "+
	"El método del resto mayor o sistema de cociente y residuo electoral es un sistema electoral que se utiliza, generalmente, para repartir los escaños de un cuerpo colegiado (p. ej. un parlamento o congreso), de modo más proporcional a los votos obtenidos por las candidaturas que otros métodos. " +
	"La fórmula del cociente Hare se utiliza para calcular el número mínimo (o cuota) de votos que se requieren para obtener un escaño en algunos países que utilizan los sistema electoral de representación proporcional de tipo voto único transferible o método del resto mayor."
	document.getElementById("descripcionmas").innerHTML = "Se obtiene dividiendo el número total de votos válidos a tomar en cuenta entre el número de puestos a adjudicar en la circunscripción correspondiente. " + 
	"<p>El cociente de Hare ha sido denominado cociente natural porque corresponde al número de votos que en perfecta proporcionalidad debería recibir una lista de candidatos por cada puesto que se le adjudique. Representa el costo en votos que proporcionalmente debe tener cada cargo. Este cociente sirve de base para la distribución de cargos restantes a nivel nacional en Italia y para la distribución de puestos según los votos por lista a nivel nacional en Alemania. También se recurre a este cociente en Venezuela para la adjudicación a nivel nacional de diputados y senadores adicionales. El cociente natural presenta el problema que a consecuencia de que la votación efectiva de las diferentes listas rara vez es un múltiplo exacto del cociente, casi siempre su aplicación deja votos sobrantes (restos) y puestos sin distribuir.</p>"
	
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=Hare";
	draw_scene(query);
}

function seleccionarImperiali(){
	document.getElementById("leydhont").className = "ley";	
	document.getElementById("droop").className = "ley";
	document.getElementById("hare").className = "ley";	
	document.getElementById("imperiali").className = "leysel";
	document.getElementById("descripcioncorta").innerHTML ="<h2>Cociente Imperiali</h2>" +
	"<p>El cociente Imperiali es una de los cocientes que se puede uitlizar en el Método del resto mayor. "+
	"El método del resto mayor o sistema de cociente y residuo electoral es un sistema electoral que se utiliza, generalmente, para repartir los escaños de un cuerpo colegiado (p. ej. un parlamento o congreso), de modo más proporcional a los votos obtenidos por las candidaturas que otros métodos. " +
	"La fórmula Imperiali se utiliza para calcular el número mínimo (o cuota) de votos que se requieren para obtener un escaño en algunos países que utilizan los sistema electoral de representación proporcional de tipo voto único transferible o método del resto mayor."
	document.getElementById("descripcionmas").innerHTML = "<p>Se calcula dividiendo el total de votos válidos a tomar en cuenta entre el número de puestos a distribuir más dos.</p>" +
	"<p>Habitualmente su efecto es más favorable a los partidos mayores que el que obtienen mediante la aplicación de los sistemas de Droop o Hare. Produce cuotas menores, lo cual genera el riesgo de que haya más candidatos elegidos con cuotas completas que escaños. En una elección entre dos listas, o en una elección de voto único transferible en la que se transfieren todos los votos es inevitable que resulte elegido un número incorrecto de candidatos, lo que requiere un ajuste posterior. Este fallo hace que el sistema no se use apenas.</p>"
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=Imperiali";
	draw_scene(query);
}

function vermas(){
	document.getElementById("descripcionmas").style.display = 'block';
	document.getElementById("vermas").style.display = 'none';
	document.getElementById("ocultar").style.display = 'block';
}

function ocultar(){
	document.getElementById("descripcionmas").style.display = 'none';
	document.getElementById("vermas").style.display = 'block';
	document.getElementById("ocultar").style.display = 'none';
}

