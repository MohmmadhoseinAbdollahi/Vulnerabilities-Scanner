# This is the main file that will be executed to run the scanning program.
import os
import subprocess
from Dockerscanvul import DockerScanner
from TestingURLScanner import LocalhostServiceScanner
from ScanVul import identify_vulnerabilities
from Testingsitescanner import Scan_tech
def main():
    print("Welcome to the scanning program!")
    print("Please select the scanning environment:")
    print("1. Docker")
    print("2. Localhosts")
    print("3. Websites")
    print("4. Open README.md file")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Check if docker is installed
        if os.system("docker --version") != 0:
            print("Docker is not installed. Please install Docker and try again.")
            main()
            
        # Check if trivy is installed
        if os.system("trivy --version") != 0:
            print("Trivy is not installed. Please install Trivy and try again.")
            main()
            
        # Show all networks
        subprocess.run(["docker", "network", "ls"])
        print()
        network_name = input("Enter the network name: ")
        # check if network exists
        if os.system(f"docker network inspect {network_name}") != 0:
            print(f"Network {network_name} does not exist. Please try again.")
            main()
        DockerScanner(network_name)
        print("Scanning completed!")
        print("Please check the generated PDF files for the scan results.")
        print("But, If you want to see what is inside container prees 1 else press 2")
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            print("wait for this part")
            print()
            main()
        else:
            print("ok")
            main()
            
    elif choice == "2":
        url = input("Enter the URL: ")
        # Check if the URL is valid
        if not url.startswith("http://") and not url.startswith("https://") and not url.startswith("localhost"):
            print("Invalid URL. Please enter a valid URL starting with 'http://' or 'https://'.")
            main()
        services = LocalhostServiceScanner(url)
        identify_vulnerabilities(services, url)
        print("Scanning completed!")
        print("But, If you want to see what is inside site prees 1 else press 2")
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            print("wait for this part")
            print()
            main()
        else:
            print("ok")
            main()

    elif choice == "3":
        url = input("Enter the URL: ")3
        # Check if the URL is valid
        if not url.startswith("http://") and not url.startswith("https://") and not url.startswith("localhost"):
            print("Invalid URL. Please enter a valid URL starting with 'http://' or 'https://'.")
            main()
        
        technologies = Scan_tech(url)
        identify_vulnerabilities(technologies,url)
        print("Scanning completed!")
        input("Press Enter to back menu...")
        main()
        
    elif choice == "4":
        os.system("cat README.md")
        main()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        return

    else:
        print("Invalid choice. Please try again.")
        return

if __name__ == "__main__":
    main()