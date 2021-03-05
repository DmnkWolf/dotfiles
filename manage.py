import pathlib
import subprocess


CONFIG_FILES = [
        r".config/i3",
        r".config/i3status",
        r".config/termite",
        r".Xresources"
        ]


for config in CONFIG_FILES:
    path = pathlib.Path.home() / config
    target_path = pathlib.Path("./")
    subprocess.run(["cp", "-r", path, target_path])
