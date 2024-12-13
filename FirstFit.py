import tkinter as tk
from tkinter import ttk, messagebox

class FirstFitMemoryAllocation:
    def __init__(self, blocks, processes):
        """Initialize memory blocks and processes"""
        self.blocks = blocks
        self.processes = processes
        self.allocation = [-1] * len(processes)  # store block allocation for each process

    def allocate_memory(self):
        """Simulate the First Fit memory allocation."""
        for i in range(len(self.processes)):
            for j in range(len(self.blocks)):
                if self.blocks[j] >= self.processes[i]:  # Check if block fits
                    self.allocation[i] = j  # Assign block to process
                    self.blocks[j] -= self.processes[i]  # Reduce block size
                    break
        return self.allocation

class MemoryAllocationApp:
    def __init__(self, master):
        """Initialize the GUI for First Fit memory allocation"""
        self.master = master
        self.master.title("First Fit memory allocation")

        # Variables to store user input
        self.blocks_var = tk.StringVar()
        self.processes_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Create widgets for the GUI"""
        # Memory blocks entry
        ttk.Label(self.master, text="Memory Blocks (comma-separated):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.blocks_entry = ttk.Entry(self.master, textvariable=self.blocks_var, width=40)
        self.blocks_entry.grid(row=1, column=0, pady=5)

        # Processes entry
        ttk.Label(self.master, text="Processes (comma-separated):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.processes_entry = ttk.Entry(self.master, textvariable=self.processes_var, width=40)
        self.processes_entry.grid(row=3, column=0, pady=5)

        # Run button
        ttk.Button(self.master, text="Run First Fit", command=self.run_allocation).grid(row=4, column=0, pady=10)

    def run_allocation(self):
        """Run the First Fit algorithm based on user inputs"""
        try:
            # Parse user inputs
            blocks = list(map(int, self.blocks_var.get().split(",")))
            processes = list(map(int, self.processes_var.get().split(",")))

            # Perform First Fit allocation
            allocator = FirstFitMemoryAllocation(blocks, processes)
            allocation = allocator.allocate_memory()

            # Display results
            self.display_results(blocks, processes, allocation)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers separated by commas.")

    def display_results(self, blocks, processes, allocation):
        """Display the allocation results in a new window."""
        result_window = tk.Toplevel(self.master)
        result_window.title("Allocation Results")

        text = "Process No.\tProcess Size\tBlock No.\n"
        for i in range(len(processes)):
            block_no = allocation[i] + 1 if allocation[i] != -1 else "Not Allocated"
            text += f"{i + 1}\t\t{processes[i]}\t\t{block_no}\n"

        result_label = tk.Label(result_window, text=text, justify=tk.LEFT, font=("Courier", 12))
        result_label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryAllocationApp(root)
    root.mainloop()
