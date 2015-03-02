First try at a small RPG game created using pygame. Repo may end up getting kinda messy by accident.

Here I will keep a day by day history of changes made to the project,

2/13/15 Project creation.. First ideas developed and beginning work on pauseMenu.py, along with several other classes

2/14/15 New Project approach.. Looking at new way of creating start menu by having each option set up separately. Build each panel of menu into separate Rect objects

2/27/15 Created test image in order to implement movement. Both TESTIMAGE.xcf
and TESTIMAGE.png were created in GIMP. Movement is now implemented within the
main game loop. Movement needs to be implemented within Player class.

3/1/15 Scrapped the idea that was going to be used for creating start menu.
New idea for start menu involves creating a class named StartMenu.py and
implementing a nested while loop within the main game loop.

3/2/15 Projected plans: 
       First is to make the Start Menu class. 
       Next will be implementing the class without error in the main game loop.
       Next will be learning to implement TMX maps in order to create a test
world.
       Next will be the process of polishing and implementing the Player
class.
       This is currently the extents of planning. The rest will be thought
about only after everything in this list is up and running.
