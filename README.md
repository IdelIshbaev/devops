# devops

This is project for lab1 on Devops course. It shows current time in Moscow.

## Description

This simple project is created by flask. There is a one page web app that shows time in Moscow.

## Getting Started
clone or download the repo and start it

### Dependencies
flask
os
pytz
datetime
docker

### Installing

use git clone or dowload the repo

### Executing program

```
python3 app.py
```
or 
```
flask run
```
or use Docker
```
docker build . -t devops
docker run devops -p 5000:'PORT NUMBER'
```
see the app in 
```
0.0.0.0:5000
```
``` to see the current time (in addition it will write current time to the file, which will be used in next step)
/
```
``` to see the last written time in .txt file
/visits
```
### Testing
to test run in app_python
```
py.test
```

### Ansible
run local vm (vagrant)
```
cd terraform
vagrant up
```
use ansible
```
cd ..
cd ansible
ansible-playbook -i ./inventory/hosts.yml ./playbooks/playbookDocker.yml
```
docker is installed in vagrant vm
can be checked by 
```
cd vagrant 
vagrant ssh
docker -v
```
## Help

For any help you can refer to
https://docs.docker.com/
and 
https://flask.palletsprojects.com/en/2.0.x/

## Authors

by Idel Ishbaev. BS-18-SE-02

## Version History
- Very first version

## Acknowledgments
- Innopolis University
