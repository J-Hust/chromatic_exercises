# Chromatic Exercises for Guitar
### 31,104 Tabs Generated in Python 3

Chromatic exercises use all 12 semitones of the chromatic scale and are typically played in one position on the fretboard.  While they have little musical value, they're great for practicing speed and coordination.  Here's an example of one:
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 3 - - - - - - - 1 - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - 3 - - - 2 - 4 - - - - - 4 - 2 - - - - - - - - - 1 - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - 3 - - - 2 - 4 - - - 1 - - - - - - - 3 - - - - - - - - - 4 - 2 - - - - - - - - - 1 - - - - - - - - -
- - - - - - 3 - - - 2 - 4 - - - 1 - - - - - - - - - - - - - - - - - - - - - - - 3 - - - - - - - - - 4 - 2 - - - - - - - - - 1 -
- - 2 - 4 - - - 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 3 - - - - - - - - - 4 - 2 - - -
1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 3 - - - - - - -
```

We can break these exercises down into two patterns - one which determines the order of the fingers, and another that determines which string is played.  (In the example, the finger pattern is [1,2,4,3] and the string 'offsets' are [0,1,1,2].)

This Python script loops over all permutations of fingers and strings and outputs the results to a text file.  Of the 31,104 exercises, some are redundant, in that they are subsets of other exercises, and others are a bit impractical to play.  Hopefully, though, you will find some new combinations you hadn't thought of before.


#### Usage

* If you're a guitarist who wants to try these, download chromatic_exercises.__txt__.
* If you want to run the script yourself, simply run chromatic_exercises.__py__ in Python 3.
