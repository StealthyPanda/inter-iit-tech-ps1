# Inter IIT Tech Meet 11, Selection PS1

Code repository for the problem statement 1, "Develop a raspberry pi based robot that can Identify and tag blocks with alphabets on it in the order Z-Y-X-...C-B-A"

Assumptions:
* Blocks are cubes
* All blocks are in the plane of the robot, and the plane is flat
* All blocks lie in a bounded region
* All the blocks have the same dimensions
* All blocks have their corresponding letter on all faces
* Tagging the blocks is the same as going to the blocks in the correct order and “touching” them (tagging is going to be done by payload carried by the robot)

Solution:

Our solution is a robotic arm that can span the range of the bounded region in which all the blocks lie. The arm has a camera on its end point that uses visual cues to determine the positions of the blocks relative to the base of the arm.(Codes for this detection are all included). The arm then moves the endpoint, that carries the payload that carries out the actual tagging of the blocks, in the order specified.

