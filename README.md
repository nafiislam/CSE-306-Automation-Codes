# pyMisp Setup Guide

This guide will walk you through setting up pyMisp with your MISP instance.
## Prerequisites:
Installed MISP instance

Installed Python

## Collecting API Key

First, you need to obtain the API key from your MISP instance. This key is necessary for authenticating your requests.

for this
go to your misp instance , then in the navbar, go to the last API section, there click OpenAPI
![image](https://github.com/Nahin009/pyMisp/assets/110973431/b46d14a9-3270-41cd-8d3a-ece7aaee6343)

then go to My Profile -> Auth Keys  by clicking here simply
![image](https://github.com/Nahin009/pyMisp/assets/110973431/38e3c179-95b5-433b-91ac-683dc1cd93b9)

then click "+Add authentication key" button
![image](https://github.com/Nahin009/pyMisp/assets/110973431/aeb22410-e224-4ce3-87c3-d067283345b4)

then fill any field according to your need(all are optional, so u can leave all empty) and click the submit button
![image](https://github.com/Nahin009/pyMisp/assets/110973431/38f78572-0bec-4a44-8915-852daf47cdb8)

then copy the key
![image](https://github.com/Nahin009/pyMisp/assets/110973431/c3908376-9c76-419c-99e6-0ff57bb3207a)

congratulations!!! API key successfully generated

## Creating `.env` File

In the main directory of your project, create a file named `.env`. This file will store sensitive information securely. Add the following line to the `.env` file:

```plaintext
MISP_API_KEY="your misp api key"
```

## run the code

Copy-Paste all the commands in the "commands" file in the terminal and click enter 
