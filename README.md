# 🧠 punput_shaping

Open API comedy for your printer — now with perfectly tuned timing.

> ⚠️ **Requires** [Kalico](https://docs.kalico.gg/G-Code_Shell_Command.html?h=gcode_shell_command#passing-parameters) or Klipper with [`gcode_shell_command`](https://github.com/dw-0/kiauh/blob/master/docs/gcode_shell_command.md) extension enabled.

---

## 📦 Installation

Clone the repository into your Klipper configuration directory:

```bash
git clone https://github.com/drewgwallace/punput_shaping.git ~/printer_data/config/punput_shaping
```

Make the Python script executable by running:
> ️ **Run again whenever updating this repository**
```bash
chmod +x ~/printer_data/config/punput_shaping/punput_shaper.py
```

---

## ⚙️ Setup Instructions

### 1. Configure Moonraker

Append the contents of `moonraker.txt` to your `moonraker.conf` or `moonraker.cfg` file to enable shell commands.

> Enable future updates through the update manager.

---

### 2. Set the Python Script Path

In `printer.cfg`, update the `command:` line to match the full path for your user. Example:

```ini
[gcode_shell_command punput]
command: /home/pi/printer_data/config/punput_shaping/punput_shaper.py
```

---

### 3. Choose Your Joke Source

You can select your preferred joke source by **passing an argument** to the G-code shell command.

---

#### 🟢 Online Sources

Update your `printer.cfg` with one of the following arguments at the end of the command:

```ini
[gcode_shell_command punput]
command: /home/user/printer_data/config/punput_shaping/punput_shaper.py icanhaz
```

Replace `icanhaz` with any of the following options:

| Argument   | Source                        | Description                              |
|------------|-------------------------------|------------------------------------------|
| `icanhaz`  | [icanhazdadjoke.com](https://icanhazdadjoke.com/api) | Classic dad jokes (default)             |
| `official` | [Official Joke API](https://github.com/15Dkatz/official_joke_api) | Programming/general jokes               |
| `norris`   | [Chuck Norris API](https://api.chucknorris.io/)      | Random Chuck Norris facts               |
| `jokeapi`  | [JokeAPI](https://jokeapi.dev/)                       | One-liner programming jokes             |

---

#### 🔵 Offline Mode (No Internet Required)

Use the `local` argument to read from a file:

```ini
command: /home/user/printer_data/config/punput_shaping/punput_shaper.py local
```

Place your own jokes (one per line) in:

```
~/printer_data/config/punput_shaping/punput.txt
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

```text
RUN_SHELL_COMMAND CMD=punput
```

In Mainsail, you can add a console filter to hide the command logs for cleaner output:

- Navigate to **Settings → Console → Filters → Add Filter**  
- Name: `PunputShaper`  
- Regex: `.*Command \{punput\}.*`

Update `variable_punputshaping_loop_duration` to use the `delayed_gcode` loop more or less frequently.  
Be cautious of overusing Open API calls!