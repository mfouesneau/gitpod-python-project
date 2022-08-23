# python project template for Gitpod and VSCode

A template project for python development


## Gitpod

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/mfouesneau/gitpod-python-project-template)


Gitpod is a friendly online IDE very similar to VSCode ([Gitpod.io](https://gitpod.io/)
In particular, it provides an entire container-based platform (not saying Docker) and provides VSCode features such as pair-coding while still compiling and running codes. It's also very convenient to write/edit and run some codes rapidly.

This repository holds a very basic workspace to start a python project and work with Gitpod.

**The rest of the README contains some notes on the template and project configuration**

### Table of contents


## Workspace configuration

Gitpod configuration is very similar to a VSCode workspace. The main difference is that Gitpod is a container-based platform, which means you can define your container images.

### Container image `.gitpod.Dockerfile`

More information: https://www.gitpod.io/docs/config-docker/

By default, Gitpod uses a standard image called `gitpod/workspace-full`.
This default image comes pre-installed with Docker, Go, Java, Node.js, C/C++, Python, Ruby, Rust, PHP, and tools such as Homebrew, Tailscale, Nginx, and several more.

If this image does not include the tools you need for your project, you can provide a public Docker image or your Dockerfile.
Using this technique provides us with the flexibility to install the tools & libraries required for your project.

> This template starts with this image as it will make sure that the platform works (sometimes new Debian images introduce breaking changes; see documentation) and installs the HDF5 library.


### Gitpod configuration `.gitpod.yml`

Here is the minimal configuration I use, which tells Gitpod to
* use the provided image information,
* install `conan` and run the first build on start,
* and install some C/C++ convenient extensions for VScode.

```yaml
image:
  file: .gitpod.Dockerfile

tasks:
  - init: "pip install conan"
  - command: "conan install . && cmake ."

vscode:
  extensions:
    - webfreak.debug
    - ms-vscode.cmake-tools
```

## Launchers and Tasks Definitions (`.vscode/tasks.json`, `.vscode/launch.json`)


## Virtual Environment instead

python has now a built-in virtual environment that can be used similarly to `conda`.

```shell
python -m venv --prompt pytemplate --symlink venv
source venv/bin/activate
pip install --upgrade pip
pip install .
# and extras as
pip install ".[ci]"
```
