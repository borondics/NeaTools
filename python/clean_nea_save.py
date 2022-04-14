# This script will clean up the Neaspec saved folders from a lot of unnecessary files. If they are needed, re-export the project.
# TODO: solve the long path string problem
import os
import argparse

# argument parsing
parser = argparse.ArgumentParser()

parser.add_argument("--directories")
parser.add_argument("--dry-run", choices=('True', 'False'), default=False)

args = vars(parser.parse_args())

mydirs = args['directories']
dry_run = args['dry_run'] == 'True'

k=0

test = [' R-O0A', ' R-O1A', ' R-O2A', ' R-O3A', ' R-O4A', 'O5A', 
        ' R-O0P', ' R-O1P', ' R-O2P', ' R-O3P', ' R-O4P', 'O5P', 
        ' R-M0A', ' R-M1A', 'M2A', 'M3A', 'M4A', 'M5A', 
        ' R-M0P', ' R-M1P', 'M2P', 'M3P', 'M4P', 'M5P',
        ' R-Z', ' R-Z C', ' R-M', ' R-EA', ' R-EP']

for d in mydirs:
    for root, dirs, files in os.walk(d):
        print(root)
        for name in files:
            if any(s in name for s in test):
                k+=1
                if not dry_run:
                    try:
                        os.remove(os.path.join(root, name))
                    except FileNotFoundError as e:
                        print('ERROR: ', e)

print(f'\nRemoved {k} files')
