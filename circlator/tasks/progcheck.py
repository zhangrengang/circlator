import argparse
import sys
from circlator import versions

def run():
    parser = argparse.ArgumentParser(
        description = 'Checks all dependencies are found and are correct versions',
        usage = 'circlator progcheck')
    options = parser.parse_args()
    versions.get_all_versions(sys.stdout)
