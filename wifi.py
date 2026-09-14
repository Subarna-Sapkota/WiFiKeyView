import re
import subprocess
import sys


def get_profiles():
    output = subprocess.check_output(
        "netsh wlan show profile",
        shell=True,
        text=True,
        errors="ignore",
    )

    profiles = []
    for line in output.splitlines():
        if "All User Profile" in line:
            parts = line.split(":", 1)
            if len(parts) > 1:
                profiles.append(parts[1].strip())

    return profiles


def get_password(profile_name):
    result = subprocess.check_output(
        f'netsh wlan show profile "{profile_name}" key=clear',
        shell=True,
        text=True,
        errors="ignore",
    )

    match = re.search(r"Key Content\s*:\s*(.+)", result, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    return "Password not found"


profiles = get_profiles()
if not profiles:
    print("No Wi‑Fi profiles found.")
    sys.exit()

for i, profile_name in enumerate(profiles, 1):
    print(f"{i}. {profile_name}")

try:
    ch = int(input("Enter the number of the Wi‑Fi profile to retrieve the password: "))
    if ch < 1 or ch > len(profiles):
        raise ValueError
except ValueError:
    print("Invalid selection.")
    sys.exit()

wifi = profiles[ch - 1]
password = get_password(wifi)

print(f"Wi‑Fi Name: {wifi}")
print(f"Wi‑Fi Password: {password}")

