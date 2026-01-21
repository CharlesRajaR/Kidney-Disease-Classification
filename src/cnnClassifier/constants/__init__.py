from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

print(Path().cwd())

print(f"Target path: {CONFIG_FILE_PATH}")
print(f"Exists: {CONFIG_FILE_PATH.exists()}")


print(f"Target path: {PARAMS_FILE_PATH}")
print(f"Exists: {PARAMS_FILE_PATH.exists()}")