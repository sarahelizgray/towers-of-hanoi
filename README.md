
Predictive Tower's of Hanoi

python verion 2.7


This sample code is a console game of the "Towers of Hanoi" problem. For more on the principle behind the problem, see the Wikipedia article: http://en.wikipedia.org/wiki/Tower_of_Hanoi.

This program is a particularly interesting implementation of the Hanoi problem because it starts the puzzle at an intermediate point with discs scattered throughout the three posts, and it is able to tell you how many moves to the completed puzzle. More than half of the code in this sample is just to figure out the number of remaining steps, using multiple addressing systems like Sierpinski addressing to represent each possible configuration. Yep, I could have done this recursively, but the addressing systems are faster and less system intensive because it uses fewer stack frames. I have coordinating unittests, but I am reluctant to pass them on because they were provided by my prof and are not my original code.

Simple directions for playing the game:

1. Open the interactive python shell on your platform of choice, making sure that you know where the hanoi.py is located
2. Type  "import hanoi"
3. To start game play, type "hanoi.play(4)" to play a puzzle with four discs. Adjust the number of discs as you see fit and see the number of moves count climb accordingly :)