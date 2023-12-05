# Zielone imperium
The goal of the project was to automate the greenimperium.co.uk website. The project was written in Python and automated by Selenium. A jenkins server was also used, and a pipeline was added to allow the script to run itself.
***
0. Requirements
Install lib from _**requirements.txt**_
In 122 line set login, password, server
1. **How to script work**

Automatically login usage credentials in function **login** <br>
Click on every harvestable plant. <br>
Check every customer needs and current supply. <br>
If in stock then script is planing. <br>
Else script randomly choose what to plant <br>
On the end water every seed.
2. **How to setup jenkins <br>**

https://www.jenkins.io/doc/book/installing/windows/ <br>
C:\users\username java –jar C:\tools\jenkins\jenkins.war <br>
Easily change the execution time : 10 min -> H/10 * * * * <br>
settings Jenkins: <br>
_call ./venv/Scripts/activate_ <br>
_pytest main_SlowFarmers.py_
3. **How to connect gitHub with Jenkins <br>**

https://www.blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project
4. **How to start server** 

_java –jar C:\tools\Jenkins\Jenkins.war_
***
# Changes
**v0.1**    03.06.22

0. Setting file with your data
1. Automatically login to game
2. Collect all available seeds
3. Plant new seeds, after that use water on them

**v0.2**    06.06.22
1. New Feature - generate account 

**v0.3** - 07.06.22
1. Deleted not necessary files
2. Speed-up mouse. Now mouse moves 5 times faster

**v0.4** 07.06.22
1. Login all account from JSON file.
2. Fix mouse speed on plant.
3. Every XPath move to _field.py_

**v0.6** 13.06.22
1. Fix imports
2. Speedup collect

**v1.0** 13.06.22
1. Now _main_slow_farmers.py_ is execute from gitHub.

**v1.1** 04.07.22
1. Faster collect.

**v1.2** 12.07.22
1. Added daily login rewards claim.

***
**v2.0** 05.08.2022r
1. Check customers needs.
2. Seed plant if available customers needs.
3. Close special offers tab.

**v2.1** 09.08.2022r
1. Function login changed.
2. Fix faster collect.
3. Fix seed plant which customer want.
4. Faster script

**v3.0** 30.11.2023
1. Added random plant function
2. Added client accept function
3. Added Plant what client needs function

***
Known issue
1. Client accept and client needs can't be in one test

***
Complex test order - div
1. Collect (test_complex_1)
2. Client accept (test_complex_1)
3. Client needs (test_complex_2)
4. Random plant (test_complex_2)
5. Water (test_complex_2)