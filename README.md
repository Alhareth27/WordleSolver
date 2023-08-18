Wordle Helper

Wordle is a popular web-based word game that millions of people use on a daily basis. The essence of the game is to find a 5 letter word that is updated every day. The game allows six attempts for the user, who is expected to win by guess the correct word within those six attempts The mechanism of the game goes as follow:

If the user gets the correct letter in the right place, the letter box turns green.
If the user gets the correct letter in the wrong place, the letter box turns yellow.
If the user gets the wrong letter, the letter box turns gray.

The Program we created

Part 1: User manual: 
Open up both the wordle website and our program.
(Assuming you already know the rules for wordle) You should consider putting  “SNAIL” and  “OTHER” for your first two guesses. If you don’t agree with these two words, you can also put in any word you like.
After getting results from wordle website: report your guess word into the program and press “ENTER”. Then, type in the results marked as different colors: 
type “x” for every gray box
type “y” for every yellow box
type “g” for every green box
Here’s an Example: )
		This would be reported in the program as:  YXXYG

Based on your  input of “x”,”y”, or “g”, the program suggests the next best guess to you. (You’re strongly encouraged to put in this word as your next guess, but again, if you don’t again, guess any word you like)
If you get the correct answer, type 2 to exit the program. If not you are then asked to either enter “1” to continue. If you don’t enter 1 or 2, then you will be asked again until you correctly type in 1 or 2.

If you input “1”, the program asks you for the guess he entered on Wordle. After you input your guess, the program again asks for the sequence in terms of “x”, “y”, “g”. And here the whole process above is repeated, until you get the correct answer!

This set of steps keeps on repeating until the user chooses to exit the program.



Part 2: Program Description
Our program is made up of three main sections: preparatory functions, executional functions, and function calls. 
We have three functions to set up for the preparations. First, we used “Moby Dick” as our corpus to comprehensively represent human language systems, and we analyzed the letter frequencies in Moby Dick. Our second function ranks all the letters from the most frequent to the least frequent. Our last preparatory function takes a txt file of 8000 possible words and converts it into a list of words that we will filter and modify in the next stage.
For the execution functions, we first deal with the answer report (a string made up of “x”, “y”, and “g”). We generate five items for later analysis: correctGuess, finalLetters, finalLetterSeq, wrongLetters, wrongLetterSeq. Second execution function is a helper function that we use to analyze overlapping letters. Then, the next and the most important function of our program is the word list filtering function. We tackled four different scenarios: base case of no repeating letters; green letter overlapping with gray letter; green letter overlapping with yellow letter; yellow letter overlapping with gray letter. We use the conditions we generated from the previous function, filter the word list according to these restrictions, and generate a list of possible answers. Finally, we run this list of words through the letter frequencies we got from the first part, and score each word by calculating the average letter frequency (repeating letters are ignored). This allows us to have a dictionary of possible answers as keys and their varying scores as values. We now simply find the word with the highest score as the next best guess and output it to the author.
Last part is function calls. The first part takes the original 8000 words as the list, and the second function call takes the result from the first part as the new modified list and run through the same functions. This function call will be repeated until the user tells the program to stop.


Part 3: Conclusion: 
One major lesson that was learnt throughout the making of this project was the research skills that both my partner and I gained, as we had to learn how to use modules and functions that we did not entirely cover in class. Therefore, we had to go through the python documentation and assimilate the new information. This was a good learning curb as it made us realize that not everything will be covered in class and that you’ll have to expand your knowledge through the resources that are available to you. 
The main thing that surprised us was the level of complexity and the repetition of the letters that occurred, where some letters were both in the green color and the yellow color, therefore dealing with that bug took quite some time. However, one thing we would do differently is using a different corpus. The reason behind this is that “Moby-Dick” talks about whales quite a bit and this has raised the frequency of the letter “w” unnaturally, more than other letters that are normally used more than the letter “w”. 
In terms of future extensions: We would include a user interface which would make it easier for the users to interact with the program. Furthermore, One issue with the program we created was the fact that if there is a typo in one of the user inputs, the program doesn’t recognize this and this ruins the entire program. Therefore, retrieving any typos instead of starting over is something we need to work on. Lastly, having a comprehensive error message system is one thing we need as well. 



