# Ultimate Tic Tac Toe - Proyecto de Inteligencia Artificial

Para la clase de Inteligencia Artificial (ITAM, Primavera 2024), se nos dejó como proyecto hacer una Inteligencia Artificial que jugara "Ultimate Tic Tac Toe". En este repositorio se incluyen todas las clases utilizadas para realizar el proyecto.

El Código completo está dividido en 5 archivos:
- *Move*, *GameBoard* y *UtttError*, hechas por [*@mellamanelpoeta*](https://github.com/mellamanelpoeta), que incluyen la implementación del juego y las reglas, así como métodos para verificar el estado del tablero, quien ha ganado en los sub-juegos, etc.
- *GameMethods*, hecha por mi ([*@Palazrak*](https://github.com/Palazrak)) y por [*@fridamarquezg*](https://github.com/fridamarquezg), que incluye la implementación de un algoritmo *minimax* y la *funcion heurística* utilizada en el proyecto.
- *UltimateTicTacToe*, hecha por [*@Majo2103*](https://github.com/Majo2103), que reúne todos los archivos para poder correr un ejecutable en terminal para jugar contra la IA que programamos.

### Instrucciones de uso

Se deben descargar todos los archivos contenidos en este repositorio y en la terminal se debe correr el archivo "UltimateTicTacToe.py", el cual es el juego como tal.

Una vez ejecutado el archivo, se debe elegir quien jugara primero, si la inteligencia artificial o el usuario (por medio de inputs). Para insertar una jugada, es importante escribir la posición en la que se quiere jugar **en notación matricial, sin usar comas**. Por ejemplo, si quisiera jugar en el centro del tablero, se debe escribir "55" y dar "enter", para que la IA procese la jugada y arroje el resultado. 

En caso de elegir una casilla no valida (según las reglas de Ultimate Tic Tac Toe), se imprimirá en pantalla que la jugada no fue valida, y te pedirá que vuelvas a insertar una jugada.

El juego continuara hasta que haya un ganador o haya un empate.

### Sobre la función heurística utilizada

La función heurística evalúa en todo momento el estado del tablero grande y el estado del sub-juego en el que se encuentre a la profundidad deseada (en este código es profundidad 5, ya que se solicitó que la IA tardara menos de 30 seg. en decidir una jugada).

Para los sub-juegos, evalúa la cantidad de *winning lines* que hay (una winning line es aquella en la que falta una ficha para poder ganar ese tablero), mientras que, para el tablero grande, además de evaluar las winning lines, pondera cada casilla con un valor arbitrario (el centro como más valioso, las esquinas en segundo lugar y al último los "medios"). también, considera como una mala jugada regalarle una tirada al enemigo, por lo que penaliza esa jugada bastante.

Al final, regresa la suma de las tres funciones evaluadoras, y ese valor es el que se propaga según el algoritmo minimax (considerando la victoria como infinito y la derrota como infinito negativo).