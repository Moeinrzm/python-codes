import subprocess
try:
    output = subprocess.check_output("speedtest-cli", shell=True, universal_newlines=True)
    print(output)
except subprocess.CalledProcessError as e:
    print(f"system error {e}")    