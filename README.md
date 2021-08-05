# PYURLCHECK

Project is currently a **WIP**.

`pyurlcheck` can be used to scan through all of a projects documents and validate any `public` facing URLs are still reachable.

### Why??
It's apparent when navigating code documentation online that keeping up with URLs in documentation isn't always done properly.  Running into constant `404 Not Found` errors is frustrating for users that are trying to learn how to use a product or tool.

### Examples
Running the tool against a single file.
```python
▶ python cli.py examples/example1.md                          
examples/example1.md:8  URL Issue: https://www.ansible.com/jeff
```

Running the tool against a directory.  All files in the directory will be executed.
```python
▶ python cli.py examples/           
examples/example2.md:6  URL Issue: https://www.ansible.com/jeff
examples/example1.md:8  URL Issue: https://www.ansible.com/fake
```

Alternatively,

you can replace `python cli.py` with `pyurlcheck` on the command line.

```
▶ pyurlcheck pyurlcheck/examples/
pyurlcheck/examples/example3.txt:4      URL Issue: https://www.ansible.com/jeff
pyurlcheck/examples/example2.md:7       URL Issue: https://www.ansible.com/jeff
pyurlcheck/examples/example3.md:3       URL Issue: https://www.ansible.com/jeff
pyurlcheck/examples/example4.rst:22     URL Issue: http://google.com/france
pyurlcheck/examples/example4.rst:23     URL Issue: http://google.com/japan
pyurlcheck/examples/example1.md:9       URL Issue: https://www.ansible.com/jeff
```

File extensions are currently not checked; therefore all files in a directory that is passed in will be validated.

## Installation

```
pip install pyurlcheck
```
