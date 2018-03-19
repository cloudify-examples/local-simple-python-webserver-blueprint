[![Build Status](https://circleci.com/gh/cloudify-examples/simple-python-webserver-blueprint.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/cloudify-examples/simple-python-webserver-blueprint)

# simple-python-webserver-blueprint

The blueprint installs a webserver on your local machine. It is supported on Linux and most *nix machines.


## Prerequisites

- [Cloudify CLI](http://docs.getcloudify.org/4.0.0/installation/from-packages/) installed on your computer.
- Your workstation's firewall should allow HTTP connections on port 8000.


## Usage

* Clone the repository

```bash
git clone https://github.com/cloudify-examples/local-simple-python-webserver-blueprint.git
cd local-simple-python-webserver-blueprint
```

* Install

```bash
cfy install blueprint.yaml
```

This will run a `Hello World` server on your local machine in port 8000.

```bash
Open your browser to http://localhost:8000
```

You will see the following in your browser:



* Uninstall

```bash
cfy uninstall -b local-simple-python-webserver-blueprint
```
