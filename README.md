# 🤣 punput_shaping

Open API comedy for your printer — now shaping for maximum comedic resonance.

[View example output](example.png)

> ⚠️ **Requires** [Kalico](https://docs.kalico.gg/G-Code_Shell_Command.html?h=gcode_shell_command#passing-parameters) or Klipper with [`gcode_shell_command`](https://github.com/dw-0/kiauh/blob/master/docs/gcode_shell_command.md) extension installed.

---

## 📦 Installation

Clone the repository into your Klipper config folder:

```bash
git clone https://github.com/drewgwallace/punput_shaping.git ~/printer_data/config/punput_shaping
```

---

## ⚙️ Setup Instructions

### 1. Include .cfg file

Add this line to your `printer.cfg` to include the repo’s macros and configs:

```ini
[include punput_shaping/punput_shaper.cfg]
```

---

### 2. Choose Your Joke Source

#### 🟢 Online Sources

| Source         | Link                                                  | Description                              |
|------------------|----------------------------------------------------------|------------------------------------------|
| `icanhazdadjoke` | [icanhazdadjoke.com](https://icanhazdadjoke.com/api)     | Classic dad jokes (default)              |
| `officialjoke`   | [Official Joke API](https://github.com/15Dkatz/official_joke_api) | Programming/general jokes       |
| `norris`         | [Chuck Norris API](https://api.chucknorris.io/)          | Random Chuck Norris facts                |
| `jokeapi`        | [JokeAPI](https://jokeapi.dev/)                           | One-liner programming jokes              |

#### 🔵 Offline Mode (No Internet Required)

| Source         | Link                                                  | Description                              |
|------------------|----------------------------------------------------------|------------------------------------------|
| `local` |  [`punput.txt`](punput.txt)     | A collection of 3D Printing puns, jokes, and comments              |

You can edit or replace this file with your own printer-themed puns.

---

### 3. Set the Python Script Path

In `printer.cfg`, customize the path and source:

- `<YOUR_USER>` → your actual username  
- `<YOUR_SOURCE>` → one of the joke sources listed above

```ini
[gcode_shell_command punput]
command: python /home/<YOUR_USER>/printer_data/config/punput_shaping/punput_shaper.py <YOUR_SOURCE>
```

Example using local source, [`punput.txt`](punput.txt):

```ini
[gcode_shell_command punput]
command: python /home/pi/printer_data/config/punput_shaping/punput_shaper.py local
```

---

## 🧪 How to Use


Call the **PunputShaping** macro manually from the Klipper console, or automatically inside another macro like print_start.

For example, adding this loop to the end of your `print_start` macro will automatically run every 15 minutes (by default) while printing:

```ini
[gcode_macro print_start]
gcode:
    ...
    UPDATE_DELAYED_GCODE ID=PunputShaping_Loop DURATION={printer["gcode_macro PunputShaping"].punputshaping_loop_duration}
```

---

## 💡 Tips

### Configure Moonraker

Append the following to your moonraker.conf to enable updates:

```ini
[update_manager punput_shaping]
type: git_repo
origin: https://github.com/drewgwallace/punput_shaping.git
path: ~/printer_data/config/punput_shaping
primary_branch: main
is_system_service: False
managed_services: klipper
```

### 🛠️ Missing Python Library?

You may be missing a required library. Install it with:

```bash
sudo apt install python3-requests  # Debian/Ubuntu-based distros
```

### 🧪 Test the Shell Command or Macro

Run manually from the Klipper console:

```ini
PunputShaping
RUN_SHELL_COMMAND CMD=punput
```

### 🧹 Console Cleanup in Mainsail

Add a console filter to hide command logs:

- Navigate to **Settings → Console → Filters → Add Filter**
- **Name**: `PunputShaper`
- **Regex**: `.*Command \{punput.*\}.*`

### ⏱️ Adjust Loop Frequency

Copy into your `printer.cfg` to set how often the macro runs by overriding `variable_punputshaping_loop_duration` (in seconds):

```ini
[gcode_macro PunputShaping]
variable_punputshaping_loop_duration: 900  # Seconds
gcode:
    RUN_SHELL_COMMAND CMD=punput
```
> ⚠️ **Be cautious of overusing Open API calls!**
