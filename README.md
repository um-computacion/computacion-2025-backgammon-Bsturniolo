## 📖 ¿Qué es Backgammon?

**Backgammon** es uno de los juegos de mesa más antiguos del mundo, con más de 5000 años de historia.  
Es un juego para **2 jugadores** que combina estrategia y azar (dados).  

### 🎯 Objetivo
Mover las **15 fichas** de cada jugador alrededor del tablero y ser el primero en sacarlas todas.  

### 🕹️ Reglas básicas
- El tablero tiene **24 puntos** (triángulos), divididos en 4 cuadrantes.  
- Cada jugador comienza con **15 fichas** colocadas en posiciones estándar.  
- En cada turno se lanzan **dos dados de 6 caras**:  
  - Los números indican cuántos puntos se puede avanzar.  
  - Si sale doble, se juega el número **cuatro veces**.  
- Se puede **capturar** fichas rivales si hay una sola en un punto (se envían a la barra).  
- Las fichas capturadas deben **reingresar desde la barra** antes de mover otras.  
- Gana el primero que logre **sacar todas sus fichas** del tablero.  

### 🖥️ Cómo jugar
1. Ejecuta el juego con Python:  
   ```bash
   python cli.py
   
## Roadmap del proyecto

- [x] Estructura inicial del proyecto
- [x] Clases principales: Board, Player, Dice, Checker, BackgammonGame
- [x] CLI inicial con visualización básica
- [x] Pruebas unitarias iniciales (Dice, Board, Player, Game, Checker)
- [x] Configuración de integración continua (GitHub Actions)
- [ ] Implementar movimientos de fichas
- [ ] Reingreso de fichas desde la barra
- [ ] Borneado de fichas
- [ ] Reglas de victoria
- [ ] Interfaz gráfica con Pygame
