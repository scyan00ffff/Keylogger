Simple Python Keylogger

This is a simple project i have worked on in my spare time and is in no means meant to be the most bulletproof soloution available. I have uploaded the code to GitHub as a means of creating a portfolio and 
it goes without saying that this application should only be run on a device you have explicit permission to do so on. 

The keylogger records all keypresses and allows the user to configure how they wish these to be transmitted. 

The first option is via email in which case the user must change the `report_method` to "email as shown below:
![image](https://github.com/scyan00ffff/Keylogger/assets/99845681/7259096f-f469-4f48-b4fa-fc8941b3b3ef)

In order to configure this correctly you need to add your credentials for the email account into the `creds.txt` file as well as change the smtp server to the relevant one for your email provider as shown:
![image](https://github.com/scyan00ffff/Keylogger/assets/99845681/445221cf-5124-4d8b-b6e1-ac83490d1513)

NOTE: After testing it is apparent that gmail no longer allows remote programs to send mail as part of their protection program so another service must be used

The second way to recieve log files is by saving them as a file in the logs folder of the working directory. This can be done by changing the `report_method` to "file as shown below:
![image](https://github.com/scyan00ffff/Keylogger/assets/99845681/121fd25d-be20-4d2f-b68c-4f9853ca551b)

These files can then be accessed by either getting into the machine and accessing the directory or more easily by accessing `localhost:8000` in a web browser while on the same network as the target device.
This will display all of the files as well as the contents of the logs folder allowing them to be viewed easily.

The code can easily be bundled into an exe file using `pyinstaller` with the relevant flags to make sure the terminal does not launch and the program remains covert. 
