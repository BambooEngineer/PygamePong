# PygamePong
Pong game with Pygame 


The JPGs in the intro function are all the same but just flipped so its like a loading screen, Needed help with how to detect collision with the ball and 'paddles' and found some mathmatical code from another pygame game. It works better than my first pygame attempt, only thing that couldn't be done was controller support.

Muiltiplayer_Server and Muiltiplayer_Client go together as the updated version of the game with added LAN functionality. Muiltiplayer Server waits for a connection from someone running Muiltiplayer Client then the game starts. With LAN added, random variable definitions got sacrificed because time was running out along with transmitting anything along UDP that wasn't one character, Im not good with buffering incoming byte stream from UDP yet so for now characters seemed to work well without distortion. 
