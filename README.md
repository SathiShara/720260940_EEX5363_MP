# 720260940_EEX5363_MP
# First Fit Memory Allocation-GUI Implementation

This mini project demonstrates the First Fit Memory Allocation Algorithm using Python. The algorithm is implemented with a graphical user interface (GUI) created using the `tkinter` library.

## Features
- Dynamic Memory Allocation: Simulates the First Fit algorithm for memory management.
- User-Friendly GUI: Provides an interface to input memory block sizes and process sizes.
- Detailed Results: Displays which process is allocated to which memory block or marked as "Not Allocated."

## How to Use:
1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/first-fit-memory-allocation.git
   cd first-fit-memory-allocation


2. Run the Program:

Ensure you have Python installed on your system.
Run the program using the following command
python first_fit_gui.py

3. Input Details:

Enter the memory block sizes (comma-separated) in the "Memory Blocks" field.
Enter the process sizes (comma-separated) in the "Processes" field.
Click the "Run First Fit" button to execute the algorithm.

4. View Results:

A new window will display which processes were allocated to which blocks.

## Example
Input:
Memory Blocks: 100, 500, 200, 300, 600
Processes: 212, 417, 112, 426
Output:
Process No.   Process Size   Block No.
1             212            2
2             417            5
3             112            3
4             426            Not Allocated

# code explaination
## Main Components:
1. FirstFitMemoryAllocation Class:

Implements the First Fit algorithm.
Allocates processes to memory blocks and tracks the allocation.

2. MemoryAllocationApp Class:

Creates the GUI for user interaction.
Handles user input, runs the allocation algorithm, and displays results.

## Workflow:
1. Parse user inputs (memory blocks and process sizes).
2. Run the First Fit algorithm to allocate processes.
3. Display results in a new GUI window.
   
## Requirements:
- Python 3.x
- tkinter (Standard Python Library)

## File Structure
- first_fit_gui.py: Main Python script containing the algorithm and GUI.
- README.md: Documentation for the project.

## Future Enhancements
- Add support for other algorithms like Best Fit and Worst Fit.
- Include a visualization of memory allocation (e.g., bar chart or grid view).
