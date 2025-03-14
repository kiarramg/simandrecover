# Bash script to run all tests
#!/bin/bash

set -e  # Stop on any error

echo "Running unit tests..."

python3 -m unittest test/test_simulate.py
python3 -m unittest test/test_recover.py

echo "All tests passed!"
