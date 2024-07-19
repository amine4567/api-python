# Contributing
## Install depedencies
To contribute to this project, you will need to install both the user and dev requirements
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Update requirement files
To update the user dependencies:
```
pip-compile requirements.in
```

To update the dev requirements:
```
pip-compile requirements-dev.in
```