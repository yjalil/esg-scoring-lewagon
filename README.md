# Guidelines for contributors

* Create a branch for the task you picked on Trello
``` git checkout -b <branch-name-matches-task-trello>```
* At the start of every coding session 'git pull' the last changes. At creation the branch is already up to date.
``` git pull```
* While working on your code make sure you're logged to the correct branch.
* At the end of your session, status/add/commit/push as we always did onchallenges
* After multiple coding sessions,you finished the task. Go to the git website to create a pull request. The branch will then be checked and merged to the master.
* Make sure the branch is merged correctly. It should be in the list
```git branch --merged master```
* Delete the branch soit doesn't clutter your git. Don't try to force the delete with -D.
```git branch -d <branch-name>```

# Notebooks
Notebooks will import data. Since we ignore data files, if you need to try someone esle's notebook, you need to copy the data file in the notebook folder. Create a /notebooks/Data subfolder and copy the csv file in it. Don't change another contributor's notebook. 

# Naming variables and classes
We will use the same convention. Classes start with a capital letter, functions and variables don't. This is important, whenthe project grows weneed to be able to find our way by intuition.
* PascalCase for classes
* camelCase for functions
* snake_case for variables
