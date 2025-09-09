
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A pacman agent that follows the LeftTurnAgent with these added features to check for danger:
    1. The ghost and the pacman are in the same row or column. 
    2. The ghost is within dist units (formal argument to the method) of the pacman. 
    3. The ghost is not frightened (see the Ghost state for how to check for this).  

    When the pacman is in danger, inDanger returns the compass direction from the pacman to the  ghost
    Method inDanger returns the Directions.Stop when the pacman is not in danger.


    Method getAction should check for the pacman being in danger from each of the ghosts using  inDanger. 
    The states can be obtained from the GameState object that will be bound to getAction’s  formal argument state. 
    See methods getPacmanState() and getGhostStates() in  pacman.GameState which will be helpful for finding the agent states. 
    Note that getGhostStates()  returns a list of states. As inDanger checks for one ghost at a time, you will need to process the  ghost states sequentially in the same order as they are returned by getGhostStates(). 
    The first  time the pacman is in danger, a decision is made. 
    Based on the direction from which the pacman  is in danger, we select a new direction. 
    We check for legal directions in the following order:  reversing the current direction, turning to the left, then turning to the right. 
    If none of these are  legal, we continue in the direction of the danger, or stop if no move is legal (only possible in  contrived boards). 
    In the example above, the pacman is in danger from the East. Reversing the  danger direction is not legal, nor is heading North (left turn from East), but the right turn to the  danger direction (South) is possible and TimidAgent should return Directions.South for this case. 
    When the pacman is not in danger, it should function n the same manner as the LeftTurnAgent.  
    That is, it turns left whenever possible. 
    If a left turn is not possible it continues straight until it  can’t go any further in the current direction. 
    When the pacman cannot go left or forward, then it  tries to turn right, and if necessary turns around. 
    If no action is possible, getAction returns Directions.Stop.  


    """

    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """

        # Your code
        raise NotImplemented
    
    def getAction(self, state):
        """
        state - GameState
        
        Fill in appropriate documentation
        """
        legal = state.getLegalPacmanActions()
        ghostPositions = state.getGhostPositions()
        pacmanPosition = state.getPacmanPosition()
        
        

        raise NotImplemented
