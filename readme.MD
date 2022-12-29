
# Pulumi
---

##  Using a Self-Managed Backend  (Local Filesystem)

To use a self-managed backend, specify a storage endpoint URL as pulumi login’s.

```<backend-url> argument:```
 * ```s3://<bucket-path>, azblob://<container-path>, gs://<bucket-path>, or file://<fs-path>```


The detailed format of the <backend-url> differs by backend and each has different options such as how to authenticate.
 
Local Filesystem :

To use the filesystem backend to store your checkpoint files locally on your machine, pass the --local flag when logging in

```console
$ pulumi login --local 
```






---

## Inputs and Outputs
Pulumi automatically captures dependencies when you pass an output from one resource as an input to another resource. Capturing these dependencies ensures that the physical infrastructure resources are not created or updated until all their dependencies are available and up-to-date.


Because outputs are asynchronous, their actual raw values are not immediately available. If you need to access an output’s raw value—for example, to compute a derived, new value, or because you want to log it—you have these options:

* Apply: a callback that receives the raw value, and computes a new output
* Lifting: directly read properties off an output value
* Interpolation: concatenate string outputs with other strings directly



---

## Creating new Pulumi Python project :

```console
$ pulumi new python 
```

A new virtual environment is created for us, lets view current dependecies.
```console 
$ pwd
...you_full_project_path.../pulumi-vsphere-demo/vSphere
# Activate virtual environment 
$ source venv/bin/activate
# List dependecies :
$ pip3 freeze 
dill==0.3.6
grpcio==1.50.0
protobuf==4.21.12
pulumi==3.50.2
PyYAML==6.0
semver==2.13.0
six==1.16.0
```

As can be ssing we are using pulumi==3.50.2.


---

## Review the New Project

Let’s review some of the generated project files:

* Pulumi.yaml defines the project.
* Pulumi.dev.yaml contains configuration values for the stack we initialized.
* main.py is the Pulumi program that defines your stack resources.


---

## Pulumi Registry / vSphere /  Installation & Configuration

[Pulumi Registry vSphere Doc](https://www.pulumi.com/registry/packages/vsphere/installation-configuration/)

Installation :
We are interasted in the package : Python: pulumi-vsphere 



Configuring Credentials :

Set the environment variables ```VSPHERE_USER```, ```VSPHERE_PASSWORD``` and ```VSPHERE_SERVER```:
```console
export VSPHERE_USER=XXXXXXXXXXXX
export VSPHERE_PASSWORD=YYYYYYYYYYYY
export VSPHERE_SERVER=ZZZZZZZZZZZZ
```


