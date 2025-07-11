# 🤣 punput_shaping

Open API comedy for your printer — now with perfectly tuned timing.

> ⚠️ **Requires** [Kalico](https://docs.kalico.gg/G-Code_Shell_Command.html?h=gcode_shell_command#passing-parameters) or Klipper with [`gcode_shell_command`](https://github.com/dw-0/kiauh/blob/master/docs/gcode_shell_command.md) extension installed.

---

## 📦 Installation

Clone the repository into your Klipper configuration directory:

```bash
git clone https://github.com/drewgwallace/punput_shaping.git ~/printer_data/config/punput_shaping
```

---

## ⚙️ Setup Instructions

### 1. Configure Moonraker

Append to your `moonraker.conf` to enable updates.

```ini
[update_manager punput_shaping]
type: git_repo
origin: https://github.com/drewgwallace/punput_shaping.git
path: ~/printer_data/config/punput_shaping
primary_branch: main
is_system_service: False
managed_services: klipper
```

Enable future updates through the update manager.

---

### 2. Choose Your Joke Source

Choose your preferred joke source by **passing an argument** to the G-code shell command.

---

#### 🟢 Online Sources

Create a macro in `printer.cfg` with a `RUN_SHELL_COMMAND` to one of the available commands.  
There is an example in `punput_shaper.cfg`:

```ini
[gcode_macro PunputShaping]
variable_punputshaping_loop_duration: 900  # 15 minutes default
gcode:
    RUN_SHELL_COMMAND CMD=punput_icanhazdadjoke
```

Replace `icanhazdadjoke` with any of the following options:

| Argument         | Source                                                  | Description                              |
|------------------|----------------------------------------------------------|------------------------------------------|
| `icanhazdadjoke` | [icanhazdadjoke.com](https://icanhazdadjoke.com/api)     | Classic dad jokes (default)              |
| `officialjoke`   | [Official Joke API](https://github.com/15Dkatz/official_joke_api) | Programming/general jokes       |
| `norris`         | [Chuck Norris API](https://api.chucknorris.io/)          | Random Chuck Norris facts                |
| `jokeapi`        | [JokeAPI](https://jokeapi.dev/)                           | One-liner programming jokes              |

---

#### 🔵 Offline Mode (No Internet Required)

Use the `local` argument to read from a file:

```ini
[gcode_macro MyCustomMacro]
gcode:
    RUN_SHELL_COMMAND CMD=punput_local
```

Place your own jokes (one per line) in:

```
~/printer_data/config/punput_shaping/punput.txt
```

---

### 3. Set the Python Script Path

In `printer.cfg`, update the `command:` line to match the full path for your user. Example:

```ini
[gcode_shell_command punput_icanhazdadjoke]
command: /home/**<YOUR_USER>**/printer_data/config/punput_shaping/punput_shaper.py icanhazdadjoke
```

---

## 🧪 How to Use

First, add this line to your `printer.cfg` to include the repo’s macros and configs:

```ini
[include punput_shaping/punput_shaper.cfg]
```

Then, add the `PunputShaping` macro to any G-code script.

For example, adding this loop to the end of your `print_start` macro will automatically run every 15 minutes (by default) while printing:

```ini
[gcode_macro print_start]
gcode:
    ...
    UPDATE_DELAYED_GCODE ID=PunputShaping_Loop DURATION={printer["gcode_macro PunputShaping_Loop"].punputshaping_loop_duration}
```

---

## 💡 Tips

### 🛠️ Missing Python Library?

You may be missing a required library. Install it with:

```bash
sudo apt install python3-requests  # Debian/Ubuntu-based distros
```

### 🧪 Test the Macro

Run manually from the Klipper console:

```gcode
RUN_SHELL_COMMAND CMD=punput
```

### 🧹 Console Cleanup in Mainsail

Add a console filter to hide command logs:

- Navigate to **Settings → Console → Filters → Add Filter**
- **Name**: `PunputShaper`
- **Regex**: `.*Command \{punput\}.*`

### ⏱️ Adjust Loop Frequency

Adjust `variable_punputshaping_loop_duration` to change how often the macro runs:

```ini
[gcode_macro PunputShaping]
variable_punputshaping_loop_duration: 900  # Seconds
    ...
```

> ⚠️ **Be cautious of overusing Open API calls!**
