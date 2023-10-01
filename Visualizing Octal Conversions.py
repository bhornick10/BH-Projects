import matplotlib.pyplot as plt
import numpy as np

# Initialize the figure and axis
fig, ax = plt.subplots()

# Define the range of octal numbers
octal_range = np.array(range(8))

# Initialize an empty 2D array to store octal addition results
octal_sum = np.zeros((8, 8), dtype=int)

# Calculate octal sums
for i in octal_range:
    for j in octal_range:
        sum_decimal = i + j
        sum_octal = int(str(oct(sum_decimal))[2:])
        octal_sum[i, j] = sum_octal

# Create the chart
cax = ax.matshow(octal_sum, cmap='viridis')

# Add color bar
plt.colorbar(cax)

# Add labels for rows and columns
for i in octal_range:
    for j in octal_range:
        c = octal_sum[j, i]
        ax.text(i, j, str(c), va='center', ha='center', color='white',fontweight = 'bold', fontsize = 20)

# Set x and y axis labels
ax.set_xticks(octal_range)
ax.set_yticks(octal_range)
ax.set_xticklabels(octal_range)
ax.set_yticklabels(octal_range)

# Set chart title and axis labels
plt.title("Number it is being added to")
plt.xlabel("Octal Addition Chart")
plt.ylabel("Original Number")

# Show the plot
plt.show()
