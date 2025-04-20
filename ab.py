import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def average(a: float, b: float):
    """Returns the number which is halfway between a and b."""
    return (a + b) / 2

# Define the main function for animation
def animate(i):
    # Initial data points for averaging
    a_values = [0, 10]
    b_values = [8, 10]
    
    # Calculate averages at different steps
    avg_1 = average(a_values[0], a_values[1])
    avg_2 = average(b_values[0], b_values[1])

    # Calculate the final average
    final = average(avg_1, avg_2)
    
    # Plot the process
    ax.clear()
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1, 12)

    ax.set_title(f"Averaging Step: {i+1}")
    
    ax.plot(a_values, [0, 0], 'bo-', label=f"First Pair (avg_1 = {avg_1})")
    ax.plot(b_values, [1, 1], 'ro-', label=f"Second Pair (avg_2 = {avg_2})")
    
    # Display the midpoint of both pairs
    ax.plot([avg_1, avg_2], [0.5, 0.5], 'go-', label=f"Final Average (final = {final})")
    
    # Display text for the averages
    ax.text(5, -0.5, f"avg_1 = {avg_1:.2f}", ha='center')
    ax.text(5, 1.5, f"avg_2 = {avg_2:.2f}", ha='center')
    ax.text(5, 2.5, f"final = {final:.2f}", ha='center')
    
    ax.legend()

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 12)
ax.set_ylim(-1, 4)

# Create the animation
ani = FuncAnimation(fig, animate, frames=3, repeat=False)

plt.show()
