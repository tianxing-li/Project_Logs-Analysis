# Project: Logs Analysis
This is a project from udacity full stack nano degree.
Project for database with SQL and Python. 
**Just for linux users.**

## Environment
Run under the a vagrant virtual machine from Udacity.
see more from [Full Stack Web Developer Nanodegree program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)

## Installation

### Install Python
When using Ubuntu 16.10 or newer, then you can easily install Python 3 with the following commands:
```
$ sudo apt-get update
$ sudo apt-get install python3 
```
see more from [Installing Python 3 on Linux](https://docs.python-guide.org/starting/install3/linux/)


### Install VirtualBox
> VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
See more from [Full Stack Web Developer Nanodegree program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)

### Install Vagrant
> Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.
See more from [Full Stack Web Developer Nanodegree program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)

### Download the VM configuration
Use Github to fork and clone, or download, the repository https://github.com/udacity/fullstack-nanodegree-vm.

You will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory, and then:
```
$ vagrant up
$ vagrant ssh
```
See more from [Full Stack Web Developer Nanodegree program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)

## How to Run
1. connect the database newsdata.sql, [Dowanload from here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. unzip the package newsdata.zip and the source code in the same directory.
3. locate the file directory
4. using this command in the command line under the virtual machine mentioned above.
```
python Proj_LogsAnalysis.py
```
5. see the result in [result](https://github.com/tianxing-li/Project_Logs-Analysis/blob/master/result)

## About the view in the code
1. view `mostreads`
This view listed **most popular articles with slug name**, and how popular they are.
2. view `errorReport`
This view listed **the statistics from requests** leads to errors group by date.
3. view `connReport`
This view listed **the statistics from all requests** group by date.
4. view `mostreadarticle`
This view listed **most popular articles with title** and views.
5. view `errrate`
This view listed **requests error rate** group by date order from high to low.
