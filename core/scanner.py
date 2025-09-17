import socket
import threading
from queue import Queue
import time
from rich.table import Table
from rich.console import Console

console = Console()

# --- Subdomain Scanner ---
def scan_subdomains(domain, wordlist_file, threads=50):
    found_subdomains = []
    q = Queue()
    
    try:
        with open(wordlist_file, 'r') as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        console.print(f"[bold red]Error: Wordlist file '{wordlist_file}' not found.[/bold red]")
        return

    global target_domain
    target_domain = domain

    for sub in subdomains:
        q.put(sub)

    def worker():
        while not q.empty():
            subdomain = q.get()
            full_url = f"{subdomain}.{target_domain}"
            try:
                ip_address = socket.gethostbyname(full_url)
                found_subdomains.append((full_url, ip_address))
            except socket.gaierror:
                pass
            q.task_done()

    for _ in range(threads):
        thread = threading.Thread(target=worker)
        thread.daemon = True
        thread.start()
    
    q.join()
    
    table = Table(title=f"[bold green]Found Subdomains for {domain}[/bold green]", style="green")
    table.add_column("Subdomain", style="cyan", no_wrap=True)
    table.add_column("IP Address", style="magenta")
    for sub, ip in sorted(found_subdomains):
        table.add_row(sub, ip)
    console.print(table)


# --- Port Scanner ---
def scan_ports(ip, ports_str="1-1024", threads=100):
    open_ports = []
    q = Queue()
    print_lock = threading.Lock()
    
    try:
        start_port, end_port = map(int, ports_str.split('-'))
    except ValueError:
        console.print("[bold red]Error: Invalid port range. Use format like '1-1024'.[/bold red]")
        return
    
    global target_ip
    target_ip = ip
        
    for port in range(start_port, end_port + 1):
        q.put(port)
        
    def worker():
        while not q.empty():
            port = q.get()
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    with print_lock:
                        open_ports.append(port)
                s.close()
            except socket.error:
                pass
            q.task_done()

    for _ in range(threads):
        thread = threading.Thread(target=worker)
        thread.daemon = True
        thread.start()
            
    q.join()

    table = Table(title=f"[bold green]Open Ports on {ip}[/bold green]", style="green")
    table.add_column("Port", style="cyan")
    table.add_column("Status", style="magenta")
    for port in sorted(open_ports):
        table.add_row(str(port), "Open")
    console.print(table)