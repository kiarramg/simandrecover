# Bash script to run the full simulation
#!/bin/bash

# Ensure correct environment is activated (modify path if needed)
source /usr/local/bin/python3

# Run the Python simulation script
python3 src/main.py

# Print completion message
echo "Simulation complete. Results saved in simulation_results.txt."
