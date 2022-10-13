#! /usr/bin/env python3

import argparse
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path
import shlex

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Utility to update the date and render the dotfiles.')
    parser.add_argument('dotfiles', nargs='+', help="Names of dotfiles to be rendered")
    args = parser.parse_args()

    if shutil.which('dot') is None:
        print('You need to install graphviz on your system to use this utility. '
              'Visit https://graphviz.org/download/\nExiting...')
        sys.exit(1)

    script_dir = Path(__file__).parent
    output_dir = script_dir.parent / 'dart_data' / 'static' / 'img' / 'ring_maps'

    for _path in args.dotfiles:
        print(f"Updating {_path} and rendering {Path(_path).with_suffix('.svg')}")
        content = Path(_path).read_text()
        pattern = re.compile('updated [0-9]{4}-[0-9]+-[0-9]+')
        mat = pattern.search(content)
        if mat is None:
            print(f"Can't find the date stamp to updated. Did you make it deviate from this? [{pattern.pattern}]")
        else:
            with open(_path, 'w') as f:
                f.write(re.sub(pattern, f'updated {date.today()}', content))

        output_file = (output_dir / _path).with_suffix('.svg')
        with open(output_file, 'w') as f:
            proc = subprocess.run(shlex.split(f'dot -Tsvg {_path}'), stdout=f, stderr=subprocess.PIPE)
        try:
            proc.check_returncode()
        except subprocess.CalledProcessError:
            print(f'dot invocation failed for {_path} as follows:\n{proc.stderr.decode("utf8")}\nFix the dotfile.')

    print(f'Rendered graphs written to {output_dir}')
