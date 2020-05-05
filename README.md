# Task-Management-Tools

### Task-Management-Tools is an application for remote control of a device with an ubuntu operating system written in the kivy framework.

### Dependences:

1. **Python >= 3.8.2**
2. **Kivy >= 1.10.1**
3. **Psutil >= 5.7.0**
4. **Cython >= 0.29.1**
5. **Virtualenv >= 16.7.10**

### Install kivy

```bash
sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get update
sudo apt-get install python3-kivy
```

### Installation

```bash
git clone https://github.com/spanickroon/Task-Management-Tools.git
cd Task-Management-Tools
virtualenv --system-site-packages env && . env bin activate && pip3 install -r requirements.txt

```

### Launch

```
Run the taskmanager/app/console_app.py file on the device that will be installed
Run the taskmanager/app/remote_app.py file on the device from which you will control
```

### Errors

```
If there are errors at startup, install the pygame, xclip:
pip3 install pygame 
sudo apt-get install xclip xsel
```