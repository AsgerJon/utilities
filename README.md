# vistutils

vistutils is a collection of modules providing helpful utility functions. The latest release includes the following functions:

## waila - what am I looking at?

Instead of writing something like:
~~~
for item in dir(obj):
  print(item)
~~~
Simply use waila(obj)! This prints the name of each entry like above including the documentation associated with the object. 
waila supports the following keyword flags:
dunder
: Includes dunder methods of the objects (default False)

magic 
: alias for dunder (default False)

getReturn
: if True, waila(obj) returns items as a list of dictionaries with keys: 'name', 'type' and 'help'

fid 
: saves the results to a text file of this name.

save
: if True, saves results to textfile, ignored if fid is given, otherwise a filename is generated, which includes the name of the object and the time of save.
