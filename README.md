# Backgammon en Python 🎲

Este proyecto implementa el clásico juego **Backgammon** en Python, con dos modalidades:
- **CLI (línea de comandos)** → obligatoria.
- **Interfaz gráfica con Pygame** → opcional, pero incluida para una experiencia visual.

El desarrollo sigue principios **SOLID**, pruebas unitarias (≥90% de cobertura), y documentación con docstrings.

---

## Estructura del proyecto

backgammon/
├── core/ → lógica central (tablero, jugadores, dados, fichas, juego)
├── cli/ → interfaz de consola
├── pygame_ui/ → interfaz gráfica con Pygame
├── assets/ → imágenes y sonidos
├── requirements.txt
└── README.md

---

## Plan de Commits (primer sprint)

Los próximos **10 commits** estarán organizados así:

1. **chore: inicializar estructura de proyecto y README.md**  
   - Crear carpetas (`core/`, `cli/`, `pygame_ui/`, `assets/`) y archivos iniciales.  
   - README básico con plan de commits.  

2. **feat(core): implementar clase `Board` inicial**  
   - Clase `Board` con 24 puntos representados.  
   - Inicialización de posiciones estándar del Backgammon.  

3. **feat(core): agregar clase `Checker`**  
   - Representa una ficha individual de un jugador.  

4. **feat(core): implementar clase `Player`**  
   - Contiene nombre, color, fichas y estado (ej: fichas en la barra, fichas fuera).  

5. **feat(core): implementar clase `Dice`**  
   - Simulación de tiradas con soporte para dobles.  

6. **feat(core): agregar clase `BackgammonGame` (flujo general)**  
   - Coordina jugadores, tablero y tiradas.  
   - Alterna turnos.  

7. **feat(cli): crear CLI inicial para mostrar tablero**  
   - Mostrar tablero en consola.  
   - Tirar dados.  

8. **test(core): agregar pruebas unitarias de `Board`, `Dice` y `Player`**  
   - Primeros tests con `unittest`.  

9. **docs: agregar `CHANGELOG.md` inicial**  
   - Siguiendo formato de [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).  

10. **ci: configurar integración continua**  
   - Configuración de GitHub Actions o similar para correr tests automáticamente.  

---

## Requisitos futuros

- Interfaz gráfica con **Pygame**.  
- Guardado de partidas con **Redis** (opcional).  
- Documentación completa (`JUSTIFICACION.md`, prompts de IA usados).  

---

