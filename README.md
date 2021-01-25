# Web-Minifier
This application runs in the console: Once you have a folder containing js, css, html, and resources files, 
you can minify it by running: <br> <code>>minify C:\Path\To\Website\Folder </code> <br> <br>
The app will:
- Clone the folder into your downloads
- Remove all the js and css files
- Minify them
- Put them into your html file
- Correctly adjust the html contents to link the scripts

NOTES
---------------
Your main html file must be named index.html

This app **WILL NOT** modify any of the original code.

You can download the exe and put it in your python folder in paths (mine is C:\Users\wdelgiudice\AppData\Roaming\Python\Python39\Scripts)
To find yours hit WinKey, type <code>Environment Variables</code>
click <code>Path</code> and find path with python in it
Next copy the path and paste it into your <code>File Explorer</code>
Drag and drop the exe file into that folder and boom, you can just type minify into your console with a folder path!

Or if you don't trust me you can download the python script and just run it in your ide or build it.

ISSUES
--------------
**Can't get to Environment Variables**
You might not have admin permissions, contact owner of laptop

**Can't find Python path?**
Did you download Python? Did you check off the Add Path checkbox when you downloaded it?

**Error message when you run the executable?**
Did you include a path to the website folder you want to minify? If it still doesn't work email me at delwillgiudice@gmail.com


