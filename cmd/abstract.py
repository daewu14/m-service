import argparse


class AbstractCommand:
    name: str
    description: str
    help: str

    def sub(self, parser: argparse.ArgumentParser):
        pass

    def run(self, parser: argparse.ArgumentParser):
        pass
