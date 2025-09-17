import time
from rich.console import Console
from rich.table import Table
from core.banner import print_banner
from core.scanner import scan_subdomains, scan_ports
from core.web_recon import dir_buster

console = Console()

def print_help():
    table = Table(title="[bold yellow]Falcon Toolkit Help Menu[/bold yellow]", style="yellow")
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Arguments", style="magenta")
    table.add_column("Description", style="white")
    
    table.add_row("subdomain", "<domain> <wordlist_file>", "Scans for subdomains using a wordlist.")
    table.add_row("portscan", "<ip_address> [port_range]", "Scans a target for open ports. Port range is optional.")
    table.add_row("dirscan", "<base_url> <wordlist_file>", "Scans a web URL for directories and files.")
    table.add_row("help", "", "Displays this help menu.")
    table.add_row("clear / cls", "", "Clears the terminal screen.")
    table.add_row("exit / quit", "", "Exits the application.")
    
    console.print(table)

def interactive_shell():
    print_banner()
    while True:
        try:
            command = console.input("\n[bold blue]falcon > [/bold blue]")
            parts = command.split()
            cmd = parts[0].lower() if parts else ""

            if cmd in ["exit", "quit"]:
                console.print("[bold yellow]Exiting Falcon Toolkit. Goodbye![/bold yellow]")
                break
            
            start_time = time.time()
            
            if cmd == "help":
                print_help()
            elif cmd == "subdomain":
                if len(parts) == 3:
                    scan_subdomains(domain=parts[1], wordlist_file=parts[2])
                    end_time = time.time()
                    console.print(f"\n[bold]Subdomain scan completed in {end_time - start_time:.2f} seconds.[/bold]")
                else:
                    console.print("[bold red]Usage: subdomain <domain> <wordlist_file>[/bold red]")
            elif cmd == "portscan":
                if len(parts) >= 2:
                    ports = parts[2] if len(parts) == 3 else "1-1024"
                    scan_ports(ip=parts[1], ports_str=ports)
                    end_time = time.time()
                    console.print(f"\n[bold]Port scan completed in {end_time - start_time:.2f} seconds.[/bold]")
                else:
                    console.print("[bold red]Usage: portscan <ip_address> [port_range][/bold red]")
            elif cmd == "dirscan":
                if len(parts) == 3:
                    dir_buster(base_url=parts[1], wordlist_file=parts[2])
                    end_time = time.time()
                    console.print(f"\n[bold]Directory scan completed in {end_time - start_time:.2f} seconds.[/bold]")
                else:
                    console.print("[bold red]Usage: dirscan <base_url> <wordlist_file>[/bold red]")
            elif cmd in ["clear", "cls"]:
                 console.clear()
                 print_banner()
            elif cmd == "":
                 pass
            else:
                console.print(f"[bold red]Unknown command: '{cmd}'. Type 'help' for a list of commands.[/bold red]")

        except KeyboardInterrupt:
            console.print("\n[bold yellow]Exiting Falcon Toolkit. Goodbye![/bold yellow]")
            break

if __name__ == "__main__":
    interactive_shell()