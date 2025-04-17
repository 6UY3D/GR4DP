import click
from gr4dp.config import initialize_node, run_node
from gr4dp.ui.server import start_ui

@click.group()
def cli():
    pass

@cli.command()
def init():
    initialize_node()

@cli.command()
def run():
    run_node()

@cli.command()
def ui():
    start_ui()

if __name__ == "__main__":
    cli()
