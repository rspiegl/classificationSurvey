# Classification Survey

This is the application that I've used for my master thesis: Humans vs CNNs (A comparison with the help of eye tracking data).
The application is written in Python 3.6 with PyQt5. The user interface was created using the QtDesigner. After editing the GUI, one needs to convert it to Python with the convert_ui.sh script. Communication with the Tobii Pro X2-60 is done with the API provided by Tobii.

Each dataset needs to have a labels.txt file to tell the evaluater the truth value of the image.
This repo still contains the evaluation logic and a few methods to produce some plots.
The requirements.txt contains what I've used for developing and executing this application.
The datasets, produced data and more sophisticated evaluation methods can be found at my other repo:
https://github.com/rspiegl/icare-dataset
