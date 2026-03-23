# 🚀Python Network Scanner

A multithreaded network scanner built in Python to identify open TCP ports and associated services on a target system.
Designed to demonstrate network reconnaissance and basic security scanning techniques used in real-world environments.

---

## 📌Overview
This tool performs TCP port scanning by attempting socket connections to a target host. Open ports are identified and mapped to common services, helping understand exposed network surfaces.

---

## 🎯Features
- Scan custom port ranges
- Detect open TCP ports
- Identify common services (HTTP, FTP, SSH, etc.)
- Multithreaded scanning for faster performance
- Save scan results to a file

---

## 🛠️Technology Stack
Language: Python
Concepts: Socket Programming, Multithreading, Networking

---

## ⚙️How It Works
1. Accepts target IP/domain and port range
2. Creates multiple threads for faster scanning
3. Attempts TCP connection on each port
4. Identifies open ports
5. Maps ports to common services
6. Saves results to file

---

## 📂Project Structure
python-network-scanner/
│
├── Outputs.pdf
├── README.md
├── scan_results.txt
├── scanner.py

---

## 📊Output
1. List of open ports
2. Identified services
3. Saved scan results (scan_results.txt)

---

## 🔐Use Cases
- Network reconnaissance
- Basic vulnerability assessment
- Understanding exposed services
- Learning SOC-level scanning techniques

---

## 📈Learning Outcomes
Port scanning techniques
Multithreading in Python
TCP socket communication
Network service identification

---

## 📸Screenshots
Outouts.pdf

▶️ Usage

## Run the script:
python scanner.py

---

# 👤Author

Vijaya
SOC Analyst (Aspiring) | Network Security | Python | Threat Intelligence
