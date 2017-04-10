## Motivation

### Problem

I believe that many scientists and analysts want to create reusable tools that generate reproducible results. But they don't know how or feel that it'll take too much time to do. So instead, they limit themselves to interactive terminals, or simply write long scripts with no organization and very little reuse of the code they have written. This approach often results in a code base "composed" as a massive collection of scripts, via a process one might call "accidental design by accretion".

The scope of viability of such code is often severely limited in time, space, platform, and use-case. It may not run next week, your coworkers can't get it to run, it won't run on Windows, and that "oh so similar" use case with slightly different inputs causes everything to break in unimaginable ways that are seemingly impossible to track down. These are common symptoms of disorganized code not written with the intent of reuse.

### Solution

This tutorial is intended to demonstrate common ways to organize and reuse Python code, with the goal of transforming "users of" the SciPy stack into "potential contributers to" the SciPy stack, capable of organizing their own code into reusable units for more locally reproducible results while reducing the time spent fighting with disorganized and unmaintainable piles of scripts. 

Specifically, by the end of the tutorial, students should be able to create, install, and distribute python and conda packages. The hope beyond that is that this might enable more people to become contributors to the SciPy ecosystem of more globally reusable tools.