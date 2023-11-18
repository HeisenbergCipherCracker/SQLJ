import subprocess

try:
    result = subprocess.run(['python', 'SQLJng.py'], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e.stderr}")
