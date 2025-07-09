# 🧠 punput_shaping

Open API comedy for your printer — now with perfectly tuned timing.

---

## 📦 Installation

Clone the repository into your Klipper configuration directory:

```bash
git clone https://github.com/drewgwallace/punput_shaping.git ~/printer_data/config/punput_shaping
```

Make the Python script executable by running:

```bash
chmod +x ~/printer_data/config/punput_shaping/punput_shaper.py
```

---

## ⚙️ Setup Instructions

### 1. Configure Moonraker

Append the contents of `moonraker.txt` to your `moonraker.conf` or `moonraker.cfg` file to enable shell commands.

> This adds the repo commands to Moonraker, enabling updates and shell command support.

---

### 2. Set the Python Script Path

In `printer.cfg`, update the `command:` line to match the full path for your user. Example:

```ini
[gcode_shell_command punput]
command: /home/pi/printer_data/config/punput_shaping/punput_shaper.py
```

---

### 3. Choose Your Joke Source

You have two options for where jokes come from:

#### 🟢 Online (default)

- `punput_shaper.py` fetches a random joke from [icanhazdadjoke.com](https://icanhazdadjoke.com/api).
- You can swap in other APIs (e.g., Official Joke API, Chuck Norris API) by editing the script.

#### 🔵 Offline (no internet required)

- Use `punput_shaper_list.py` instead, which pulls from a local file: `punput.txt`
- Format: one joke per line

Update your command in `punput_shaper.cfg` accordingly:

```ini
command: /home/pi/printer_data/config/punput_shaping/punput_shaper_list.py
```

---

## 🧪 How to Use

Add the `PunputShaping` macro to any G-code script. For example, at the end of your `print_start` macro to run, by default, every 15 minutes as long as the printer is printing:

```ini
[gcode_macro print_start]
gcode:
    ...
    UPDATE_DELAYED_GCODE ID=PunputShaping_Loop DURATION={printer["gcode_macro PunputShaping_Loop"].punputshaping_loop_duration}
```

Also add this line to your `printer.cfg` to include the repo’s macros and configs:

```ini
[include punput_shaping/punput_shaper.cfg]
```

---

## 💡 Tip

To test manually, run from the Klipper console:

```gcode
RUN_SHELL_COMMAND CMD=punput
```

In Mainsail, you can add a console filter to hide the command logs for cleaner output:

- Navigate to **Settings → Console → Filters → Add Filter**  
- Name: `PunputShaper`  
- Regex: `.*Command \{punput\}.*`
