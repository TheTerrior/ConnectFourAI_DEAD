# ConnectFourAI (In Progress)
A self-evolving Connect Four opponent for Linux! Makes no use of minimax algorithms nor brute forcing, just reinforcement learning. Works as an evolution simulator, complete with sexual reproduction.

## Project Details:<br>
Neural networks are made of 3 layers of nodes. The network accepts 42 inputs, which leads to 84 hidden nodes, to 42 hidden nodes, to 7 output nodes. The 42 inputs represents each tile on a 7x6 board. The 7 outputs each represent a column. The column with the greatest output is where the game will drop a tile. In the case of a tie, the column is chosen at random. As a whole, this means there are 133 nodes, 133 biases, and 7350 weights.<br>

In the first generation, all 1000 neural networks are spawned with randomized weights. From then on, every new neural network is descendent from two parents from the previous generation. Every weight is taken as a gradient between the two equivalent weights from the parents, and then mutated slightly. The mutation constant is also a gene inherited from the parents, and then also mutated according to itself.<br>

During the first generation, each neural network will play against exactly 5 other neural networks, completely chosen at random (can include themselves). Once a neural network has been chosen to be played against, this will count as one of their games as well, but if a neural network plays itself then it'll only count as one game. Exactly 3 games will take place between each pair of neural networks. Each neural network starts with 10 points per game. Each turn they take is -1 points. A loss is -15 points, while a win is +20 points. The scores from the five games are added together for the neural network's final score. The neural networks are reorganized from highest score to lowest score.<br>

The population always remains at a constant 1000. About half of the population is killed off every generation using a gradient (it becomes more likely to die the lower a network's rank is; about a 50% chance of dying near rank 500). The population is then brought back up to 1000 again via sexual reproduction between the survivors from this generation (completely random, no preference). No networks that were just born are allowed to reproduce until the next generation.<br>

In subsequent generations, instead of playing against a random set of 5 neural networks, all neural networks will play against the top 5 (neural networks in the top 5 will play against themselves). The neural networks will be reordered just as before, and this will continue on until the AI is adequately trained.


## Dependencies (old):<br>
python, sqlalchemy, numpy, numba, pysimpleguiqt

## Dependencies (new):<br>
Python (PySimpleGUIQt, maturin), Rust (PyO3)

## Future Plans:<br>
Scrap much of the existing code (except for the main and GUI code)<br>
Rewrite the scrapped code in Rust with PyO3<br>
Store data in JSON files (maybe one file per generation, which will grow in amount very very quickly)
