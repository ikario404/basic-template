# Basic template
Simple web app template with flask, python, bootstrap, fontAwesome to run with python(virtualenv) or docker

## Sources
- flask
- flask_bootstrap
- fontAwesome

## How to
1. git clone
2. run sh (install latest fontawesome)
``` sh install_fontAwesome.sh```

### Run with
* virtualenv
``` virtualenv env3 -p /usr/bin/python3 && source ./env3/bin/activate ```
``` pip install -p requirements.txt ```
* docker/docker-compose
``` docker build -t basic_template . && docker-compose up ```

## To do
- linking conf to sh if needed specific version
- patch footer flask_bootstrap in sources package
