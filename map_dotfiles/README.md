The dotfiles can be generated using the `dot` executable of graphviz
https://graphviz.org/download/

The `generate.py` script in this directory is meant to make this easy.

If you have graphviz and a sufficient version of python3, it's as easy as

`python generate.py file1.dot file2.dot file3.dot`

The script will update the "updated" stamp in the file, and will render it to svg
in the static folder for use in the web application.