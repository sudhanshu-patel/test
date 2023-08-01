import subprocess

def run_objection_command(command):
    """
    Function to run Objection command and return the output.
    """
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True)
        return result.stdout.strip()
    except FileNotFoundError:
        return "Error: Objection not found. Please ensure Objection is installed and added to your system PATH."

def android_list_apps():
    """
    List installed applications on the connected Android device.
    """
    return run_objection_command("objection android hooking list applications")

def android_bypass_ssl_pinning(package_name):
    """
    Bypass SSL Pinning for the specified Android app.
    """
    return run_objection_command(f"objection android sslpinning disable {package_name}")

def ios_list_apps():
    """
    List installed applications on the connected iOS device.
    """
    return run_objection_command("objection ios hooking list applications")

def ios_dump_keychain():
    """
    Dump keychain data from the connected iOS device.
    """
    return run_objection_command("objection ios keychain dump")

if __name__ == "__main__":
    print("Welcome to the simplified Objection script!")

    while True:
        print("\nAvailable options:")
        print("1. List installed apps on Android")
        print("2. Bypass SSL Pinning for Android app")
        print("3. List installed apps on iOS")
        print("4. Dump keychain data from iOS")
        print("0. Exit")

        choice = input("Enter the option number: ")

        if choice == "1":
            android_apps_output = android_list_apps()
            print(android_apps_output)
        elif choice == "2":
            package_name = input("Enter the package name of the Android app: ")
            bypass_ssl_output = android_bypass_ssl_pinning(package_name)
            print(bypass_ssl_output)
        elif choice == "3":
            ios_apps_output = ios_list_apps()
            print(ios_apps_output)
        elif choice == "4":
            keychain_output = ios_dump_keychain()
            print(keychain_output)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")