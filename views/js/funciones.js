

function seleccionarLeyDhont(){
	document.getElementById("leydhont").className = "leysel";	
	document.getElementById("manoli").className = "ley";
	document.getElementById("pruebito").className = "ley";
	document.getElementById("descripcioncorta").innerHTML ="<h2>Ley d'hont</h2>" + 
	"<p>El sistema de D'Hondt es una fórmula electoral, creada por Victor d'Hondt, que permite obtener el número de cargos electos asignados a las candidaturas, en proporción a los votos conseguidos.</p>";
	
	document.getElementById("descripcionmas").innerHTML = "<p>Tras escrutar todos los votos, se calcula una serie de divisores para cada lista. La fórmula de los divisores es V/N, donde V representa el número total de votos recibidos por la lista, y N representa cada uno de los números enteros de 1 hasta el número de cargos electos de la circunscripción objeto de escrutinio. Una vez realizadas las divisiones de los votos de cada candidatura por cada uno de los divisores desde 1 hasta N, la asignación de cargos electos se hace ordenando los cocientes de las divisiones de mayor a menor y asignando a cada uno un escaño hasta que éstos se agoten.</p>" +
	"<p>El orden en que se repartan los cargos electos a los individuos de cada lista no está dado por este sistema: puede ser una decisión interna del partido (en un sistema de listas cerradas) o puede que los votantes ejerzan alguna influencia (en un sistema de listas abiertas).</p>" +
	"<p>A veces, las leyes electorales fijan un porcentaje mínimo de votos tal que los partidos que no consigan alcanzar ese umbral quedan excluidos del cuerpo deliberante. En España, ese porcentaje es de 3%, aplicado a cada circunscripción electoral, provincia.</p>"
}

function seleccionarManoli(){
	document.getElementById("leydhont").className = "ley";	
	document.getElementById("manoli").className = "leysel";
	document.getElementById("pruebito").className = "ley";
	document.getElementById("descripcioncorta").innerHTML ="<h2>Ley de manoli</h2><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>"

}

function seleccionarPruebito(){
	document.getElementById("leydhont").className = "ley";	
	document.getElementById("manoli").className = "ley";
	document.getElementById("pruebito").className = "leysel";	
	document.getElementById("descripcioncorta").innerHTML ="<h2>Ley de pruebito</h2><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>"

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

