# GPT Sucks 

import math

time_list = []
vy_list = []
pos_y_list = []
energy_list = []
pos_x_list = []

state = {
    "Vx" : 0, "Vy" : 0, "Pos_x" : 0, "Pos_y" : 0
}
time = 0
dt = 0.1
Ay = -9.81
Ax = 0

def vel_update(ux0, uy0):
    Vx_new = ux0
    Vy_new = uy0 + Ay*dt
    return Vx_new, Vy_new

def pos_update(ux, uy, time):
    pos_x = state["Pos_x"]+ux*dt
    pos_y = state["Pos_y"]+uy*dt
    return pos_x, pos_y
    
def energy(speed_square, height):
    g = 9.81

    ke = 0.5 * speed_square
    pe = g*height
    Te = ke+pe
    return Te
    
def start():
    u = float(input("Enter intial velocity (m/s): "))
    angle = math.radians(float(input("angle (degree): ")))
    sin_component = math.sin(angle)
    cos_component= math.cos(angle)
    Vx_intial = u*cos_component
    Vy_intial = u*sin_component

    return Vx_intial, Vy_intial

def reset_pos():
    state["Pos_x"] = 0 
    state["Pos_y"] = 0
    return 0

def main():
    
    time = reset_pos()
    state["Vx"], state["Vy"] = start()

    print(f'Vy = {round(state["Vy"],2)} at time = {round(time,2)}, coordinates: {round(state["Pos_x"],2)},{round(state["Pos_y"],2)}')
    
    time = time+dt

    time_list = []

    while state["Pos_y"] >= 0:

        state["Vx"], state["Vy"] = vel_update(state["Vx"], state["Vy"])
        state["Pos_x"], state["Pos_y"] = pos_update(state["Vx"], state["Vy"], time)
        speed_square = (state["Vx"]*state["Vx"]) + (state["Vy"]*state["Vy"])
        Te = energy(speed_square, state["Pos_y"])
        # print(f'Vy = {round(state["Vy"],2)} at time = {round(time,2)}, coordinates: {round(state["Pos_x"],2)},{round(state["Pos_y"],2)}')
        print(f"energy = {Te}")
        time = time+dt

        time_list.append(time)
        vy_list.append(state["Vy"])
        pos_y_list.append(state["Pos_y"])
        pos_x_list.append(state["Pos_x"])
        energy_list.append(Te)

    import matplotlib.pyplot as plt

    
    # plt.figure(1)
    # plt.plot(time_list, vy_list)
    # plt.xlabel("Time (sec)")
    # plt.ylabel("Vertical Velocity (m/s)")
    # plt.title("Vy vs Time")
    # plt.grid(True)

    plt.figure(2)
    plt.plot(time_list,pos_y_list)
    plt.ylabel("Y position")
    plt.xlabel("Time")
    plt.grid(True)

    plt.figure(3)
    plt.plot(pos_x_list,pos_y_list)
    plt.ylabel("Y position")
    plt.xlabel("X position")
    plt.grid(True)

    plt.figure(4)
    plt.plot(time_list,energy_list)
    plt.ylabel("Total energy")
    plt.xlabel("Time")
    plt.grid(True)

    plt.show()

    quit()

main()


