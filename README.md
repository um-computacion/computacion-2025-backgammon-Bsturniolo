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

## ♟️ Sistema de barra en el Backgammon

En **Backgammon**, cuando una ficha es **golpeada**, no se elimina del juego.  
En su lugar, se **envía a la barra**, una zona temporal donde espera hasta poder volver a entrar al tablero.

### 🧩 ¿Cómo funciona la barra?
- Cada jugador tiene su propia barra:
  - `Jugador 1 (O)` → `bar[1]`
  - `Jugador 2 (X)` → `bar[-1]`
- Si una ficha enemiga queda sola en un punto (por ejemplo, un `-1`) y el jugador contrario cae en ese punto, la ficha es golpeada y:
  - Se suma `+1` a la barra del jugador golpeado.
  - El punto se reemplaza por la ficha del jugador que golpeó.
- Mientras un jugador tenga fichas en su barra, **debe reingresarlas** antes de realizar otros movimientos (esta mecánica se implementará más adelante).

## ♻️ Reentrada desde la barra

Cuando una ficha ha sido **golpeada**, se almacena en la barra del jugador.  
Para volver al juego, el jugador debe **reingresar** esa ficha al tablero en su zona de entrada.

### 🧩 Reglas básicas
- Cada jugador tiene una zona de entrada:
  - **Jugador 1 (O)** entra entre los puntos **1 a 6** (índices 0–5).
  - **Jugador 2 (X)** entra entre los puntos **19 a 24** (índices 18–23).
- Si el punto de entrada está:
  - **Vacío o con fichas propias**, la ficha entra normalmente.
  - **Con una sola ficha enemiga**, la golpea (y esa ficha va a la barra).
  - **Con dos o más fichas enemigas**, el punto está **bloqueado** y no se puede reingresar ahí.
- Si un jugador tiene fichas en la barra, **debe reingresarlas antes de hacer cualquier otro movimiento**.

