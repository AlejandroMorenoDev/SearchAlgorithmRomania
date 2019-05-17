# SearchAlgorithmRomania
Se trata de una solución al problema del GPS en Rumanía.
Basándonos en la implementación de la búsqueda en anchura y la búsqueda en profundidad, se han diseñado otros 2 algoritmos de búsqueda:
"Ramificación y Acotación" y "Ramificación y Acotación con Subestimación".

Ramificación y Acotación: Consiste en ordenar la lista abierta utilizando para ello el coste acumulado o path_cost que supone desplazarse hasta dicho nodo.
Los nodos quedan ordenados de menor a mayor coste acumulado. De este modo, se prioriza la expansión de los nodos con menor coste, llegando así a una solución eficiente.

Ramificación y Acotación con Subestimación: Se basa en la solución anterior, pero esta vez se apoya en una heurística de distancia euclídea entre el nodo y el nodo objetivo.
De este modo, con la suma de path_cost y heurística conseguimos "premiar" a aquellos nodos más próximos al objetivo. Estos se situarían al principio de la lista abierta, ordenada de menor a mayor, priorizando así su expansión.
