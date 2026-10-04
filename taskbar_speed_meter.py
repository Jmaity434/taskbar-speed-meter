import time
import tkinter as tk
import psutil


class NetworkSpeedMeter:
    def __init__(self, root):
        self.root = root

        # 1. Window size and style (fully transparent background)
        self.root.title("Speed Meter")
        self.root.geometry("90x35+1100+980")  # Small size that fits nicely on the taskbar
        self.root.overrideredirect(True)  # Remove border and title bar
        self.root.wm_attributes("-topmost", True)  # Always stay on top

        # Windows trick: this color becomes fully invisible (transparent)
        transparent_color = "#123456"
        self.root.configure(bg=transparent_color)
        self.root.wm_attributes("-transparentcolor", transparent_color)

        # 2. Speed display text (smaller font size optimized for taskbar)
        self.label = tk.Label(
            self.root,
            text="⬇ 0.0 K\n⬆ 0.0 K",
            font=("Segoe UI", 9, "bold"),  # Windows standard system font
            fg="#FFFFFF",  # White text for easy visibility on the taskbar
            bg=transparent_color,
            justify="left",
        )
        self.label.pack(expand=True, fill="both")

        # 3. Logic to drag the widget onto the taskbar with the mouse
        self.label.bind("<Button-1>", self.start_drag)
        self.label.bind("<B1-Motion>", self.drag)
        self.label.bind("<Double-Button-1>", lambda e: self.root.destroy())  # Double-click to close

        # Reset network counters
        self.last_bytes_recv = psutil.net_io_counters().bytes_recv
        self.last_bytes_sent = psutil.net_io_counters().bytes_sent
        self.last_time = time.time()

        self.update_speed()

    def convert_to_speed_string(self, bytes_per_sec):
        if bytes_per_sec >= 1024 * 1024:
            return f"{bytes_per_sec / (1024 * 1024):.1f} M"
        else:
            return f"{bytes_per_sec / 1024:.1f} K"

    def update_speed(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        if elapsed_time <= 0:
            elapsed_time = 1

        io_counters = psutil.net_io_counters()
        bytes_recv = io_counters.bytes_recv - self.last_bytes_recv
        bytes_sent = io_counters.bytes_sent - self.last_bytes_sent

        download_speed = bytes_recv / elapsed_time
        upload_speed = bytes_sent / elapsed_time

        dl_str = self.convert_to_speed_string(download_speed)
        ul_str = self.convert_to_speed_string(upload_speed)

        # Compact text to save taskbar space
        self.label.config(text=f"⬇ {dl_str}\n⬆ {ul_str}")

        self.last_bytes_recv = io_counters.bytes_recv
        self.last_bytes_sent = io_counters.bytes_sent
        self.last_time = current_time

        self.root.after(1000, self.update_speed)

    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSpeedMeter(root)
    root.mainloop()
