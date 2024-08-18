# Wordle

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With
![python_badge]
![openai_badge]

Wordle is a Python-based implementation of the popular word-guessing game. In this version, the user attempts to guess a randomly generated word, with the length and difficulty determined by the selected mode. The game utilizes the OpenAI GPT-3.5 API to dynamically generate random words, ensuring a fresh challenge with each playthrough.

Features

	•	Difficulty Modes: Choose between Easy, Hard, or Challenge mode, which affects the word length and the number of attempts available.
	•	Dynamic Word Generation: Leverages the OpenAI GPT-3.5 API to generate a random word each time, ensuring no two games are the same.
	•	Stylized Output: Uses the colorama library to provide colored and styled text output in the terminal, enhancing the user experience.
	•	Hints: Players can request hints if they get stuck, making the game accessible for all skill levels.
	•	Feedback System: The game provides immediate feedback on each guess by highlighting letters in different colors:
	•	Green for correct letters in the right position.
	•	Yellow for correct letters in the wrong position.
	•	Red for incorrect letters.

How to Play

	1.	Choose a Difficulty Mode: Select between Easy (4-letter words), Hard (5-letter words), or Challenge (6-letter words).
	2.	Guess the Word: Try to guess the word within the allowed number of attempts, with feedback provided after each guess.
	3.	Use Hints if Needed: You can request a hint by typing y, but hints are limited based on the difficulty level.
	4.	Win or Lose: If you guess the word within the allowed attempts, you win! If not, the correct word is revealed.

This project combines Python programming, API integration, and terminal-based game design, providing a fun and educational experience for developers and players alike. 


<!-- GETTING STARTED -->
## Getting Started


### Installation


1. Get a OpenAI API Key at [(https://platform.openai.com/api-keys)](https://platform.openai.com/api-keys)

2. Clone the Repo or simply Download the Python File
   ```sh
   git clone https://github.com/bryanrg22/Wordle.git
   ```
3. Install Colorama through the Terminal
   ```sh
   pip install colorama
   ```
4. Install Openai through the Terminal
   ```sh
   pip install openai
   ```
4. Enter your API in `wordle.py` on Line 11
   ```js
   openai.api_key = 'ENTER YOUR API'
   ```

<!-- CONTACT -->
## Contact Me



[![linkedin_badge]](https://linkedin.com/in/bryanrg22)  [![gmail_badge]](mailto:bryanram2024@gmail.com) [![github_badge]](http://www.github.com/bryanrg22)

Bryan Ramirez-Gonzalez - [Add me on Linkedin!](https://linkedin.com/in/bryanrg22) - [bryanram2024@gmail.com](mailto:bryanram2024@gmail.com)

Project Link: [https://github.com/bryanrg22/Wordle.git](https://github.com/bryanrg22/Wordle.git)



<p align="right">(<a href="#readme-top">back to top</a>)</p>

[python_badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[openai_badge]: https://a11ybadges.com/badge?logo=openai
[linkedin_badge]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[gmail_badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[github_badge]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
