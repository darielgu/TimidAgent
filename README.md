## CS 450 TimidAgent 

- Assignment for cs450 where we are creating a pacman agent to play UCBerkleys Intro to AI Pacman Game
- Goals of TimidAgent
TimidAgent should be based on the LeftTurnAgent with one difference.
Each time the game  invokes nextAction, nextAction will make a call for each ghost to see if the pacman is in danger.

### TimidAgent is in danger if

1. The ghost and the pacman are in the same row or column. 
2. The ghost is within dist units (formal argument to the method) of the pacman.
3. 3. The ghost is not frightened (see the Ghost state for how to check for this).  
