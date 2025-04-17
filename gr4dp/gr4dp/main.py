import argparse
import sys
from gr4dp.cli import cli_main

def main():
    cli_main()

if __name__ == "__main__":
    main()

def cli_main():
    parser = argparse.ArgumentParser("GR4DP Node")
    parser.add_argument("command", choices=["init", "run", "ui"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "init":
        from gr4dp.config import initialize_node
        initialize_node()
    elif args.command == "run":
        from gr4dp.config import run_node
        run_node()
    elif args.command == "ui":
        from gr4dp.ui.server import start_ui
        start_ui()
