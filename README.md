# Taskbar Network Speed Meter for Windows

**Lightweight, transparent, always-on-top network speed monitor that sits directly on the Windows taskbar.**

A free, open-source Python desktop utility that displays real-time download and upload speeds as a floating transparent widget. Drag it next to the system tray icons (language, network, volume) so it looks like a native part of the Windows taskbar.

---

## Features

- Real-time download (⬇) and upload (⬆) speed
- Fully transparent background (no black box)
- Always-on-top and borderless window
- Drag & drop positioning anywhere on the screen
- Double-click to close
- Extremely lightweight (single .exe with PyInstaller)
- Uses Windows system font (Segoe UI) for native look
- Compact size optimized for taskbar placement

---

## Requirements

- Windows 10 or Windows 11
- Python 3.8 or newer (only needed if you want to run from source)
- Internet connection (for initial package installation)

---

## Installation (Recommended – Build Standalone .exe)

### Step 1: Install Python Dependencies

Open **PowerShell** or **Command Prompt** and run:

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install psutil pyinstaller
```

### Step 2: Build the Executable

Navigate to the project folder and run:

```bash
python -m PyInstaller --noconsole --onefile taskbar_speed_meter.py
```

### Step 3: Run the App

1. After the build finishes, open the newly created `dist` folder.
2. Double-click `taskbar_speed_meter.exe`.
3. You will see only white speed text (no black background).
4. Drag the text with your mouse and place it next to the ENG / Network / Speaker icons on the taskbar.
5. Double-click the text anytime to close the meter.

---

## Run from Source (Development)

```bash
python taskbar_speed_meter.py
```

---

## How It Works (Technical Overview)

1. The window is made completely transparent using the Windows `transparentcolor` attribute.
2. Only the white speed text remains visible.
3. Mouse drag events allow free repositioning.
4. `psutil` reads network I/O counters every second and calculates current speed.
5. Speeds are shown in KB/s or MB/s automatically.

---

## Project Structure

```
taskbar-speed-meter/
├── taskbar_speed_meter.py   # Main application source code
├── requirements.txt         # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This documentation
```

---

## Customization Tips

| What you want to change          | Where to edit                          |
|----------------------------------|----------------------------------------|
| Window size                      | `self.root.geometry("90x35+...")`      |
| Text color                       | `fg="#FFFFFF"` in the Label            |
| Font size / family               | `font=("Segoe UI", 9, "bold")`         |
| Update interval                  | `self.root.after(1000, ...)` (ms)      |
| Transparent color key            | `transparent_color = "#123456"`        |
| Starting position                | Geometry string (x+y coordinates)      |

---

## Troubleshooting

- **Black box still appears**  
  Make sure you are using the latest code that sets `-transparentcolor`.

- **Speeds show 0.0**  
  Check that `psutil` is installed and your network adapter is active.

- **Widget disappears behind other windows**  
  The `-topmost` attribute is already enabled. Restart the app.

- **Want it to start with Windows**  
  Create a shortcut of the `.exe` and place it in the Startup folder  
  (`shell:startup`).

---

## License

MIT License – free for personal and commercial use.

---

## Keywords (SEO)

Windows taskbar network speed meter, real-time download upload monitor, transparent desktop widget, Python psutil tkinter, lightweight system tray alternative, free open source network monitor, Windows 10 11 taskbar gadget, drag and drop speed overlay.

---

**Enjoy a clean, native-looking network speed indicator right on your Windows taskbar!**
