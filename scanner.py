import socket
import time

TARGET = "scanme.nmap.org"
PORTS = [21, 22, 23, 80, 443, 8080]

print(f"""
╔══════════════════════════════════════╗
║         DARK SCANNER v1.0            ║
║         Not just code. A mindset.    ║
╚══════════════════════════════════════╝
""")

print(f"  [*] Target  : {TARGET}")
print(f"  [*] Ports   : {len(PORTS)} selected")
print(f"  [*] Status  : Initializing...\n")
time.sleep(1)

print("  [~] Scanning...\n")

for port in PORTS:
    time.sleep(0.4)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((TARGET, port))
        if result == 0:
            print(f"  [+] Port {port:>5}  →  OPEN   ✓")
        else:
            print(f"  [-] Port {port:>5}  →  closed")
        s.close()
    except Exception:
        print(f"  [!] Port {port:>5}  →  error")

print(f"""
  [✓] Scan complete.
  [~] "See what others can't."
""")
