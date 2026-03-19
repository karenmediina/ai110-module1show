# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
The game took a while to load but it had my attempts and score 0 to start. I began hitting random numbers and I entered the guess 9 twice but got different messages to go lower and then go higher, for the same guess. I hit negative numbers and it also told me to go lower. The history grows infinitely large and does not reset between games. I have a feeling when you are below the secret number, it tells you to go lower. But when you are above the secret number, it tells you to higher. My group found that the secret number can currently be higher than the range, however it should be abiding by the appropriate closed set. The secret number was 42 when I was on easy mode.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I used Gemini and Copilot to work on this project. I used Gemini to get set up with VSCode and even find copilot because I had never used it.
I used inline Copilot to understand specific lines and the chat feature to load in some documents and have a general overview. An AI suggestion that was correct was fixing and reseting the attempt and score variables. An example of an incorrect suggestion was actually fixing the labels. I t didn't detect the ranges were wrong and even when I pointed it out, the fix was not correct. I then explained it again and it saw the logic.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I read over the code before it was fixed trying to identify the bugs myself. I had some hypotheses so I tested them with AI (made some tests). When they didn't pass, I confirmed my hypotheses and the behavior of the program. I told Copilot to identify the bug, describe it to me (to see if we aligned), fix it and comment your fix, explain to me how you fixed it and reran my tests. I tested the go higher and go lower features and found that they were flipped and when I had to go higher it would tell me to go lower and vice versa. Yes, AI helped me design my tests by using the description I gave it and the parameters, plus highlighting what function specifically I wanted to test.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
Streamlit is a little weird in the sense that it will rerun everything after each play. If you were to think about being in a library, then imagine you're on a desk and every time you flip over a page, someone goes and cleans up everything for you. The session state would be like a little note on the side that would store what page number you were at, etc so at each step your progress would be saved. 


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

That's a good question. One strategy I want to reuse is leaning more on AI to gather an overarching idea of what the codebase is doing. I'm pretty good at understanding inline issues or at least debugging them but I have a hard time trusting and diving into a codebase I've never seen before. It takes me a while to catch up but I'll try new methods like uploading the files like that. Header files are good for me. One thing I would do differently next time is finding a better way of keeping track of the changes I make and multiple versions. I've heard Git is very good for that type of bookkeeping but I'm just getting familiarized with it. This project changed the way I approach coding with AI and AI generated code by 