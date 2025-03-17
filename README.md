---Usage of the Programs---

The idea for these programs comes from implementing a Treasure Hunt
game in a school using micro:bit boards.

In this context, one student, with the board running the emisora.py
program, guides another student who has the board with the receptora.py
program towards one or several targets.

On the displays of both boards, two types of arrows are shown. Static
arrows, which mean 'do not walk', and moving arrows, which mean 'walk'.
You switch from one type of arrow to the other by pressing both the A
and B buttons simultaneously. Additionally, for both types of arrows
(commands to walk or not walk), turning instructions can be given, to
the left or right, by pressing the corresponding buttons (A or B).

If the game is played by more than one pair of players at a time, it is
necessary to establish a channel for each pair. This is done through the
channel parameter of the radio.config() method. Thus, one pair of players
can use channel=0, another pair channel=1, and so on. It is important to
make this modification in the programs before starting the game.

Finally, I believe this version of the programs is somewhat useful for
demonstrating the topic of object-oriented programming and providing an
immediate practical application. The class declarations are repeated in
both files for convenience, although this duplication is redundant.

I hope you find it useful and fun.

Alejandro Chimera