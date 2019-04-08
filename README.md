# Website-Blocker

This is something I made for myself back when I was just starting to get on with my computer path in life and at times even today I use this if I have to concenterate on any task without any deviations in my work. I wanted to built something for myself which will help me save my time and stay focused on better things.

This chunk of code is not more than 30 lines and it saved my day many times. 
"WEBSITE BLOCKER" is a peice of code that I wrote to stop some sites to work during the specified time and automatically after the time limit these sites are accesible.
What it does is it just adds few sites that you want to block and prohibit access to for the time limit you want, and after that time these sites are automatically removed from the list and you can access them after the time limit passed. And the best part is, this chunk of code runs in background as a windows process, on startup it automatically triggers.
Thats it!!
But as it sounds so easy, doing it took a special trick, if you go through the code you can see a neat trick that is pulled here.

It is helpful and useful in ways that can multiply your work hours. And also in cases if you want to block certain sites to accessible by anyone.


In this chunk of code I have used "path" variable as a test hosts file which I have copied into project directory.


AND IF YOU WANT TO ADD THIS TO YOUR WINDOWS PROCESS, YOU NEED TO DO SOME STEPS WHICH I'LL BE EXPLAINING DOWN BELOW.
----------------------------------
HOW TO RUN IT ON YOUR OWN COMPUTER
----------------------------------

Step 1 : Fork and Clown this repo. , download the code to your machine and change the paths, you'll get an idea about what path you must replace when you see the code.

Step 2 : Add the sites which you want to block in the list given in the code.

Step 3 : Getting the original hosts file in windows --> An example is shown :  "C:\Windows\System32\drivers\etc\hosts"

Step 4 : Run the code to test if it's working or not.

Step 5 : Now to work with this is in Windows as a background process, you need to do some work.

-------------------------------
Running as a background process
-------------------------------
Firstly, you need to rename the format of your python script to ".pyw", then you need to schedule a tast and for that you need to follow the following Steps -

Step 1 :  Go to START and search for "TASK SCHEDULER" , find and click on "CREATE TASK" you will get a popup and then in GENERAL 
          section type the name you want to give to your task and Check the "RUN WITH HIGHEST PRIVILEGES" box, then move to Trigger
           pannel.
           
Stepc 2 : Click on the "Begin the task" dropdown button and select "At startup". Then move to Actions pannel.

Step 3 : Add a new "Action" and then in "Action" select "Start a new program" and add the file path to your python script. And then 
         click OK and move to "Conditions" pannel.
         
Step 4 : In "Conditions" pannel uncheck the "Stop if the battery switches to battery power" option and you are good to go.

I'm attaching the screenshots to work throught the scheduling task process in windows.
