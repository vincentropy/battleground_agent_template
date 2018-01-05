# Agent Templates
Develop your own agents for the battleground platform.



## System Setup
You can develop agents using any of your own favorite tools,
just fork and download this repository and adapt the my_agent.py and/or my_persistent_agent.py examples.

Debugging your agents locally requires you to run the battleground platform locally.
There are 2 ways to do this:
1. Using a virtual machine and vagrant
2. Running/Installing natively

### 1. Using Vagrant (recommended)
Even if you are not already familiar with Vagrant, this is probably the easiest way to go.
Make sure you follow all the [installation instructions for vagrant.](https://www.vagrantup.com/docs/installation/)
Then run
```
vagrant up
```
in the folder that contains the Vagantfile supplied in this repo, using the console. 
This automatically installs all necessary components (battleground package, docker, etc.) for the environment to run.  

You can then connect to your virtual machine using
```
vagrant ssh
```

### 2. Native Setup
This method is a bit more involved.
- [install Docker](https://www.docker.com/community-edition)
- [install python 3 on your system](https://www.python.org/)
- your probably want to [create a virtual environment](https://docs.python.org/3/tutorial/venv.html)

Then start a local mongoDB container:
```
docker run docker run -d mongo
```

**activate your virtual enviromnent** and then install the requirements:
```
pip install --upgrade -r requirements.txt
```



## Configuring and Running a Game

Ok, now we're ready to play!
Edit the example_config.json file to determine what game configuration you want to play.
The basic game provided as an example is just a number guessing game. 
It instantiates four players: one from the battleground core component, two from my_agent 
in the basic_agent folder, and one from my_persistent_agent in the same folder. 
In contrast to my_agent, the persistent agent has access to a memory, which is stored 
in a local mongoDB. Accessing it, it continuously tries to improve the guess for the next move.

We can  run the game server now using
```
battleground_start --config ./example_config.json
```

The output should look something like
```
starting battleground ...
basic_game
[40, 17, 35, 100.07654482421009]
[107, 0, 2, 33.970877838933404]
[55, 5, 0, 101.1932715214214]
```

These numbers are the final scores of each of the four players in each of the three games that were played.

### Playing an Arena Game

As a second example, there is an arena_config.json file which plays four arena games with 
a similar agent composition as above. The core agents move randomly by default. 
This arena game loads the boosts mod, which introduces the option for the agent to boost 
certain stats of the gladiator it is playing. If you want to include more or other mods, check out the 
[battleground.games.arena.mods](https://github.com/arenarium/battleground/tree/master/battleground/games/arena/mods) 
folder to see what is available, and append your choice to the list of mod_paths in the arena_config file.

To start the game server, we run
```
battleground_start --config ./arena_config.json
```

which should give an output that looks like
```
starting battleground ...
arena_game
{0: 0, 1: 1, 2: 0}
{0: 1, 1: 0, 2: 0}
{0: 0, 1: 0, 2: 2}
{0: 2, 1: 0, 2: 0}
```
The keys of this dictionary are the IDs of the agents playing the game, and the values
are the scores that were achieved. The score is 1 for each other gladiator killed, but 
set to 0 if your gladiator dies.



## Further Comments

There are many places where the configs can be modified and individualized 
to possibly also play your own games!
```
"game":{
  "name": your favorite game name,
  "type": your favorite game type description,
  "local_path": local path to game engine,
  "class_name": name of game engine class,
  "mods":{"builder_path": local path to builder file for configuring mods,
          "mod_paths":[paths to mods that shall be configured
                       ]
          },
  "settings":{ possible settings for game engine }
},
```
```
"players":[
  {
    "owner": your name/alias,
    "name": name of your agent (unique amongst every owner),
    "local_path": local path to agent file,
    "class_name": name of agent class,
    "remote_path": if no local path, then remote path to agent file
  }
]
```
Note that all entries are strings.
