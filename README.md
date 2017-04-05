# Introduction to Reusable Python

### For Scientists and Analysts

A tutorial on how to organize python code into reusable units such as scripts, containers, functions, modules, and packages; and how to reuse those units, locally and globally, by installing and distributing them using pip and conda.

## Motivation

### Problem

I believe that many scientists and analysts want to create reusable tools that generate reproducible results. But they don't know how or feel that it'll take too much time to do. So instead, they limit themselves to interactive terminals, or simply write long scripts with no organization and very little reuse of the code they have written. This approach often results in a code base "composed" as a massive collection of scripts, via a process one might call "accidental design by accretion".

The scope of viability of such code is often severely limited in time, space, platform, and use-case. It may not run next week, your coworkers can't get it to run, it won't run on Windows, and that "oh so similar" use case with slightly different inputs causes everything to break in unimaginable ways that are seemingly impossible to track down. These are common symptoms of disorganized code not written with the intent of reuse.

### Solution

This tutorial is intended to demonstrate common ways to organize and reuse python code with the goal of transforming "users of" the SciPy stack into "potential contributers to" the SciPy stack, capable of organizing their own code into reusable units for more locally reproducible results while reducing the time spent fighting with disorganized and unmaintainable piles of scripts. The hope beyond that is that this might enable more people to become contributors to the SciPy ecosystem of more globally reusable tools.

## Preparation

* [Tutorial Description](./tutorial_description.md)
* [Tutorial Plan](./tutorial_plan.md)
* [Tutorial Set-Up](./tutorial_setup.md)
* [Tutorial Resources](./tutorial_resources.md)

## Lessons

### Interactions

* [Introduction to Shells and Portable Interactions](./content/shells.md)
* [Python Scripts and Reusable Interfaces](./content/python_scripts.md)

### Modules

* [Python Modules and Reusable Code Blocks](./content/python_modules.md)
* [Python Packages to Combine and Install](./content/python_packages.md)

### Environments

* [Introduction to Conda](./content/conda_intro.md)
* [Using Conda to Manage Environments](./content/conda_envs.md)

### Distributions

* [Building Conda Packages](./content/conda_packages.md)
* [Distributing Packages with Conda Channels](./content/conda_channels.md)

