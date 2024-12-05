import random

x_dim = int(input("X dimension: "))
z_dim = int(input("Z dimension: "))

# Function to update y_dim while keeping it within 0.1 of old_y_dim
def generate_y(old_y_dim):
	while True:
		new_y_dim = random.randint(-100, 100) / 100  # Generate new y_dim
		if abs(new_y_dim - old_y_dim) <= 0.05:  # Check if within 0.1 range
			return new_y_dim

# Main logic
old_y_dim = 0.0  # Initialize old_y_dim
for x in range(x_dim):
	for z in range(z_dim):
		y_dim = generate_y(old_y_dim)  # Generate new y_dim
		print(f"{y_dim},", end="")
		old_y_dim = y_dim  # Update old_y_dim
	print(",")  # New row
