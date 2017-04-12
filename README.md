# MobileCloudBridgeServer

This is a rest bridge server done exclusively in conjunction with projects:
<br>
MobileCloudBridgeServer: https://github.com/diegofsousa/MobileCloudServer<br>
AppCloudClient: https://github.com/diegofsousa/AppCloudClient<br>

Step by Step to Install:

First of all, have pip and virtualenv installed.

1. Create a virtualenv for the project by prescribing Python 3:<br>
```virtualenv --python = python3 [environment name]```

2. Enter the virtualenv folder and activate it:<br>
```source bin/activate```

3. Make the clone or download the project into the part of the newly created virtualenv.

4. Install some prerequisites:<br>
```sudo apt-get install python3-dev```

5. Enter the "CloudServerAPI" folder and install pip dependencies:<br>
```pip install requirements.txt -r.```

6. Still in the app folder run ```make run```
