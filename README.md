# Falcon Recon Toolkit

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Rich CLI](https://img.shields.io/badge/Rich_CLI-FFD700?style=for-the-badge&logo=rich&logoColor=black)

A multi-tool interactive command-line interface for network reconnaissance, built with Python and styled with Rich for a modern, professional user experience.

أداة سطر أوامر تفاعلية متعددة الوظائف مخصصة لاستكشاف الشبكات، تم بناؤها باستخدام بايثون ومكتبة Rich لواجهة مستخدم عصرية واحترافية.

---

##  Demo

<img width="1920" height="1080" alt="falcon-toolkit" src="https://github.com/user-attachments/assets/22dde935-0c8d-49f5-9f51-10a116a4e397" />



---

## Key Features

- **Interactive Shell**: A user-friendly shell that accepts commands directly.
- **Multi-threaded Scanning**: All tools are built for maximum speed.
- **Professional UI**: Uses Rich to display results in clean tables and show live progress bars.
- **Modular Codebase**: Structured for easy maintenance and future expansion.

---

## Available Tools

The toolkit currently includes the following modules:

1.  **Subdomain Scanner**: Discovers subdomains for a target domain using a wordlist.
2.  **Port Scanner**: Scans a target IP for open TCP ports.
3.  **Web Directory Scanner**: Finds hidden directories and files on a web server.

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/F9-0/falcon-toolkit.git](https://github.com/F9-0/falcon-toolkit.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd falcon-toolkit
    ```
3.  **Create and activate a virtual environment:**
    - On Windows (PowerShell):
      ```powershell
      python -m venv venv
      .\venv\Scripts\Activate
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

First, run the main script to start the interactive shell:
```bash
python falcon.py
