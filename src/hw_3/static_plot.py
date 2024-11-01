# Static Plot No 1 
# This line plot shows the velocity component 𝑈 across the spatial dimension 𝑦 at a distance of 4D from the cylinder.

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('C:/Users/admin\Downloads/archive/Astar-0.9_Ustar-8_Re-4000_sample/sample/1/fourD_U_vorticity.csv') 

# Ensure that the CSV file (fourD_U_vorticity.csv) is in the same directory as the script or 
# adjust the file path in the pd.read_csv function.

# Static Line Plot of one velocity component (U_0) against y
plt.figure(figsize=(10, 6))
plt.plot(data['y'], data['U_0'], color='blue', label='U_0')
plt.title('Velocity (U_0) across Spatial Dimension (y) at 4D Distance')
plt.xlabel('Spatial Dimension (y)')
plt.ylabel('Velocity (U_0)')
plt.legend()
plt.grid(True)
plt.show()

# Static Plot No 2
# This plot This visualizes the vorticity intensity across spatial positions y for each vorticity measurement, 
# with color representing the magnitude of vorticity.

import numpy as np

# Identify columns with vorticity data
vorticity_columns = [col for col in data.columns if 'vorticity' in col]
vorticity_data = data[vorticity_columns].T  # Transpose for compatibility with heatmap

# Create the heatmap
plt.figure(figsize=(12, 6))
plt.imshow(vorticity_data, aspect='auto', cmap='viridis', extent=[data['y'].min(), data['y'].max(), 0, len(vorticity_columns)])
plt.colorbar(label='Vorticity')
plt.title('Heatmap of Vorticity Across Spatial Dimension (y)')
plt.xlabel('Spatial Dimension (y)')
plt.ylabel('Vorticity Measurement Index')
plt.show()
