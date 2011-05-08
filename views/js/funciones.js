function cambiarAno()
{
	var ley
	if (document.getElementById("leydhont").className == "leysel")
	{
		ley = "dhont"
	}
	if (document.getElementById("manoli").className == "leysel")
	{
		ley = "manoli"
	}
	if (document.getElementById("pruebito").className == "leysel")
	{
		ley = "manoli"
	}
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=" + ley;
	draw_scene(query);
}

function cambiarAnoLeyManoli()
{
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=manoli";
	draw_scene(query);
}

function cambiarAnoLeyPruebito()
{
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=manoli";
	draw_scene(query);
}


function seleccionarLeyDhont(){
	document.getElementById("leydhont").className = "leysel";	
	document.getElementById("manoli").className = "ley";
	document.getElementById("pruebito").className = "ley";
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
	document.getElementById("manoli").className = "leysel";
	document.getElementById("pruebito").className = "ley";
	document.getElementById("descripcioncorta").innerHTML ="<h2>Cociente Droop</h2>" + 
	"<p>Denominado así en honor a su proponente, el abogado inglés Henry Droop, cuyo libro Sobre el Método para Elegir los Representantes fue publicado en 1868. Se calcula dividiendo el total de votos válidos a tomar en cuenta entre el número de puestos a distribuir más uno, y luego al número entero que resulte se le añade uno.</p>"
	document.getElementById("descripcionmas").innerHTML = "<p>El cociente de Droop tiene la característica de ser el que teóricamente permite la distribución de un número mayor de cargos sin llegar nunca a repartir más de los que correspondan a la respectiva circunscripción. En otras palabras, es el divisor más pequeño utilizable sin peligro de adjudicar más puestos que los sometidos a elección. Algunas leyes electorales han adoptado cocientes aun menores, pero esto las ha obligado a prever correctivos para el caso de que se presente este problema..</p>" +
	"<p>En la actualidad el cociente de Droop sirve de base al Sistema del Voto Unico Transferible en Irlanda, Malta y Australia (senado). También se usa dentro del llamado sistema de Hagenbach-Bischoff, que emplea la distribución por cociente para la primera distribución y el método D’Hondt (media más elevada) para la adjudicación de los cargos restantes, por ello algunos autores dan a este cociente el nombre de Hagenbach-Bischoff. En esta modalidad (combinado con el método D’Hondt) funciona en Suiza, Luxemburgo y Lichstenstein.</p>"
	
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=manoli";
	draw_scene(query);
}

function seleccionarPruebito(){
	document.getElementById("leydhont").className = "ley";	
	document.getElementById("manoli").className = "ley";
	document.getElementById("pruebito").className = "leysel";	
	document.getElementById("descripcioncorta").innerHTML ="<h2>Ley de pruebito</h2><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>"
	var indice = document.getElementById("select-ano").selectedIndex; 
	var ano = document.getElementById("select-ano").options[indice].value; 
	var query = "/?year=" + ano + "&alg=manoli";
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

