import os
import subprocess

# Function to check if Docker is installed and install it if not
def install_docker():
    if not os.path.exists('/usr/bin/docker'):
        print("Docker is not installed. Installing Docker...")
        subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
        subprocess.run(["sudo", "sh", "get-docker.sh"])
        subprocess.run(["sudo", "usermod", "-aG", "docker", os.getlogin()])
        os.remove("get-docker.sh")
        print("Docker has been installed.")

# Function to pull and run MobSF Docker container
def install_mobsf():
    print("Pulling MobSF Docker image...")
    subprocess.run(["docker", "pull", "opensecurity/mobile-security-framework-mobsf"])

    print("Starting MobSF container...")
    subprocess.run(["docker", "run", "-it", "--name", "mobsf", "-p", "8000:8000", "-p", "9090:9090", "opensecurity/mobile-security-framework-mobsf"])

    print("Stopping and removing the MobSF container...")
    subprocess.run(["docker", "stop", "mobsf"])
    subprocess.run(["docker", "rm", "mobsf"])

    print("Deleting MobSF Docker image...")
    subprocess.run(["docker", "rmi", "opensecurity/mobile-security-framework-mobsf"])

# Main function
def main():
    install_docker()
    install_mobsf()

if __name__ == "__main__":
    main()