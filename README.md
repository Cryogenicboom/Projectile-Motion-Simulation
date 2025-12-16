# Projectile Motion Simulation (Python)

This project simulates **2D projectile motion** using a discrete time-step approach.  
It numerically computes the projectile’s velocity, position, and mechanical energy over time and visualizes the results using graphs.

The purpose of this project is to understand how classical kinematic equations behave when implemented **numerically** rather than using closed-form physics equations.

---

## Physical Model & Assumptions

The simulation is based on the following assumptions:

- Constant gravitational acceleration (`g = 9.81 m/s²`)
- No air resistance
- Horizontal acceleration is zero
- Fixed time step (`dt = 0.1 s`)
- Projectile starts from the origin `(0, 0)`
- Simulation stops when the projectile reaches the ground (`y < 0`)

> **Note:**  
> This is a numerical approximation using **Euler’s method**, not an exact analytical solution.

---

## Code Structure

### Global State

The projectile state is stored using a dictionary:

- `Vx`, `Vy` → Horizontal and vertical velocity
- `Pos_x`, `Pos_y` → Projectile position

Lists are used to store values for plotting:

- `time_list`
- `vy_list`
- `pos_y_list`

---

## Function Overview

### `start()`
Takes user input for:
- Initial velocity (m/s)
- Launch angle (degrees)

Resolves them into horizontal and vertical velocity components.

---

### `vel_update(ux0, uy0)`
Updates the velocity using constant gravitational acceleration.

---

### `pos_update(ux, uy, time)`
Updates the projectile position using the current velocity and time step.

---

### `energy(speed_square, height)`
Calculates total mechanical energy:

- **Kinetic Energy:** `0.5 * v²`
- **Potential Energy:** `g * h`

Returns the total energy at a given time step.

---

### `reset_pos()`
Resets the projectile position to the origin before starting the simulation.

---

### `main()`
Runs the main loop while y-pos > 0
