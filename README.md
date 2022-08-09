HOW TO SETUP JENKINS
1. https://www.jenkins.io/doc/book/installing/windows/
2. C:\users\username java –jar C:\tools\jenkins\jenkins.war 
3. Easily change the execution time : 10 min -> H/10 * * * *
4. settings Jenkins: 
call ./venv/Scripts/activate
pytest main_SlowFarmers.py
# START java –jar C:\tools\Jenkins\Jenkins.war
Settings jenkins: https://www.blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project
***
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