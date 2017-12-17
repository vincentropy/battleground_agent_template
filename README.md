# Agent Template
Develop your own agents for the battleground platform

## System setup
You can develop agents using any of your own favorite tools,
just adapt the my_agent.py and/or my_persistent_agent.py examples.

Debugging your agents locally requires you to run the battleground platform locally.
There are 2 ways to do this:
1. Using a virtual machine and vagrant
2. Running/Installing natively

### 1. Using Vagrant  
If you are already familiar with Vagrant, this is probably the easiest way to go.
Make sure you follow all the [installation instructions for vagrant.](https://www.vagrantup.com/docs/installation/)
Then run
```
vagrant up
```
in the folder that contains the Vagantfile supplied in this repo.

you can then connect to your virtual machine using
```
vagrant ssh
```

### 2. Native setup
This method is a bit more involved.
- [install Docker](https://www.docker.com/community-edition)
- [install python 3 on your system](https://www.python.org/)
- your probably want to [create a virtual environment](https://docs.python.org/3/tutorial/venv.html)

then start a local mongoDB container:
```
docker run docker run -d mongo
```

**activate your virtual enviromnent** and then install the requirements:
```
pip install --upgrade -r requirements.txt
```

## Configuring and running a game

Ok, now we're ready to play!
edit the example_config.json file to determine what game configuration you want to play.
Then run the game server:
```
battleground_start --config ./example_config.json
```

The output should look something like:
```
starting battleground ...
basic_game
[6, 63.79083986857607, 105, 0]
[26, 101.94530518101656, 53, 1]
[0, 103.03455728229633, 68, 2]
```

These numbers are the final scores of each of the 4 players in each of the 3 games that were played.
