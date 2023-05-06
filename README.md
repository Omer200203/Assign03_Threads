Conway Game Of Life Using Posix Threads
Operating System Assignment # 3
21k-3066

#REPORT

* Create a two-dimensional array to represent the cell grid, and use conditional statements to apply the game's rules:
1) Give the grid of cells a random starting value.
2) Use conditional statements to put the Game of Life's rules into action. Based on the number of living neighbours a cell has, determine the condition of each cell in the grid in the following generation. Adjust the grid as necessary.
3) For the chosen number of generations, repeat the previous step.
![image](https://user-images.githubusercontent.com/125944925/236648132-18ebae5e-bbcf-489d-97b8-0e73f3caac31.png)
![image](https://user-images.githubusercontent.com/125944925/236648165-5da572f5-ecc1-4a26-b8d8-b52e22343059.png)

* To execute the Game of Life algorithm concurrently, create multiple POSIX threads:
1) Allocate a single thread to each area of the grid that is divided into equal-sized pieces.
2) To avoid data races, each thread will calculate the subsequent generation for the given area of the grid and update the shared grid using a mutex.
3) To make sure that each thread has finished updating the grid before the next generation is calculated, synchronise the threads using condition variables.

* To synchronise access to shared data structures like the cell grid, use mutexes and condition variables:
1) To avoid data races when updating the shared grid, use a mutex.
2) To let the main thread know when a thread has done updating its section of the grid, use a condition variable.
![image](https://user-images.githubusercontent.com/125944925/236648217-7ffe6f41-4372-4acd-b3d3-f78c299b4f71.png)

* Shell scripting can be used to gauge the speedup brought about by running the finished application with varying thread counts:
1) To determine how long it takes for your programme to run with various amount of threads, use the time command.
2) Plot a graph to show the increase in speed brought about by running the programme with different numbers of threads.
![image](https://user-images.githubusercontent.com/125944925/236648265-be017250-ed3a-4249-bc19-71033b2629f1.png)

* Report your implementation in full, mentioning any design choices you made and the outcomes of your speedup measurements:
1) Describe your implementation strategy, including the choices you made for the use of data structures, synchronisation techniques, and thread allocation.
2) Analyse the performance improvements made possible by running the programme with many threads and present the results of your speedup measurements in a table or graph.
![image](https://user-images.githubusercontent.com/125944925/236648587-57fbacb2-3f3d-4dd8-8389-d179d1ebd9b9.png)
