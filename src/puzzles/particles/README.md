Particle Animation
==================

A collection of particles is contained in a linear chamber. They all have the same speed, but some are headed toward the right and others are headed toward the left. These particles can pass through each other without disturbing the motion of the particles, so all the particles will leave the chamber relatively quickly.

The initial conditions will be provided as a String called `init` containing at each position an 'L' for a leftward moving particle, an 'R' for a rightward moving particle, or a '.' for an empty location. `init` shows all the positions in the chamber. Initially, no location in the chamber contains two particles passing through each other. A speed will be provided as an int which represents the number of positions each particle moves in one time unit.

## Goal

We would like to create an animation of the process. At each unit of time, we want a string showing occupied locations with an 'X' and unoccupied locations with a '.'. The method will return an array of strings in which each successive element shows the occupied locations at the next time unit. The first element of the return should show the occupied locations at the initial instant (at time = 0) in the 'X', '.' format. The last element in the return should show the empty chamber at the first time that it becomes empty.

## Assumptions

The solution makes the following assumptions about the input values:
- Speed will be between 1 and 10 inclusive.
- `init` will contain between 1 and 50 characters inclusive.
- Each character in init will be '.' or 'L' or 'R'

## Algorithm

We can think of the movement of leftward and rightward particles separately. Picture two arrays of 'X' and '.', where an 'X' represents a particle moving in that direction and a '.' represents the absence of a particle.

We can more easily represent the 'X's and '.'s as 0s and 1s. Furthermore, an array of 0s and 1s is simply a binary representation of a number. We can model the movement of leftward and rightward particles by performing bitwise operations on these numbers. We can also check the 'animation' of the tube at any time by performing a bitwise or on the leftward and rightward numeric representations, since a bitwise or will check whether any type of particle is in each position.