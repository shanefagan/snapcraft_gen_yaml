**Usage**

cd snap

python3 yaml_gen.py

cd ..

snapcraft

**Rationale**

Basically meant to handle generation of snapcraft.yaml for use in CI tools where a human isn't interacting with the yaml file directly.

**Output**

It should output a nice snapcraft.yaml with valid yaml and no messing about with spaces or whatever and with generated version numbers...etc.

Version: year month day 20180506 style outputs to make sure each build version doesn't clash. It isn't awfully helpful but you can change it to be 0.1 0.2 0.3...etc if you want by adding in the extra step of reading the old yaml and then adding 1 to it. I prefer date based version numbers to pinpoint specific issues relating to different triggered builds so that is useful to me but maybe not to someone else.

name, description...etc are all the same as regular snapcraft.yaml configs so if you want to change that just change the variables that they are attached to. 
