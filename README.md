# Sea Battles

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

   * Player two has their turn doing the same process.

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

  * Have a working loop environment without users input errors.


  ___

Feature Enhancements:
  
  * More functions to add to the battleships game.

  * Keeping players score during the game.

  * Adding the ability for each player to add their own names.

  * Bigger grid.

  * More ships with different size options.


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

[Passed code image can be found here!](https://github.com/Flow-matic/sea-battle/blob/main/images/pep8%20code%20ok.png?raw=true)


___

Testing game functions:
---

  * You must type in 'start' before the game can be played. If you spell start wrong or input a number instead, the game app will tell you to type the word start.

  * Each player will be asked to input a row number first followed by a column number. Numbers between 1 and 5 must be used, if a number above 5 is added the game app will say 'Oops, that's not even in the ocean' and also if a letter is added the following 'Enter a number only' will also appear.

  * When each player has used all there turns, the current match score is 0 : 0 (Player1 : Player2)
  will show in the game app.

  * All inputs have been continuously tested. All game app functions and each piece of code was tested in Gitpod as well as in Pep8.


___

Bugs and Errors:
---
Throughout writing my code, I continuously tested the code in [VS Code's](https://code.visualstudio.com/) terminal as well as [Gitpod's terminal](https://www.gitpod.io/)

   * [E501 line too long (107 > 79 characters)](https://github.com/Flow-matic/sea-battle/blob/main/images/battleships%20error%20codes%202.png?raw=true) was the first error when running the code through pep8.

   * For flowing long blocks of text with fewer structural restrictions (docstring or comments), the line length should be limited to 72 characters as [image shows](https://github.com/Flow-matic/sea-battle/blob/main/images/code%20too%20long%20fixed.png?raw=true).

   * The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses.

   * [Expected 2 blank lines, found 1 E302](https://github.com/Flow-matic/sea-battle/blob/main/images/battleships%20error%20codes%202.png?raw=true) Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

   * A extra space between lines [41 and 43](https://github.com/Flow-matic/sea-battle/blob/main/images/extra%20space%20between%2041%2043.png?raw=true) was needed to solve this issue.

   * No bugs remained in the app at this time of submission.

   * One human error was caused by no other than my self, I wanted to add a mp4 video clip of how the game is played, and the only way to add a video to a readme.md file is to drag and drop the video directly to the file within github. Once saved it did flag up errors within gitpod when trying to push new updates to the readme.md file.🙈

   * Dealing with non-fast-forward errors, sometimes, Git can't make your change to a remote repository without losing commits. When this happens, your push is refused. If another person has pushed to the same branch as you, Git won't be able to push your changes: This was fixed by following the steps taking in the [image](https://github.com/Flow-matic/sea-battle/blob/main/images/non-fast-forward%20errors.png?raw=true)


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


___

Setting up Heroku environment:
---

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


Git Cloning Loacal Deployment:
---
   * You can clone a repository from GitHub.com to your local computer to make it easier to fix merge conflicts, add or remove files, and push larger commits. When you clone a repository, you copy the repository from GitHub.com to your local machine. You can clone your existing repository or clone another person's existing repository to contribute to a project.

   1. On GitHub.com, navigate to the main page of the repository.

   2. Above the list of files, click  Code.

   3. To clone the repository using HTTPS, under "Clone with HTTPS", click copy . To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click copy . To clone a repository using GitHub CLI, click Use GitHub CLI, then click copy.

   4. Open Terminal.

   5. Change the current working directory to the location where you want the cloned directory.

   6. Type git clone, and then paste the URL you copied earlier.

   7. Press Enter to create your local clone.


___ 

Technologies Used:
--- 

   * [Python](https://www.python.org/) is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

   * [Github](http://github.com/) is a provider of Internet hosting for software development and version control using Git. It offers the distributed version control and source code management functionality of Git.

   * [Heroku](http://www.heroku.com/) is a cloud platform as a service supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.


___

Features & Design:
--- 

  * There are some limitations as to how you can style a command-line based app, 
   
   * Colors used for the app grid was as follows. [Red](https://www.w3schools.com/colors/colors_picker.asp), [Blue](https://www.w3schools.com/colors/colors_picker.asp), [Cyan](https://www.w3schools.com/colors/colors_picker.asp), I used [W3schools color picker](https://www.w3schools.com/colors/colors_picker.asp)

  * [Canva](http://www.canva.com/) was used to design and make the background README.md main header image. Canva is an Australian graphic design platform, used to create social media graphics, presentations, posters, documents and other visual content. The app includes templates for users to use free of charge or you can upgrade and pay a yearly fee.

  * [Responsive design](http://ami.responsivedesign.is/) was used to preview the app online.
  
   *  How it works
  
  1. Add your URL to the input field.
  2. Click GO (reloads the preview) or press Enter (reloads the page).
  3. Admire you’re good work.
  4. [Finished image](https://github.com/Flow-matic/sea-battle/blob/main/images/responsive%20design.png?raw=true)
  
  * [Preview app on my Mac](https://en.wikipedia.org/wiki/Preview_(macOS)) was used to cut out images from the final responsive design layout, then I overlaid the images so as to have a background image on the main header and not just a white background. The following step were taking.

   1. Duplicate photos before editing.
   * Find the pictures in Finder. Duplicate them first, so you can always restore them when you made any mistake in the editing process.

   2. Cut and copy the first picture to clipboard.
   * Double click on the first picture to open it with Preview. Click and hold, then drag on the picture to select part of the image, or go to the Edit menu, choose Select All to select the whole picture. Then click Edit > Cut or press Command+X to cut the picture or the selected part of it and copy it to clipboard. This will convert the photo to PNG format if it was an image file in JPG, JPEG or other format that does not support transparency. Converting will replace the existing file. That’s one of the reasons we asked you to create a copy of original pictures above and edit only the copies.

   3. Resize image optionally.
   * Now we need to adjust the size of the image to make room for all photos you want to join together. Click Tools > Adjust Size. Set the desired width and height in the Image Dimensions screen that pops up.

   4. Paste the first picture.
   * Press Commend + V or go Edit menu, choose Paste to paste the first photo or the selected part of it from clipboard to the image background.
   Drag the blue dots in its border to resize the first photo. And drag and drop to position it anywhere above the transparent background.

   5. Copy and paste the second photo.
   * Again open the second photo in Preview on Mac. Go to the Edit menu to choose Select All or drag on the picture   to select part of it, then copy it to clipboard.
   After that paste the second photo to the same image with the first photo.
   Likewise, drag its border to resize it, drag and drop to move it anywhere above the canvas.

   6. Save the photo.
   * Repeat the steps to add more photos to the collage. Finally click File > Export and follow the on-screen tips to  save the photo collage as a new image file on your Mac.

___

Credits:
---

   * [Stack Overflow](https://stackoverflow.com/) for the code to the game, and also solving other issues along the way to achieving the end result.

   * [YouTube](https://www.youtube.com/) for the endless videos on seeing how code looks and works from professional developers perspective.

   * [Stack Exchange](https://stackexchange.com/) general knowledge questions.

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


