# Wordle-Solver
I made this in math class because I was bored and I nearly failed the wordle. It made me realize that I suck at wordle, but I'm good at code, so I'm automatically good at wordle.

## How to use:
**Step 1)** download the code  
  
**Step 2)** navigate to the folder's location and run the code with python `python wordle-solver.py`  
  
**Step 3)** open the wordle and either enter the suggested word or skip in the terminal until you find a word that pleases your fancy  
  
**Step 4)** enter the results of the wordle, where ` ` represents a grey square, `y` represents a yellow square, and `g` represents a green square  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**e.g)** 🟩🟨⬜️🟩🟨 would be `gy gy`  
  
**Step 5)** repeat steps 3 -> 4 until you have solved the wordle  

## how it works:
Being a sophmore and in precalc, I took the most obvious aproach, without tbinging in advanced statistics or complicated math in order to choose a guess from the thousands of options. The first step was to loop through the entire word list and count how many time each letter appeared, using this data, I could score each letter from 0(the best score) to 25(the worst score). looping through all of the words again, I then scored each letter based on each letter, so that words with tons of popular letter are suggested above other words. The best word is suggested, and the results filter the massive word list into a smaller one, repeating the letter counting process.
