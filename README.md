# A STAR ALGORITHM - COMP 472 ASSIGNEMENT 1 - ROLE C
### By Arash Manpreet Singh
<br /><br /><br /><br />


## **Instructions**
I chose role C for this assignement

Before starting the program, make sure to activate the virtual environment in the terminal by the command:</br>
`source env/bin/activate`
<br /><br /><br /><br />


Then start the application by typing the path of the Main.py file in the terminal
<br /><br /><br /><br />

When you start the application, you enter the grid size you want: 
![rowInfo](img/rowInfo.png)
<br /><br /><br /><br />





Then the program will ask for what you want to place in the grid:
![gridInfo](img/gridInfo.png)
<br /><br /><br /><br />




Then the program will ask for the coordinates like (0,1) or (1,0):</br>
Since it's role C, we assume that we only start in one of the corners so we can't enter non-corner coordinates
![coordinateInfo](img/coordinateInfo.png)
<br /><br /><br /><br />




Finally, the program will display the result:<br /><br />

IN THE CONSOLE:
![consoleResult](img/consoleResult.png)
<br /><br />
IN THE GUI:
![guiResult](img/guiResult.png)


**LEGEND FOR GUI:**<br />
Starting point = blue<br />
Ending point = orange<br />
AStar optimal path = green
<br /><br /><br /><br />

## **Libraries**

- MatplotLib/Networkx for the GUI<br />
- Numpy<br />

## **Files Description**

- Main.py: contains the code to *make the map* and *make the GUI*
- AStarAlgorithm.py: contains the code for the *Heuristic function*, *AStar function* and *helper functions*