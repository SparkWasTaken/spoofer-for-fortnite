import subprocess
import random
import string

def generate_hwid():
    # Generate a random 16 character string of upper and lowercase letters, and numbers
    hwid = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return hwid

def spoof_hwid():
    # Generate a new random HWID
    new_hwid = generate_hwid()

    # Use the subprocess module to run the command to change the HWID
    command = f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001" /v HwProfileGuid /t REG_SZ /d {new_hwid} /f'
    subprocess.run(command, shell=True)

# Show the banner
print("\033[0;35m\n                                                    _____             ")
print("___  __ ____ ___  ___   ____________   ____   _____/ ____\___________ ")
print("\\  \\/ // __ \\\\  \\/  /  /  ___/\\____ \\ /  _ \\ /  _ \\   __\\/ __ \\_  __ \\")
print(" \\   /\\  ___/ >    <   \\___ \\ |  |_> >  <_> |  <_> )  | \\  ___/|  | \/")
print("  \\_/  \\___  >__/\\_ \\ /____  >|   __/ \\____/ \\____/|__|  \\___  >__|   ")
print("           \\/      \\/      \\/ |__|                           \\/       \n\033[0m")

# Ask for user input
print("\033[0;35m[1] spoofer\033[0m")
option = input("Select an option: ")

# Execute the selected option
if option == "1":
    spoof_hwid()
    print("\033[0;35mdone!\033[0m")
else:
    print("\033[0;35mInvalid option.\033[0m")
