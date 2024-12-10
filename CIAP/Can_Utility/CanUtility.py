
import tkinter as tk
from tkinter import ttk
import can
import random
import threading
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ATCU AIS -140")
        self.geometry("800x600")

        # Main Frame
        self.frame = ttk.Frame(self)
        self.frame.pack(pady=10)

        # Labels
        self.sampark_label = ttk.Label(self.frame, text="ATCU AIS -140", font=("Times New Roman", 18, "bold"))
        self.sampark_label.pack(pady=(0, 10))

        self.utility_label = ttk.Label(self.frame, text="CAN Utility", font=("Times New Roman", 16, "bold", "underline"))
        self.utility_label.pack(pady=(0, 20))

        self.CanId_label = ttk.Label(self.frame, text="Select CAN Ids:", font=("Times New Roman", 14, "bold"))
        self.CanId_label.pack(anchor=tk.W)

        # Vehicle Id
        self.vehicleId_lbl = ttk.Label(self.frame, text="0x18FEF100", font=("Times New Roman", 12))
        self.vehicleId_lbl.pack(anchor=tk.W)
        self.vehicleId_lbl.bind("<Button-1>", self.select_vehicle)

        self.vehicle_lbl = ttk.Label(self.frame, text="Vehicle Speed", font=("Times New Roman", 12))
        self.vehicle_lbl.pack(anchor=tk.W)

        # Engine Id
        self.engineId_lbl = ttk.Label(self.frame, text="0x0CF00400", font=("Times New Roman", 12))
        self.engineId_lbl.pack(anchor=tk.W)
        self.engineId_lbl.bind("<Button-1>", self.select_engine)

        self.engine_lbl = ttk.Label(self.frame, text="Engine Speed", font=("Times New Roman", 12))
        self.engine_lbl.pack(anchor=tk.W)

        # Odo Id
        self.odoId_lbl = ttk.Label(self.frame, text="0x18FF5117", font=("Times New Roman", 12))
        self.odoId_lbl.pack(anchor=tk.W)
        self.odoId_lbl.bind("<Button-1>", self.select_odo)

        self.odo_lbl = ttk.Label(self.frame, text="VDHR_ODO", font=("Times New Roman", 12))
        self.odo_lbl.pack(anchor=tk.W)

        # Input Fields
        self.input1 = tk.Entry(self.frame)
        self.input1.pack(pady=5)

        self.input2 = tk.Entry(self.frame)
        self.input2.pack(pady=5)

        self.plainTextEdit_3 = tk.Entry(self.frame)
        self.plainTextEdit_3.pack(pady=5)

        # Buttons
        self.start_button = ttk.Button(self.frame, text="START", command=self.start_action)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=20)

        self.stop_button = ttk.Button(self.frame, text="STOP", command=self.stop_action)
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=20)

        # Additional Controls
        self.tcu_lbl = ttk.Label(self.frame, text="TCU Reset", font=("Times New Roman", 12))
        self.tcu_lbl.pack(anchor=tk.W)

        self.tcuID_lbl = ttk.Label(self.frame, text="0x18FEC099", font=("Times New Roman", 12))
        self.tcuID_lbl.pack(anchor=tk.W)

        self.set_rtc_label = ttk.Label(self.frame, text="SET RTC", font=("Times New Roman", 12))
        self.set_rtc_label.pack(anchor=tk.W)

        self.reset_button = ttk.Button(self.frame, text="RESET", command=self.reset_action)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.set_button = ttk.Button(self.frame, text="SET", command=self.set_action)
        self.set_button.pack(side=tk.LEFT, padx=5)

        # Initialize selections
        self.selected_ids = []

        # CAN Bus Initialization
        self.bus = None
        self.initialize_can_bus()

        # Control flags for threading
        self.running_threads = []

    def initialize_can_bus(self):
        """Initialize the CAN bus."""
        try:
            self.bus = can.interface.Bus(channel='PCAN_USBBUS1', interface='pcan', bitrate=500000)
            print("CAN bus initialized successfully.")
        except Exception as e:
            print(f"Failed to initialize CAN bus: {e}")

    def select_vehicle(self, event):
        """Select the vehicle CAN ID."""
        if "0x18FEF100" not in self.selected_ids:
            self.selected_ids.append("0x18FEF100")
            self.vehicleId_lbl.config(foreground='blue')
        else:
            self.selected_ids.remove("0x18FEF100")
            self.vehicleId_lbl.config(foreground='black')

    def select_engine(self, event):
        """Select the engine CAN ID."""
        if "0x0CF00400" not in self.selected_ids:
            self.selected_ids.append("0x0CF00400")
            self.engineId_lbl.config(foreground='blue')
        else:
            self.selected_ids.remove("0x0CF00400")
            self.engineId_lbl.config(foreground='black')

    def select_odo(self, event):
        """Select the ODO CAN ID."""
        if "0x18FEC100" not in self.selected_ids:
            self.selected_ids.append("0x18FF5117")
            self.odoId_lbl.config(foreground='blue')
        else:
            self.selected_ids.remove("0x18FF5117")
            self.odoId_lbl.config(foreground='black')

    def start_action(self):
        print("Start action triggered")
        if "0x18FEF100" in self.selected_ids:
            thread = threading.Thread(target=self.send_vehicle_speed, daemon=True)
            thread.start()
            self.running_threads.append(thread)
        if "0x0CF00400" in self.selected_ids:
            thread = threading.Thread(target=self.send_engine_speed, daemon=True)
            thread.start()
            self.running_threads.append(thread)
        if "0x18FF5117" in self.selected_ids:
            thread = threading.Thread(target=self.send_odo, daemon=True)
            thread.start()
            self.running_threads.append(thread)

    def stop_action(self):
        print("Stop action triggered")
        self.running_threads = []  # Stop all threads by clearing the list

    def reset_action(self):
        print("Reset action triggered")
        self.selected_ids.clear()
        self.vehicleId_lbl.config(foreground='black')
        self.engineId_lbl.config(foreground='black')
        self.odoId_lbl.config(foreground='black')

    def set_action(self):
        print("Set action triggered")
        # Implement set functionality if needed

    def send_vehicle_speed(self):
        while True:
            if self.bus:
                message = can.Message(arbitration_id=0x18FEF100, data=[0] * 8, is_extended_id=True)
                vehicle_speed = random.randint(0, 250)
                message.data[2] = vehicle_speed & 0x00FF
                try:
                    self.bus.send(message)
                    print("Sent Vehicle Speed:", vehicle_speed)
                except can.CanError as e:
                    print(f"Failed to send vehicle speed message: {e}")
            time.sleep(0.1)

    def send_engine_speed(self):
        while True:
            if self.bus:
                message = can.Message(arbitration_id=0x0CF00400, data=[0] * 8, is_extended_id=True)
                engine_speed = random.uniform(501, 600.000)
                scaled_speed = int(engine_speed * 16)
                message.data[3] = scaled_speed & 0x00FF
                message.data[4] = (scaled_speed >> 8) & 0x00FF
                try:
                    self.bus.send(message)
                    print("Sent Engine Speed:", engine_speed)
                except can.CanError as e:
                    print(f"Failed to send engine speed message: {e}")
            time.sleep(0.1)

    def send_odo(self):
        current_odo_value = 0
        while True:
            if self.bus:
                message = can.Message(arbitration_id=0x18FF5117, data=[0] * 8, is_extended_id=True)
                current_odo_value += 5
                message.data[0] = (current_odo_value >> 0) & 0xFF
                message.data[1] = (current_odo_value >> 8) & 0xFF
                message.data[2] = (current_odo_value >> 16) & 0xFF
                message.data[3] = (current_odo_value >> 24) & 0xFF
                try:
                    self.bus.send(message)
                    print(f"Sent ODO: {current_odo_value}")
                except can.CanError as e:
                    print(f"Failed to send ODO message: {e}")
            time.sleep(0.1)

if __name__ == "__main__":
    app = App()
    app.mainloop()

