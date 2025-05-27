# PACS Honeypot System

This project is a Dockerized honeypot system simulating a medical imaging environment. It is built with Orthanc (PACS), Suricata (IDS), Filebeat (log shipper), and Graylog (log analysis UI).

## 🧱 Architecture

- Orthanc: PACS DICOM Server (http://localhost:8042)
- Suricata: Network-based IDS (with custom rules)
- Filebeat: Log collector
- Graylog: Log visualization (http://localhost:9000)

## 🚀 How to use

```bash
git clone https://github.com/Kter1317/pacs-honeypot.git
cd pacs-honeypot
docker-compose up -d --build
