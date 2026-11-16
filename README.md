# Lingua-Poker
Educational Poker Game in Python

The project will consist of developing a Poker game in Python that combines card-game mechanics with language learning. The player will be able to play Poker while answering vocabulary and language questions. The objective is to make learning a language more interactive and entertaining.

The problem I want to address is that learning a new language can become repetitive when it is based on memorizing vocabulary or answering traditional exercises. The program will use Poker as the main game and will include questions in the selected language during the game. 
For example, before performing certain actions or between rounds, the player may have to answer a vocabulary or translation question. Correct answers can give the player rewards such as points or additional advantages

The program could include questions such as:

What does "raise" mean in Poker?

A) Retirarse
B) Aumentar la apuesta
C) Repartir cartas
D) Pasar

If the player answers correctly, they can continue playing or receive a reward.

The project is also interesting from a programming perspective because it requires implementing different concepts.

Libraries Used

Lingua Poker uses the following Python libraries:

- math: Mathematical operations.
- random: Generating random values and shuffling cards.
- collections.Counter: Counting elements.
- unittest.mock: Simulating actions during testing.

All these libraries are part of Python's standard library, so no additional packages or `pip install` commands are required.

Algorithm:
1. Display the main menu.
2. Allow the player to select the language and difficulty level.
3. Initialize the player's score, chips, and game settings.
4. Create a standard deck of 52 cards.
5. Shuffle the deck randomly.
6. Deal the initial cards to the player and the computer.
7. Display the player's cards.
8. Ask the player a language-learning question.
9. Check the player's answer.
10. If the answer is correct, give the player a reward.
11. If the answer is incorrect, apply a small penalty or continue without a reward.
12. Allow the player to perform a Poker action, such as:
    - Check
    - Bet
    - Raise
    - Fold
13. Continue the Poker round according to the rules of the game.
14. Compare the player's hand with the computer's hand.
15. Determine the winner.
16. Update the player's chips, score, and language-learning progress.
17. Ask the player if they want to play another round.
18. If the player chooses Yes, return to step 4. 
19. If the player chooses No, display the final score and learning statistics.
20. Ask if the player wants to save their score.
21. If yes, save name and score
22. End the program.
