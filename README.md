# 🌀 Marbling Simulation using Processing.py

This project simulates **paper marbling** – a traditional art technique – using Python mode in the Processing environment. The canvas is imagined as a **tray of water**, and drops of colored ink (red, green, and blue) are added and manipulated based on simple fluid dynamics principles.

##  Features

- **Blank Mode (Key `0`)**  
  Starts with a blank canvas. Clears all previous drops and interactions.

- **Create Mode (Key `1`)**  
  Add colorful circular ink drops to the tray. Drops interact using a simplified **incompressible and immiscible fluid behavior**, based on **Jaffer's displacement formula**. This ensures drops deform when new ones are added nearby but do not mix.

- **Tineline Mode (Key `2`)**  
  Click and drag to apply a **"tineline" transformation** – ink gets pulled along the vector you draw. The length of your drag controls the **strength** of the deformation, creating swirling and flowing effects on the drops.

## Interaction

| Key | Mode         | Description                                     |
|-----|--------------|-------------------------------------------------|
| `0` | Blank        | Clears everything and resets to a blank screen |
| `1` | Create Mode  | Click to drop red, green, or blue circles       |
| `2` | Tineline Mode| Click and drag to deform ink along a vector     |

## Technical Notes

- Written entirely in **Processing.py (Python Mode)**.
- Each ink drop is a circular shape made from discrete points.
- Deformation and displacement are applied using vector operations to maintain incompressibility and immiscibilty using Jaffer's formula.
- The goal is to mimic the physical properties of ink drops floating on water.

## How to Run

1. Open **Processing** and switch to **Python Mode**.
2. Paste the code from `marbling_simulation.py`.
3. Run and interact using your mouse and keyboard as described above.

