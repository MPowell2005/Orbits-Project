'''
Author: Michael Powell
Narrative: This program allows the user to simulate the orbit of an object around a host.

@author: mpowell23@gcds.net
'''

# Import Box
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_collection(number_of_rows, G, mass_of_host, time_increment, x_position_initial, x_velocity_initial, y_position_initial, y_velocity_initial):
    # Define eight lists that will contain the values for time, x-position, x-velocity, x-acceleration, y-position, y-velocity,  y-acceleration, and speed
    time_storage = []
    x_position_storage = []
    x_velocity_storage = []
    x_acceleration_storage = []
    y_position_storage = []
    y_velocity_storage = []
    y_acceleration_storage = []
    speed_storage = []
    
    # Collect all of the data into these lists for the predetermined number of rows
    counter = 1
    while counter <= number_of_rows:
        # Variable calculation process for each list at the first row
        if counter == 1:
            time = 0
            x_position = x_position_initial
            x_velocity = x_velocity_initial
            y_position = y_position_initial
            y_velocity = y_velocity_initial
            x_acceleration = -(G * mass_of_host * x_position)/((x_position**2 + y_position**2)**1.5)
            y_acceleration = -(G * mass_of_host * y_position)/((x_position**2 + y_position**2)**1.5)
            speed = (x_velocity**2 + y_velocity**2)**0.5
    
        # Variable calculation process for each list after the first row
        else:
            time = time + time_increment
            x_position = x_velocity*time_increment + x_position
            x_velocity = x_acceleration*time_increment + x_velocity
            y_position = y_velocity*time_increment + y_position
            y_velocity = y_acceleration*time_increment + y_velocity
            x_acceleration = -(G * mass_of_host * x_position)/((x_position**2 + y_position**2)**1.5)
            y_acceleration = -(G * mass_of_host * y_position)/((x_position**2 + y_position**2)**1.5)
            speed = (x_velocity**2 + y_velocity**2)**0.5
        
        counter = counter + 1
        
        # Data collection for each calculated variable
        time_storage.append(time)
        x_position_storage.append(x_position)
        x_velocity_storage.append(x_velocity)
        x_acceleration_storage.append(x_acceleration)
        y_position_storage.append(y_position)
        y_velocity_storage.append(y_velocity)
        y_acceleration_storage.append(y_acceleration)
        speed_storage.append(speed)
    
    data_storage = [time_storage, x_position_storage, x_velocity_storage, x_acceleration_storage, y_position_storage, y_velocity_storage, y_acceleration_storage, speed_storage]
    return data_storage


def main():
    # Define the names of the orbiter and host
    host_name = 'The Earth'
    orbiter_name = 'The Moon'
    
    # Define the values for the inputs into the data collection function
    G = 6.67*10**-11
    mass_of_host = 5.972e24
    time_increment = 250
    total_time = 2332800
    x_position_initial = 384472282
    x_velocity_initial = 0
    y_position_initial = 0
    y_velocity_initial = 1000
    
    # Calculate the number of rows to create in the data collection function
    number_of_rows = total_time/time_increment + 1
    
    # Collect data for the x-position, x-velocity, x-acceleration, y-position, y-velocity, y-acceleration, and speed at particular times
    data_storage = data_collection(number_of_rows, G, mass_of_host, time_increment, x_position_initial, x_velocity_initial, y_position_initial, y_velocity_initial)
    
    # Define the list of values for the time, x-position, y-position, and speed out of data_storage
    time_storage = data_storage[0]
    x_position_storage = data_storage[1]
    y_position_storage = data_storage[4]
    speed_storage = data_storage[7]
    
    # Define a figure that will illustrate the motion of an object around a host
    # The figure will consist of four plots in a 2 by 2 matrix
    figure, ax = plt.subplots(ncols = 2, nrows = 2)
    figure.suptitle('The Orbit of "' + orbiter_name + '" around "' + host_name + '"')
    
    # Draw the plane curve of the planet that orbits the host
    plane_curve, = ax[0, 0].plot(x_position_storage, y_position_storage, color = "#000000", linewidth = 1.5)
    ax[0, 0].set_xlabel('X-position (meters)')
    ax[0, 0].set_ylabel('Y-position (meters)')
    ax[0, 0].grid()
    
    # Plot the orbiter moving around the plane curve
    orbiter, = ax[0, 0].plot(0, 0, "o", markeredgecolor = "#000000", markerfacecolor = "#fefcd7")
    
    # Plot the host at one of the foci of the plane curve
    ax[0, 0].plot(-(max(x_position_storage)**2 - max(y_position_storage)**2)**0.5, 0, "o", markeredgecolor = "#9fc164", markerfacecolor = "#4f4cb0")
    
    # Draw the curve that represents the speed as a function of time
    speed_curve, = ax[0, 1].plot(time_storage, speed_storage, color = '#008000', linewidth = 3)
    ax[0, 1].set_xlabel('Time (seconds)')
    ax[0, 1].set_ylabel('Speed (meters per second)')
    ax[0, 1].grid()
    
    # Draw the curve that represents the x-position of the orbiter as a function of time
    x_position_curve, = ax[1, 0].plot(time_storage, x_position_storage, color = "#ff0000", linewidth = 3)
    ax[1, 0].set_xlabel('Time (seconds)')
    ax[1, 0].set_ylabel('X-position (meters)')
    ax[1, 0].grid()
    
    # Draw the curve that represents the y-position of the orbiter as a function of time
    y_position_curve, = ax[1, 1].plot(time_storage, y_position_storage, color = "#0000ff", linewidth = 3)
    ax[1, 1].set_xlabel('Time (seconds)')
    ax[1, 1].set_ylabel('Y-position (meters)')
    ax[1, 1].grid()
    
    # Define empty lists that will update throughout the animation process
    t_data = []
    x_data = []
    y_data = []
    speed_data = []
    
    # Establish the number of frames for which the animation will occur
    frame_length = int(number_of_rows/10)
    
    # Utilize the animate function to animate the three plots defined above
    def animate(i):
        # Avoids bug whereby moving the window for the figure sets i equal to 0
        if i == 0:
            pass
        else:
            # Slowly add values to the empty lists by using the parameter i
            t_data.append(time_storage[10*i])
            x_data.append(x_position_storage[10*i])
            y_data.append(y_position_storage[10*i])
            speed_data.append(speed_storage[10*i])
            
            # Set data into each parametric curve and the particles as it updates in the animate function
            plane_curve.set_data(x_data, y_data)
            x_position_curve.set_data(t_data, x_data)
            y_position_curve.set_data(t_data, y_data)
            speed_curve.set_data(t_data, speed_data)
            orbiter.set_data(x_data[len(x_data) - 1], y_data[len(y_data) - 1])
            
        return plane_curve, x_position_curve, y_position_curve, speed_curve, orbiter
    
    # Output the animation using "FuncAnimation"
    ani = animation.FuncAnimation(figure, animate, frames = frame_length, interval = 1, blit = True, repeat = False)
    
    # Output the figure
    print('See the orbit in the plot below:')
    figure.tight_layout()
    plt.show()
    print('The orbit has finished.')
    
if __name__ == '__main__':
    main()