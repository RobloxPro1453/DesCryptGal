
from os import name,system
from prompt_toolkit import styles
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    SpinnerColumn,
)

def clear():
    system('cls' if name == 'nt' else 'clear')



def CliStatus(msg,hide=True):
    prg = Progress(
        SpinnerColumn("bouncingBar"),
        TextColumn("[cyan]"+msg),
        BarColumn(bar_width=40),
        transient=hide)
    prg.add_task(msg, total=None)
    return prg



prompt_tema = styles.Style([
    ('qmark', 'fg:#5F819D bold'),
    ('question', 'fg:#289c64 bold'),
    ('answer', 'fg:#48b5b5 bg:#hidden bold'),
    ('pointer', 'fg:#48b5b5 bold'),
    ('highlighted', 'fg:#07d1e8'),
    ('selected', 'fg:#48b5b5 bg:black bold'),
    ('separator', 'fg:#6C6C6C'),
    ('instruction', 'fg:#77a371'),
    ('text', ''),
    ('disabled', 'fg:#858585 italic'),
])