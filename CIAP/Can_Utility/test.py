
import tkinter as tk
from tkinter import messagebox
import can
import random
import threading
import uptime

class MainWindow(tk.Tk):
    def __init__(self, channel='PCAN_USBBUS1', bitrate=500000):
        super().__init__()

        self.bus = None
        self.initialize_can_bus(channel, bitrate)

        # Initialize variables
        self.current_odo_value = 0
        self.vehicle_speed_running = False
        self.engine_speed_running = False
        self.odo_running = False

        self.title("CAN Utility")
        self.geometry("400x300")

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select CAN IDs:").pack(pady=10)

        self.vehicle_speed_var = tk.BooleanVar()
        self.engine_speed_var = tk.BooleanVar()
        self.odo_var = tk.BooleanVar()

        tk.Checkbutton(self, text="Vehicle Speed", variable=self.vehicle_speed_var, command=self.log_selection).pack()
        tk.Checkbutton(self, text="Engine Speed", variable=self.engine_speed_var, command=self.log_selection).pack()
        tk.Checkbutton(self, text="ODO", variable=self.odo_var, command=self.log_selection).pack()

        tk.Button(self, text="START", command=self.start_actions).pack(pady=20)
        tk.Button(self, text="STOP", command=self.stop_actions).pack(pady=5)
        tk.Button(self, text="RESET", command=self.reset_fun).pack(pady=5)

    def initialize_can_bus(self, channel, bitrate):
        """Initialize the CAN bus."""
        try:
            self.bus = can.interface.Bus(channel=channel, interface='pcan', bitrate=bitrate)
            self.log("CAN bus initialized successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize CAN bus: {e}")
            self.destroy()

    def log(self, message):
        """Log messages to the existing logging window."""
        # Assuming you have a method to update your existing log
        print(message)  # Replace this with the method to update your actual log

    def log_selection(self):
        """Log the selected CAN IDs."""
        selected_ids = []
        if self.vehicle_speed_var.get():
            selected_ids.append("Vehicle Speed")
        if self.engine_speed_var.get():
            selected_ids.append("Engine Speed")
        if self.odo_var.get():
            selected_ids.append("ODO")

        self.log("Selected CAN IDs: " + ", ".join(selected_ids))

    def start_actions(self):
        """Start sending messages based on selected checkboxes."""
        if self.bus is None:
            messagebox.showwarning("Warning", "CAN bus is not initialized.")
            return

        if self.vehicle_speed_var.get() and not self.vehicle_speed_running:
            self.vehicle_speed_running = True
            threading.Thread(target=self.vehicle_speed_fun, daemon=True).start()

        if self.engine_speed_var.get() and not self.engine_speed_running:
            self.engine_speed_running = True
            threading.Thread(target=self.engine_speed_fun, daemon=True).start()

        if self.odo_var.get() and not self.odo_running:
            self.odo_running = True
            threading.Thread(target=self.odo_fun, daemon=True).start()

        self.log("Started sending messages for: " + ", ".join(self.get_selected_ids()))

    def stop_actions(self):
        """Stop sending messages."""
        self.vehicle_speed_running = False
        self.engine_speed_running = False
        self.odo_running = False
        self.log("Stopped all actions.")

    def get_selected_ids(self):
        """Get selected CAN IDs as a list."""
        ids = []
        if self.vehicle_speed_var.get():
            ids.append("Vehicle Speed")
        if self.engine_speed_var.get():
            ids.append("Engine Speed")
        if self.odo_var.get():
            ids.append("ODO")
        return ids

    def vehicle_speed_fun(self):
        while self.vehicle_speed_running:
            if self.bus:
                can_id = 0x18FEF100
                message = can.Message(arbitration_id=can_id, data=[0] * 8, is_extended_id=True)

                vehicle_speed_int = random.randint(0, 250)
                message.data[2] = vehicle_speed_int & 0x00FF

                try:
                    self.bus.send(message)
                    self.log(f"Sent Vehicle Speed: {vehicle_speed_int}")
                except can.CanError as e:
                    self.log(f"Failed to send vehicle speed message: {e}")

                time.sleep(0.1)

    def engine_speed_fun(self):
        while self.engine_speed_running:
            if self.bus:
                can_id = 0x0CF00400
                message = can.Message(arbitration_id=can_id, data=[0] * 8, is_extended_id=True)

                engine_speed = random.uniform(501, 8031.875)
                scaled_engine_speed = int(engine_speed * 16)
                message.data[3] = scaled_engine_speed & 0x00FF
                message.data[4] = (scaled_engine_speed >> 8) & 0x00FF

                try:
                    self.bus.send(message)
                    self.log(f"Sent Engine Speed: {engine_speed}")
                except can.CanError as e:
                    self.log(f"Failed to send engine speed message: {e}")

                time.sleep(0.1)

    def odo_fun(self):
        can_id = 0x18FF5117
        message = can.Message(arbitration_id=can_id, data=[0] * 8, is_extended_id=True)

        ODO_step = 6
        while self.odo_running:
            if self.bus:
                self.current_odo_value += ODO_step
                if self.current_odo_value > 21055406:
                    self.current_odo_value = 21055406

                message.data[0] = (self.current_odo_value >> 0) & 0xFF
                message.data[1] = (self.current_odo_value >> 8) & 0xFF
                message.data[2] = (self.current_odo_value >> 16) & 0xFF
                message.data[3] = (self.current_odo_value >> 24) & 0xFF

                try:
                    self.bus.send(message)
                    self.log(f"Sent ODO: {self.current_odo_value}")
                except can.CanError as e:
                    self.log(f"Failed to send ODO message: {e}")

                time.sleep(0.1)

    def reset_fun(self):
        self.log('Resetting device')
        # Add your reset logic here if needed

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
