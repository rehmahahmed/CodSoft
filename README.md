# CodSoft
All CodSoft internship tasks

Python Internship:
1) To-do List
Created by using tkinter module.
As per the specifications given by codsoft, the program will add a task on clicking submit button, allow user to edit a task on clicking edit button and delete a task on clicking the delete button.
I have tried my best to give it the same look and feel as specified by codsoft with colors and widget placing.

![todo1](https://github.com/rehmahahmed/CodSoft/assets/95929046/812f8b02-9fc3-4910-be76-790708f1a183)
![todo2](https://github.com/rehmahahmed/CodSoft/assets/95929046/a33711d2-d5a4-46a6-a2b2-8b2b6e1ce2fe)
![todo3](https://github.com/rehmahahmed/CodSoft/assets/95929046/7252492a-f64c-4127-b7c3-8a38dfe3ba55)
![todo4](https://github.com/rehmahahmed/CodSoft/assets/95929046/d7c54420-0a6d-4bb2-a2a8-745ef575cfdf)

2) Calculator
Created by using tkinter, sqrt, factorial module.
As per the specifications given by codsoft, the program will provide operands and operators and perform evaluations in one entry box.
Its a simple calculator with basic arithmetic operations, square root, factorial all with decimals too.
I have tried my best to give it the same look and feel as specified by codsoft with colors and widget placing.

![cal1](https://github.com/rehmahahmed/CodSoft/assets/95929046/59230fdd-6776-4257-a422-99389fb7cfa0)
![cal2](https://github.com/rehmahahmed/CodSoft/assets/95929046/cbecf3c2-6464-4b92-93d0-ca81231bfe65)

3) Password Generator
Created by using tkinter, random, string, pyperclip module.
As per the specifications given by codsoft, the program will take entries name and length of password.
On clicking generate password a password with random characters of specified length is generated.
On clicking accept the generated password will be copied to clipboard.
On clicking reset all fields will reset to blank.
I have tried my best to give it the same look and feel as specified by codsoft with colors and widget placing.

![pw1](https://github.com/rehmahahmed/CodSoft/assets/95929046/1a1e4de8-ff69-4d26-80fc-c074e41ea476)
![pw2](https://github.com/rehmahahmed/CodSoft/assets/95929046/42d1edb3-8096-4b0d-8a1f-392211a3d1d4)
![pw3](https://github.com/rehmahahmed/CodSoft/assets/95929046/541641e2-4bba-4b1e-9dac-fa031c15b1f2)
![pw4](https://github.com/rehmahahmed/CodSoft/assets/95929046/faff1189-5200-4bfc-9db4-fe018740bc71)

AI Internship:
1) Chatbot
Created using re, random, sys module.
This chatbot works with the help of predefined prompts and responses.
The main working of this code is that when prompted a query/sentence it searches all the predefined prompts and checks which one has highest matching precentage. After checking all prompts and evaluating which one has the maximum matching words it prints the respond defined to it.
This chatbot can reply to basic queries like hi, how are you and what did you eat today?
If encountered with some query that does not match with any predefined prompts the unknown function handles it with some responses.
The chatbot can also exit and end program if told to exit.

![chatbot](https://github.com/rehmahahmed/CodSoft/assets/95929046/c2e18e97-d242-432a-aca8-0ab6a0d94a5d)

2) Tic Tac Toe Game
Created using tkinter and implemeting the minimax algorithm.
The game works via tkinter buttons that are originally set to display " ", but are updated when player clicks on them and computer plays its turn.
The minimax algorithm checks all base conditions first, then calls itself recursively by alternating the is_maximizing parameter's value.
The find_best_move function checks all conditions and returns the best move, this makes the computer unbeatable.
On completion of the game a messagebox is displayed that informs 'you won' or 'computer won' or 'its a tie' then resets the board for another match.

![t1](https://github.com/rehmahahmed/CodSoft/assets/95929046/d36882dd-208c-4a9e-b4f9-13905f755568)
![t2](https://github.com/rehmahahmed/CodSoft/assets/95929046/adeca565-206c-46d6-a735-45e29de62a2a)
![t3](https://github.com/rehmahahmed/CodSoft/assets/95929046/399c50d9-f7d4-41b7-8836-578fa8e50c64)
![t4](https://github.com/rehmahahmed/CodSoft/assets/95929046/453c3a48-00b7-436f-87f7-110d059e7c98)

3) Face Recognition
Created using Haarcascades face and eyes dataset and cv2 module.
The program opens webcam and recognize faces from the captured frames.
The recognized faces that are the Regions Of Interest (ROI) are highlighted in a rectangle.
On pressing enter the program ends.

![f1](https://github.com/rehmahahmed/CodSoft/assets/95929046/ce2e83cb-e335-443e-984e-a83ff6d7b8b9)

ML Internship:
1) Customer Churn Prediction
Import all modules.
Load the dataset.
Assigning X and y. X is dataset without the churn ie 'exited' column. Y is the churn ie 'exited' column
Split the data into training and testing sets.
List all columns in either categorical or numeric list.
Preprocessing the data by applying standard scaling on numeric columns and ignoring unknown data from categorical columns.
Apply Logistic Regression classifier on the preprocessed data via pipeline. Fit and Predict.
Apply Random Forest classifier on the preprocessed data via pipeline. Fit and Predict.
Apply Gradient Boosting classifier on the preprocessed data via pipeline. Fit and Predict.
Print Accuracy of each.
Logistic Regression Accuracy: 0.811
Random Forest Accuracy: 0.8435
Gradient Boosting Accuracy: 0.863

3) Movie Genre Classsification
Import all modules.
Load the dataset.
Dropping irrelevant columns.
Preprocessing data so textual data can be trained, since genre classification is based on plot summary of the movie and other featuers such as movie name, cast, etc.
Apply Naive Bayes classifier on the preprocessed data via inversing the labelencodings done while preprocessing. Fit and Predict.
Print Accuracy.
Accuracy: 0.54

5) Credit Card Fraud Detection
Import all modules.
Load the dataset.
Dropping irrelevant columns.
Apply Random Forest classifier on the preprocessed data. Fit and Predict.
Print Accuracy.
Accuracy: 1.0 
