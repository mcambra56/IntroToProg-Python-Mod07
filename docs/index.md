# Assignment 7 - Pickling and Standard Error Handling

__Name:__ Megan (Megs) Cambra

__Date:__ May 3rd, 2023

__Class:__ IT FDN 110

__Github:__ [Github Repository](https://github.com/mcambra56/IntroToProg-Python-Mod07)


## Assignment 07 – Pickling and Structured Error Handling

### Introduction
This simple script demonstrates two new concepts in python: picking and structured error handling. Used to their full potential in more complicated scripts, pickling can help with securing files from prying eyes and decreasing file size, while structured error handling can help find where an error in a code exists and let the user continue to run the rest of the script. These can be very powerful techniques that help turn a hobby coder into a professional.  

### Pickling
In python, the act of pickling allows an object, such as a list or variable, to be converted into a byte stream to then be stored in a file. Converting to byte stream has several advantages that can especially help when trying to share or store the file: pickling obscures the file’s contents so that it cannot be immediately read without unpickling, and pickling may reduce the file’s size, especially for larger or complex objects. 

While the contents will look obscured to the human eye after pickling, the contents are not encrypted and can be unpickled by anyone who has managed to make it this far in a python class, therefore sensitive content should not be stored this way without further security measures. 
Additionally, users must be careful when unpickling as they could ne at risk of unpacking a malicious object. Since the user cannot read the file, they will not know what it contains until they unpickle and should only unpickle files from trusted sources. 

An example of pickling and unpickling can be found in Figure 1, the first piece of the script. Here, the user will be prompted to input an item and the count of that item, which will be stored and displayed as the ‘inventory’. This is then pickled and stored in a file called “InventoryData.dat” and the file is closed. Finally, the file is opened and unpickled before the first row of content is displayed. 

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure1.png "Figure 1")

_**Figure 1.** Pickling and unpickling script using user input data_

As described above, when running the script, the user will first be prompted to input an item and its count before their input is then displayed back to them. Finally, after the file is pickled and unpickled the user will again see the first row of data in the file. This can be seen in Figure 2 (see Appendix B to see the code run in Windows Command Line). If the file doesn’t already exist, python will create the file; however, if it already exists the script will add onto the existing data in the file, in which case the first row of data displayed at the end will not be same row of data the user just entered, as seen in Figure 3. The obscured data file can be seen in Figure 4. 

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure2.png "Figure 2")

_**Figure 2.** Running the pickling code with user input_

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure3.png "Figure 3")

_**Figure 3.** Rerunning the pickling code with new user input_

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure4.png "Figure 4")

_**Figure 4a.** (left) Directory showing file created. Figure 4b. (right) File with obscured content after pickling_

### Structured Error Handling
When python encounters an error when running code, it returns a complicated error message that is sometimes hard to understand or use to trace down where the error occurred. Python will also end the run as soon as it encounters the error, not allowing the script to finish running through the rest of the code that may be working. Structured error handling allows sections of the code to be run without tripping python errors, and instead allows error handling defined by the coder. This is done in a ‘try-except’ block, where the code being tested is trapped in the ‘try’ block, and the ‘except’ block define how the program should handle errors encountered in the ‘try’ block. This technique is very helpful in debugging code, especially when new code is introduced. 

In the script seen in Figure 5, standard error handling is demonstrated for non-existent file names. This could be the case is the file truly doesn’t exist or is not in the same folder as the code and therefore python cannot find it without a path description. This is a common error encountered by python that will usually break the code. However, when inside the ‘try’ block, the run does not stop and rather turns to the ‘except’ block to find out how it should be handled. In this case, the user is asked to input a file name which is then read, and the contents are printed. This obviously cannot happen if the file cannot be found. Here, the code in the ‘except’ block displays an error message explaining to the user that the file cannot be found and then also prints the built-in error message. The standard error handling does not need to be a message and could instead break the code or run a separate piece of code. Many options are available depending on how the coder wants to handle the error encountered. 

Figure 6 shows the results of the user inputting a file that does not exist. The user is informed that file cannot be found and then the built-in python error message is displayed. To test the code to make sure it would run properly for an existing file, Figure 7 shows a simple text file that was created containing one row of data. When the code is rerun after the creation of this test file, and that file name is called up, Figure 8 shows that rather than displaying the common error message the contents of the file are displayed. 

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure5.png "Figure 5")

_**Figure 5.** Structured Error Handling script to handle non-existent file with custom message._

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure6.png "Figure 6")

_**Figure 6.** Running Structured Error Handling script, where user inputs a non-existent file and a custom error message is displayed._ 

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure7.png "Figure 7")

_**Figure 7.** A text file called “Test.txt” is created in the same directory as the script._

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure8.png "Figure 8")

_**Figure 8.** Running Structured Error Handling script, where an existing file is input and therefore no error message is returned._

### Summary
Pickling and structured error handling are two techniques that can enhance python code and its outputs. Pickling allows a python object to be converted to a byte stream and saved to a file, which obscures the data for human reading and can even help reduce the file size. When unpickling the data users should take caution to only handle files from trusted sources, as malicious objects could be embedded into a pickled file. 
Structured error handling allows the code to be run without breaking and triggering the built-in python error messages using ‘try and except’ blocks. A piece of code to be tested is put inside the ‘try’ block, and should it encounter an error python will instead look to the custom error handling inside the ‘except’ block on how to proceed. This could include a custom error message, a break in the code or a completely different path. Structured error handling is very useful when debugging code, especially when new code is introduced by other users. 

### Appendix A. _The entire script_
![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure9.png "Figure 9")

### Appendix B. _Running the code in Windows Command Line_
Note that the directory is first changed to the folder where the script lives. 

For the pickling demo, since the code was run previously in PyCharm, when the file is unpickled the first row in the file that is now displayed is the one previously saved. 

![alt text](https://github.com/mcambra56/IntroToProg-Python-Mod07/blob/main/docs/Assignment07_Figure10.png "Figure 10")
