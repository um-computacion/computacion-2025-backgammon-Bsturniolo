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

# Backgammon - Proyecto Computación 2025

## Características implementadas

- ✅ Tablero (`Board`) con 24 puntos y configuración inicial correcta
- ✅ Jugadores (`Player`) con nombre e id
- ✅ Dados (`Dice`) con manejo de dobles
- ✅ Movimiento de fichas (`move_checker`) en el tablero
- ✅ Validación de movimientos (`can_move`)
- ✅ Fichas (`Checker`) con dueño
- ✅ Interfaz por consola (CLI) básica con turnos y tirada de dados
- ✅ Pruebas unitarias para Board, Player, Dice, Game y Checker
- ✅ Integración continua con GitHub Actions

## Próximos pasos

- ➡️ Implementar barra de fichas capturadas
- ➡️ Implementar borneado (remover fichas)
- ➡️ Reglas de victoria
- ➡️ Interfaz gráfica con Pygame
