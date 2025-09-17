from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_banner():
    """Prints the new green FALCON banner."""
    
    BANNER = r"""
███████╗ █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██║     ██╔════╝ ██╔═══██╗████╗  ██║
█████╗  ███████║██║     ██║      ██║   ██║██╔██╗ ██║
██╔══╝  ██╔══██║██║     ██║      ██║   ██║██║╚██╗██║
██║     ██║  ██║███████╗╚██████╗ ╚██████╔╝██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
    """
    
    text = Text(BANNER, style="bold green")
    text.append("\n\n")
    byline = Text.from_markup("[bold cyan]By[/bold cyan][dim]:[/dim] [blue_violet][[/blue_violet][bold green]+[/bold green][blue_violet]][/blue_violet] [bold cyan]Faisal Al-Shrif[/bold cyan]", justify="center")
    text.append(byline)
    
    panel = Panel(
        text,
        title="[bold yellow]Falcon Recon Toolkit[/bold yellow]",
        subtitle="[yellow]v3.5 - World Class[/yellow]",
        style="bold green"
    )
    console.print(panel)