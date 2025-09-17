import requests
import threading
from queue import Queue
from rich.table import Table
from rich.console import Console
from rich.progress import Progress

console = Console()

def dir_buster(base_url, wordlist_file, threads=30):
    if not base_url.startswith('http'):
        base_url = 'http://' + base_url
    
    try:
        requests.get(base_url, timeout=5)
    except requests.ConnectionError:
        console.print(f"[bold red]Error: Could not connect to {base_url}. Check the URL.[/bold red]")
        return

    q = Queue()
    try:
        with open(wordlist_file, 'r') as f:
            paths = f.read().splitlines()
    except FileNotFoundError:
        console.print(f"[bold red]Error: Wordlist file '{wordlist_file}' not found.[/bold red]")
        return
        
    for path in paths:
        q.put(path)

    found_paths = []
    
    def worker():
        while not q.empty():
            path = q.get()
            url = f"{base_url}/{path}"
            try:
                res = requests.get(url, timeout=5, allow_redirects=False)
                if res.status_code != 404:
                    found_paths.append((res.status_code, url))
            except requests.RequestException:
                pass
            q.task_done()

    for _ in range(threads):
        thread = threading.Thread(target=worker)
        thread.daemon = True
        thread.start()
    
    with Progress(console=console) as progress:
        task = progress.add_task("[cyan]Scanning Web Paths...", total=q.qsize())
        while not q.empty():
            completed_count = q.qsize() - q.unfinished_tasks
            progress.update(task, completed=completed_count * -1)
            time.sleep(0.1)
    
    q.join()

    table = Table(title=f"[bold green]Web Directory Scan Results for {base_url}[/bold green]", style="green")
    table.add_column("Status Code", style="cyan")
    table.add_column("URL", style="magenta")
    
    for status, url in sorted(found_paths):
        table.add_row(str(status), url)
        
    console.print(table)