# azure-functions-c7n-test

This will be a test environment for running Python 3.6 in Azure Functions.

## Clone C7n

We're going to assume that we have a local copy of the custodian project.

```powershell
git clone https://github.com/cloud-custodian/cloud-custodian/
```

We can also assume we'll have a policy folder for testing.

## Build the image
Navigate to the docker folder and build the image.  This will assume Docker is configured for Linux Containers.

```powershell
docker build -t <myrepo>/cloud-custodian-python36 .
```

## Running the image

Assuming we have Docker installed, we can run the image (in Linux Containers).

```powershell
docker run -it myplooploops/cloud-custodian-python36 -v <localpath-custodian>:/cloud-custodian -v <localpath-policies>:/policies -v <localpath-functions>:/functions
```

Navigate to the functions folder and then make a test function.

```bash
cd /functions

python3.6 -m venv .env
source .env/bin/activate

func init myfuncproj
```

We can also login using az cli:

```bash
az login
az account set -s 'account id'
```

## A note on Cloud Custodian

We also have the c7n environment, which we can refer to [Cloud Custodian](http://cloudcustodian.io) and it's [github repo](https://github.com/cloud-custodian/cloud-custodian).
