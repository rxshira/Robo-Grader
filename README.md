This is my final project for one of my classes, 15-112, that I took in the Fall of 2024. Enjoy!

======

My project title is: RobotAutoGrader. The idea of it is separated into two parts.

The first part of my project is from the backend. Simply put, given any video of a robot moving from one place to another, where the other place is its “end goal”, the computer program will track the movement of the robot. The program will be able to find where the robot (which is red) and the block it moves (which is blue) is in the image as well as where “end goal” (which is green) is based on their colors. If the blue covers the green (so that the green is no longer in the image, or is at least overlapping with the moved block’s position), the path of the robot was successful. The program will also draw out the path that the block the robot moves takes, in order to use it for the next step, which is, the user interface portion. 

As for the user interface of this program, it can be broken into several parts. First, the user will draw the path that they plan for the tracked block to take, which is going to be the “reference solution”. This will be the expected path of the block, which will later be compared to the path the block actually took. Then, the user will upload the video of the robot moving the blue block, or choose a file from their device. Then, the program will work in the background to track the robot's movement and create the path that it took. Once the program has finished drawing out the path of the block, it will compare the path the block took to the sample solution. Based on how close the actual path of the block was to the sample solution, the program will give the user a percentage accuracy score, as well as overlaying the sample solution with the actual path the block took, to show the user where they went wrong. 

======

Run instructions:


Make sure that you have all the files for the RoboGrader before running, including all the preloaded videos to the program.

Also, make sure that in the same space you run the src code, you also download another file of videos. Here is the link to acesss the required video files:
https://drive.google.com/drive/folders/1-U6JkVNn4xdKyY5nEVX28MaSZBmGpL1o?usp=sharing

Put these videos under the "videos" folder.

Please be patient with this program! It might run a little slower than expected becuase of all the image analysis. There will be a clear change once a video is uploaded/selected, so just wait for it. 

Please install the following additonal modules: Moviepy, Pillow, EasyGui.



As you run it, to begin a new project, click 'New Project' OR ‘Example Project’

======

NEW PROJECT:

Here, you can first type in the title for your project by clicking on the 'project title.' Make sure that it is containing only Letter and Numbers up to a max of 14 chars.

Next, upload a video of your robot moving. It must have a moving blue point and a stationary green point. 

Then, wait to select a temporary place on your computer to store the frames of the video. 

Wait until the green check mark in the circle shows up, and then you may proceed to the next step. 

Click on the 'Draw Path' button to draw the correct path for the robot.

Then, click on the green and red squares. Move them around to your desire in the canvas, and once you do that, click on the fix buttons under both of them.

After that, draw your path from the red 'start' box to the green 'end' box. Once you are done, click on the 'back' button. Click on the 'clear' button to erase all your drawings.

Then, click on the 'compare paths' button, and see your percent success! You can also click on the 'see image' button to see how your drawing compares with the actual path the robot took. 

======

EXAMPLE PROJECT:

Here, you can select from 5 video examples pre-loaded into the app. 

Click on ‘Select Video’, and then select one of the 5 options. 

Click on the 'Draw Path' button to draw the correct path for the robot.

Then, click on the green and red squares. Move them around to your desire in the canvas, and once you do that, click on the fix buttons under both of them.

After that, draw your path from the red 'start' box to the green 'end' box. Once you are done, click on the 'back' button. Click on the 'clear' button to erase all your drawings.

Then, click on the 'compare paths' button, and see your percent success! You can also click on the 'see image' button to see how your drawing compares with the actual path the robot took. 

======

Shortcuts!
When on the Drawing menu, you can click the following keys:
- 'a' == get list of all the points in the drawing
- 'g' == run the comparison between the video and the drawing early, giving path comparison with image.

======

*** A note on art: ***

All art in this project is my own. I drew it myself on IbisPaint on my iPad, and then uploaded it to Pinterest to get the image URL. 

*** A note on AI use: ***

I have used a mix of Microsoft Co-Pilot, ChatGPT, and Claude in this project. 
Of course, most of this code IS my own, and so is the idea and execution. 

However, I often asked AI to help me clean up my code. I did my best to make sure I credited it
where I used it, but I always have the lingering fear I may have missed some things. (I hope I didn't)

Sometimes I'd have it re-write functions to run cleaner or change the way I have my drawing functions appear, just to note some examples of my uses.

I mentioned when, where, and how I used the AI and what it helped me with. When used right, it is a very helpful tool, especially to 
get tedious UI work done fast!

