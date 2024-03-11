# Hive, Cortex and MISP Integration Guide

This guide will walk you through setting up Hive, Cortex and MISP Integration.
## Prerequisites:
Installed docker and docker compose

## Commands to run:
```
i.  first up(install):
    docker compose up -d
ii. remove all containers:
    docker compose down
iii. start a previous compose:
    docker compose start
iv. stop a previous compose:
    docker compose stop
```

## Caution 
You may need to increase vm.max_map_count.To do this: 

We need to add below line in /etc/sysctl.conf file and then run sysctl -p to apply the changes.
```
vm.max_map_count = 1048575
```

## Cortex API key
Firstly, Go to "Add organization".
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Cortex/0.png)

Then input necessary information and save.
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Cortex/1.png)

Then click "Add user" button and input necessary information with orgadmin role
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Cortex/2.png)

Then click Reveal to get the API key
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Cortex/3.png)

Then copy the key
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Cortex/4.png)

## MISP API key
Firstly, Go to "Add oOrganizations". Then input necessary information and Submit.
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Misp/0.png)

Then, go to "Add User" and create an user
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Misp/1.png)

Then click View User icon
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Misp/2.png)

Then click "Add authentication key"
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Misp/3.png)

Then copy the key
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Misp/4.png)

## Setup in Hive
Firstly, Go to "Platform Management"
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Hive/0.png)

Then, go to "Cortex" tab
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Hive/1.png)

Input info like the picture and add the previously saved Cortex API key
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Hive/2.png)

Then, go to "MISP" tab
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Hive/3.png)

Input info like the picture and add the previously saved MISP API key
![image](https://github.com/Nahin009/pyMisp/blob/Hive%26Cortex%26MISP-Integration/images/Hive/4.png)

Congratulations!! You have successfully integrated Hive, Cortex and MISP.
