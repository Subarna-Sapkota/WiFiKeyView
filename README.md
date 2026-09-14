# WiFiKeyView

WiFiKeyView is a lightweight Python script for Windows that lists saved Wi‑Fi profiles and lets you select one to reveal its stored password.

The project uses the built-in `netsh wlan` command to read saved wireless profile details from the system.

## Features

- Lists all saved Wi‑Fi profiles on the current Windows machine
- Lets the user choose a profile by number
- Displays the selected Wi‑Fi network name
- Shows the saved password for that profile
- Runs from the command line with no external dependencies

## Requirements

- Windows operating system
- Python 3 installed

## How to Run

1. Open PowerShell or Command Prompt.
2. Navigate to the project directory:

    ```bash
    cd path
    ```

3. Run the script:

    ```bash
    python wifi.py
    ```

4. Select a Wi‑Fi profile from the list.
5. The program will print the network name and its saved password.

## Example

```text
1. HomeWiFi
2. OfficeNetwork
3. CafeGuest
Enter the number of the Wi‑Fi profile to retrieve the password: 1
Wi‑Fi Name: HomeWiFi
Wi‑Fi Password: ********
```

## Notes

- This script only works with Wi‑Fi profiles already saved on the current Windows machine.
- It is intended for legitimate local network troubleshooting and profile management.
- Use responsibly and only on systems you own or are authorized to inspect.
