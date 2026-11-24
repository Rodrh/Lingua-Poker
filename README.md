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
- datetime: Recording the date and time when game results are saved

All these libraries are part of Python's standard library, so no additional packages or `pip install` commands are required.

Algorithm:
1. Executed the automated tests.
2. Display the Lingua Poker title.
3. Allow the player to choose language.
4. Initialize the player's statistics
5. Create the player and two computer opponents.
6. Create a standard deck.
7. Shuffle deck
8. Deal two private cards to each participant.
9. Display the player's private cards.
10. Start the Pre-Flop betting round.
11. Ask the player a random vocabulary question.
12. Check the answer
13. Award 10 points for a correct answer or subtract 5 if incorrect.
14. Allow the player to perform the action.
15. Allow computer opponents to make decisions.
16. Continue through Flop, Turn, and River betting rounds.
17. Deal the community cards.
18. Evaluate the active player's hands.
19. Determine the winner/s.
20. Distribute the pot among the winners/s.
21. Display the player's educational statistics.
22. Ask whether the player wants to save the results.
23. If the player choose Yes, request their name and save results in the extra file.
24. End program.

Python API references

- [Python `math` module](https://docs.python.org/3/library/math.html)
- [Python `random` module](https://docs.python.org/3/library/random.html)
- [Python `collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter)
- [Python `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html)
- [Python `datetime`](https://docs.python.org/3/library/datetime.html)
- [Python reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
