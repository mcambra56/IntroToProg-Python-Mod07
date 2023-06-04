# Assignment 7 - Pickling and Standard Error Handling

__Name:__ Megan (Megs) Cambra

__Date:__ May 3rd, 2023

__Class:__ IT FDN 110

__Github:__ [Github Repository](https://github.com/mcambra56/IntroToProg-Python-Mod07)


### Assignment 07 – Pickling and Structured Error Handling

#### Introduction
This simple script demonstrates two new concepts in python: picking and structured error handling. Used to their full potential in more complicated scripts, pickling can help with securing files from prying eyes and decreasing file size, while structured error handling can help find where an error in a code exists and let the user continue to run the rest of the script. These can be very powerful techniques that help turn a hobby coder into a professional.  

#### Pickling
In python, the act of pickling allows an object, such as a list or variable, to be converted into a byte stream to then be stored in a file. Converting to byte stream has several advantages that can especially help when trying to share or store the file: pickling obscures the file’s contents so that it cannot be immediately read without unpickling, and pickling may reduce the file’s size, especially for larger or complex objects. 

While the contents will look obscured to the human eye after pickling, the contents are not encrypted and can be unpickled by anyone who has managed to make it this far in a python class, therefore sensitive content should not be stored this way without further security measures. 
Additionally, users must be careful when unpickling as they could ne at risk of unpacking a malicious object. Since the user cannot read the file, they will not know what it contains until they unpickle and should only unpickle files from trusted sources. 

An example of pickling and unpickling can be found in Figure 1, the first piece of the script. Here, the user will be prompted to input an item and the count of that item, which will be stored and displayed as the ‘inventory’. This is then pickled and stored in a file called “InventoryData.dat” and the file is closed. Finally, the file is opened and unpickled before the first row of content is displayed. 

