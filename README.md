# Sea Battle

Sea Battle (also known as Battleships or Battleship. The game of Battleship is thought to have its origins in the French game L'Attaque played during World War I, although parallels have also been drawn to E. I. Horseman's 1890 game Baslinda, and the game is said to have been played by Russian officers before World War I.  The first commercial version of the game was Salvo, published in 1931 in the United States by the Starex company. Other versions of the game were printed in the 1930s and 1940s, including the Strathmore Company's Combat: The Battleship Game, Milton Bradley's Broadsides: A Game of Naval Strategy and Maurice L. Freedman'sWarfare Naval Combat. Strategy Games Co. produced a version called Wings which pictured planes flying over the Los Angeles Coliseum. All of these early editions of the game consisted of pre-printed pads of paper. [Wiki](https://en.wikipedia.org/wiki/Battleship)

---

![responsive design](https://github.com/Flow-matic/sea-battle/blob/main/images/ahoy%20there%20matey.jpeg?raw=true)


 [Sea Battle app can be found here ](https://sea-battles.herokuapp.com/) 🛳

---
  App Goals:
---


* When playing any of the battleship games you need logic and reason, as well as memory.

* you must remember the shots you’ve taken.

* which square will be next and you must be able to formulate a mental picture of your opponent’s set up and keep that in mind as the game progresses.

* Battleship games introduce school kids to coordinates and grids in a hands-on kind of way

* Battleships is a classic strategy/guessing game of naval combat.

* As a returning regular visitor I would expect all external links to be working and updated.

* All in all, it’s a complete brain workout and a great way to make learning fun.

___

Critical Thinking Skills:
---
 Battleship games introduce school kids to coordinates and grids in a hands-on kind of way; it helps them understand the relationship between rows and columns, as well as the relationship between an actual object or a sequence of events and how they are represented on a graph.

Battleship requires you to formulate a mental picture of your opponent's set up and to keep that picture in mind, making and remembering adjustments as the game unfolds and new information comes in. Not only that, but you need to be aware of what your opponent is doing also.

___

 How To Play: 
--- 

   * Firstly choose if you would like to be player one or player two.

   * The chosen player to go first types in start and hits enter.

   * Then guess your row and hit enter.

   * Guess your column and hit enter.

   * Player two has there turn doing the same process.

   * Each turn will show on the 5x5 board an x to see if you have a direct hit or miss.

   * You missed my battleship! will appear to let you know that you missed the target.

   * You guessed that one already, will show if you have typed the same positions on the board during your turn.

   * Each player will have 4 turns to get a direct hit and sink the other opponents ship.

   * Congratulations! you sunk my battleship! will appear if any player is successful in a direct hit.

   * Oops that's not even in the ocean, will also appear if you type in the same location numbers.

   * This game is a draw. will appear if after each player has used up there turn, an option to play again will be offered with the following, play again (y) or (n) 

   * How to win the game! Guess your opponent's ship locations better. [Game play images](https://github.com/Flow-matic/sea-battle/tree/main/images)

 ___

User Stories:
---
  
As a user, I want to be able to:

  * See clearly what the game is.

  * Have a easy understanding on how the game is played.

  * Be able to play and enjoy a classic game of battleships.

  * I would like the game to be easy to navigate through.

  * Have a working loop environment without users imput errors.


___

Game Flow Chart:
--- 

Lucidcharts was used to give a visual step by step guide on how the game will play out for each user.

   * [What is a flow chart?](https://lucid.co/)

   * A diagram that depicts a process, system or computer algorithm. They are widely used in multiple fields to document, study, plan, improve and communicate often complex processes in clear, easy-to-understand diagrams. Flowcharts, sometimes spelled as flow charts, use rectangles, ovals, diamonds and potentially numerous other shapes to define the type of step, along with connecting arrows to define flow and sequence.

![Flow chart](https://github.com/Flow-matic/sea-battle/blob/main/images/Game%20flow%20chart.jpeg?raw=true)


___ 

Testing Code:
---
[Pep8](http://pep8online.com/) sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

[Code image can be found here!](https://github.com/Flow-matic/sea-battle/blob/main/images/pep8%20code%20ok.png?raw=true)

___

Bugs and Errors:
---
Throughout writing my code, I continuously tested the code in [VS Code's](https://code.visualstudio.com/) terminal as well as [Gitpod's terminal](https://www.gitpod.io/)

   * [E501 line too long (107 > 79 characters)](https://github.com/Flow-matic/sea-battle/blob/main/images/battleships%20error%20codes%202.png?raw=true) was the first error when running the code through pep8.

   * For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters as [image shows](https://github.com/Flow-matic/sea-battle/blob/main/images/code%20too%20long%20fixed.png?raw=true).

   * The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses.

   * [Expected 2 blank lines, found 1 E302](https://github.com/Flow-matic/sea-battle/blob/main/images/battleships%20error%20codes%202.png?raw=true) Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

   * A extra space between lines [41 and 43](https://github.com/Flow-matic/sea-battle/blob/main/images/extra%20space%20between%2041%2043.png?raw=true) was needed to solve this issue.

   * No bugs remained in the app at this time of submission.


___

Deployment:
--- 

Code Institute student template for deploying my third portfolio project was used, the Python command-line project.

The project was deployed to [GitHub](https://github.com/) Pages using the following steps, I used [Gitpod](https://www.gitpod.io/) as a development environment to write and push code to Github. Once your project is finished the folowing steps must be taking before you deploy your app to [Heroku](https://www.heroku.com/)

 

   * Log in to GitHub and locate the GitHub Repository.
     
   * At the top of the Repository, click on the "Settings" Button on the menu.
     
   * Scroll down the Settings page until you locate the "Pages" Section.

   *  Under "Source", click the dropdown called "None" and select "Master Branch" and click on save.

   * The page will automatically refresh.

   * The now published site link shows at the top of the page.


Setting up Heroku environment:

   * Once you have your account ready, login with your credentials.

   * Click New on the top right corner and select “Create new app”.

   * Give your app a name (This will be included in the public URL for your application) and click Create app.

   * This step will take you to the dashboard of your app. Open Deploy tab and scroll to the “Deployment method” section.

   * Select GitHub as the method.

   * It will show a “Connect to GitHub” option where we can provide our GitHub repository. If you are doing it for the first time, Heroku will ask permission to access your GitHub account.

   * Here, you can search for your GitHub repository and click connect:

   * If it’s able to find and connect to the GitHub repository, the Deployment section will show up where you can select if you want Automatic Deployment (as soon as the changes are pushed to GitHub, Heroku will pick them up and deploy) or Manual Deployment.

   * Click Enable Automatic Deploys (because it’s less overhead for demo apps :) ). You can also select the GitHub branch if you need to, deploy from the master branch.

   * Now we need to tell Heroku that our app is a Python and Node.js Framework. When you create the app, you will need to add two buildpacks from the Settings tab.

   * Open the Settings tab and locate Buildpacks and click “Add buildpack”.

   1. python
   2. nodejs

   * The ordering is as follows: python first then nodejs second. Select each buildpack from the options and click Save changes.

   * Now, go back to the Deploy tab, and click Deploy Branch at the bottom.

   * Heroku will take the code and host it. Open the Activity tab and there you can see the progress:

   * Hoooorah!! And that’s it! you just created your own web application that can be accessed over the internet.


___ 

Technologies Used:
--- 

   * [Python](https://www.python.org/) is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

   * [Github](http://github.com/) is a provider of Internet hosting for software development and version control using Git. It offers the distributed version control and source code management functionality of Git.

   * [Heroku](http://www.heroku.com/) is a cloud platform as a service supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.


___

Credits:
---

   * [Stack Overflow](https://stackoverflow.com/) for the code to the game, and also solving other issues along the way to achieving the end result.

   * [YouTube](https://www.youtube.com/) for the endless videos on seeing how code looks and works from professional developers perspective.

   * [Stack Exchange](https://stackexchange.com/) gerneral knowledge questions.

   * [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template) for providing the template needed to work on my project 3.

   * [Python standard library](https://docs.python.org/3/library/) is a collection of script modules accessible to a Python program to simplify the programming process and removing the need to rewrite commonly used commands.

   * [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) is a free online encyclopedia.

   * [Google](http://www.google.com/) Search the world's information, including webpages, images, videos and more.


___

Acknowledgement:
---

  * My mentor for support, advice and feedback. Thanks dickv_mentor. 🙏🏻

  * [Slack](https://slack.com/) community for answers and help along the way to finishing deadlines with projects. 🍻

  * My wife for putting up with my baby Tantrums when my code didn’t work during my project 3. 😂


