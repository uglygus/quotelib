#  installation guide


Taken from here:
https://packaging.python.org/tutorials/packaging-projects/

install the necessary tools
`python3 setup.py sdist bdist_wheel`



`cd` to root of this package
`pip3 install --user .`


pip might get confused if this is built using files from a previous iteration of this module. Clear Pips cache to fix that.

`rm -dr ~/Library/Caches/pip`

