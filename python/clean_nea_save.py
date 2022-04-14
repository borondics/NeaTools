# This script will clean up the Neaspec saved folders from a lot of unnecessary files. If they are needed, re-export the project.
import os
import argparse

# argument parsing
parser = argparse.ArgumentParser()

parser.add_argument("--dry-run", action='store_true')

parser.add_argument('-d', '--directories', action='store', dest='directories',
                    type=str, nargs='*', required=True,
                    help="Example: -d dir1 dir2, -i dir3")

args = vars(parser.parse_args())

mydirs = args['directories']
dry_run = args['dry_run']

k=0

# TODO could be done with a nice complex RegEx?
testF = [' R-O0A', ' R-O1A', ' R-O2A', ' R-O3A', ' R-O4A', 'O5A', 
        ' R-O0P', ' R-O1P', ' R-O2P', ' R-O3P', ' R-O4P', 'O5P', 
        ' R-M0A', ' R-M1A', 'M2A', 'M3A', 'M4A', 'M5A', 
        ' R-M0P', ' R-M1P', 'M2P', 'M3P', 'M4P', 'M5P',
        ' R-Z', ' R-Z C', ' R-M', ' R-EA', ' R-EP']

for d in mydirs:
    print(d)
    for root, dirs, files in os.walk(d):
        print(f'Current directory: {root}')
        for name in files:
            if any(s in name for s in testF):
                k+=1
                if not dry_run:
                    try:
                        os.remove(os.path.join(root, name))
                        # TODO: solve the long path string problem
                        # TODO: deleting is not extremely fast - could be vectorized?

                    except FileNotFoundError as e:
                        print('ERROR: ', e)

if dry_run:
    print(f'\n{k} file{"s" if k>1 else ""} can be removed.')
else:
    print(f'\nRemoved {k} file{"s" if k>1 else ""}')

