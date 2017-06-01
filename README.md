[![Build Status](https://circleci.com/gh/cloudify-examples/simple-python-webserver-blueprint.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/cloudify-examples/simple-python-webserver-blueprint)

# simple-python-webserver-blueprint

This is the blueprint example used for Cloudify's Intro section in our [Docs](http://docs.getcloudify.org).

The blueprint runs a local Python SimpleHTTPServer and allows to tear it down as well and supports Linux,

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
You can `curl http://localhost:8000` or open the link in your browser.

* Get Outputs

```bash
cfy deployments outputs
```

You should see the endpoint of the webserver.

* Get Instances

```bash
cfy node-instances
```

You should see the two instances as defined in the blueprint.

* Uninstall

```bash
cfy uninstall
```
