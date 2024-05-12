# Vulnerabilities Scanner
Security Assignment

This is the README file for the security assignment.

## Project Description

The project is a security assignment that aims to implement a program for identifying vulnerabilities by using the extracted version of services which found by the program.

## Files

The project folder contains the following files:

- `Main.py`: This is the main entry point of the program. It serves as the starting point for executing the program.
- `Dockerscanvul.py`: This file contains the implementation of a vulnerability scanning tool specifically designed for Docker containers. It includes various security checks and tests to identify potential vulnerabilities in Docker images and containers. The tool can be used to assess the security posture of Docker deployments and help identify and mitigate security risks.
- `TestingURLScanner.py`: This file contains the implementation of a URL scanner for testing purposes. It is responsible for finding services throw the localhosts.
- `Testingsitescanner.py`: This file contains the implementation of scan a given URL and detect the technologies used in the frontend of the website. It does this by fetching the HTML of the page and then parsing it to find clues about the technologies used.
- `ScanVul.py`:This file  used to identify vulnerabilities in a given website, particularly those that use WordPress. It uses the vulners API and wpscan tool to perform the vulnerability scanning.
- `CmsversionFinder.py`:This file  used to designed to detect the version of a Content Management System (CMS) used by a website.
- `CmsversionFinder.py`:This file  used to designed to detect the version of a Content Management System (CMS) used by a website.
- `PredictTheDatabaseVersion.py`:the file is a set of functions that work together to determine the most compatible database for a given CMS (Content Management System) version with `compatibility_table.csv`.
- `Convert.py`:the file designed to convert text files (.txt) into PDF files (.pdf). It consists of two main functions: convert_txt_to_pdf and Convert.

## Usage

To use the program, follow these steps:


1. Install these libraries :

    - `requests`: This library is used for making HTTP requests.

    - `beautifulsoup4`: This library is used for parsing HTML and XML documents. It creates parse trees that are helpful to extract the data easily.
    ```bash
    pip install requests beautifulsoup4
    ```
    - `re`: This is a built-in Python module used for working with regular expressions.

    - `fpdf`: This library is used for creating PDF files in Python.
    ```bash
    pip install fpdf
    ```
    - `os`: This is a built-in Python module for interacting with the operating system.

    - `subprocess`: This is a built-in Python module for spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes.

    - `json`: This is a built-in Python module for working with JSON data.

    - `Docker`: This is not a Python library, but a platform that uses OS-level virtualization to deliver software in packages called containers. The code uses Docker commands, so Docker needs to be installed on the machine where this code will run.
    Docker: https://docs.docker.com/get-docker/
    
    - `Trivy`: This is a simple and comprehensive vulnerability scanner for containers. The code uses the trivy command, so Trivy needs to be installed on the machine where this code will run.
    Trivy: https://github.com/aquasecurity/trivy#installation

    - `vulners`: This library is used for interacting with the Vulners Database API to search for vulnerabilities.(need api token which you can get from their site with 100 credit for free)
    ```bash
    pip install vulners
    ```

    - `WPScan`: This is not a Python library, but a black box WordPress vulnerability scanner. The code uses the wpscan command, so WPScan needs to be installed on the machine where this code will run.
    (need api token which you can get from their site for free)

2. Run the program by running following file:
    ```
    Main.py 
    ```
3. in "Output" folder, you can see the files that containing the vulnerabilities of the services that were running in the provided url or docker network in .txt and .pdf style."some file provided for sample for running the program by yourself delete all files in the "output" folder. 


## Contributing

The project defined by [@auino](https://github.com/auino), our professor in security studies .

## License


## Contact

If you have any questions or suggestions regarding the project, please contact the project maintainer at [@mohiabd99](https://github.com/Mohiabd99).
