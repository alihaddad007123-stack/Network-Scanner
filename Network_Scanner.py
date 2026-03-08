import socket
import threading
target=input("Enter the ip target :")
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}
lock=threading.Lock()
print(f"Scanning {target} ....\n")
report=open("scan_report.txt","w")
def scan(port):
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.settimeout(1)
          print(f"Scanning {port} ....\n")
          result = s.connect_ex((target, port))
          if result == 0:
              service = services.get(port, "Unknown")
              result_text = f"Port {port} OPEN ({service})"
              print(result_text)
              with lock:
                   report.write(result_text + "\n")
          s.close()
threads=[]
for port in services:
    t=threading.Thread(target=scan,args=(port,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
report.close()
print("Scan completed. Results saved in scan_report.txt")