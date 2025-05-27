from orthanc import *
import time

def OnLoad():
    LogInfo("[PLUGIN] Python plugin has been loaded.")
    with open("/tmp/hl7_plugin_loaded.txt", "w") as f:
        f.write("Loaded at " + time.ctime() + "\n")

'''
import socket
import threading

def start_hl7_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 2575))
    server.listen(5)
    print("[*] HL7 Listener started on port 2575")
    while True:
        conn, addr = server.accept()
        print(f"[+] Connection from {addr}")
        conn.close()

def OnLoad():
    threading.Thread(target=start_hl7_listener, daemon=True).start()


import socket
import threading
from hl7apy.parser import parse_message
import requests

def handle_hl7_connection(conn, addr):
    print(f"[+] HL7 connection from {addr}")
    data = b''
    while True:
        packet = conn.recv(1024)
        if not packet:
            break
        data += packet

    message = data.decode('utf-8').strip().replace('\x0b', '').replace('\x1c\r', '')
    print(f"[HL7 Raw]:\n{message}\n")

    try:
        hl7 = parse_message(message)
        patient_id = hl7.pid.patient_identifier_list[0].cx_1.value
        patient_name = hl7.pid.patient_name[0].family_name.fn_1.value

        response = requests.post('http://127.0.0.1:8042/patients', json={
            "PatientID": patient_id,
            "MainDicomTags": {
                "PatientName": patient_name
            }
        })
        print(f"Orthanc API response: {response.status_code}")
    except Exception as e:
        print(f"[!] Error: {e}")

    conn.close()

def start_hl7_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 2575))  
    server.listen(5)
    print("[*] HL7 Listener started on port 2575")
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_hl7_connection, args=(conn, addr))
        client_thread.start()

def OnLoad():
    import threading
    threading.Thread(target=start_hl7_listener, daemon=True).start()
'''
