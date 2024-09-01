import subprocess
import re

def get_microphone_device():
    result = subprocess.run(
        ["ffmpeg", "-list_devices", "true", "-f", "dshow", "-i", "dummy"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    devices = result.stdout
    microphone_match = re.search(r'"([^"]*Mikrofon[^"]*)"', devices)
    return microphone_match.group(1) if microphone_match else None
