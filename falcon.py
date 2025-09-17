from rich.console import Console
from core.banner import print_banner
from core.scanner import scan_subdomains, scan_ports
from core.web_recon import dir_buster

console = Console()

def interactive_shell():
    """The main interactive shell loop."""
    print_banner()
    while True:
        try:
            command = console.input("\n[bold blue]falcon > [/bold blue]")
            parts = command.split()
            cmd = parts[0].lower() if parts else ""

            if cmd in ["exit", "quit"]:
                console.print("[bold yellow]Exiting Falcon Toolkit. Goodbye![/bold yellow]")
                break
            elif cmd == "help":
                # Print help menu
                pass
            elif cmd == "subdomain":
                if len(parts) == 3:
                    scan_subdomains(domain=parts[1], wordlist_file=parts[2])
                else:
                    console.print("[bold red]Usage: subdomain <domain> <wordlist_file>[/bold red]")
            elif cmd == "portscan":
                if len(parts) >= 2:
                    ports = parts[2] if len(parts) == 3 else "1-1024"
                    scan_ports(ip=parts[1], ports_str=ports)
                else:
                    console.print("[bold red]Usage: portscan <ip_address> [port_range][/bold red]")
            elif cmd == "dirscan":
                if len(parts) == 3:
                    dir_buster(base_url=parts[1], wordlist_file=parts[2])
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