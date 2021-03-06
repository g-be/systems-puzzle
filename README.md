# NOTES [Insight DevOps Engineering Systems Puzzle]

## pre
install github for windows
install docker for windows
fork systems-puzzle
pull systems-puzzle
run readme commands

## main
localhost:8080 is not returning anything, check ports aligned properly

change docker-compose nginx ports from 80:8080 to 8080:80
success, but now bad gateway 502

remove -d option from docker-compose to see (very helpful) output and errors

logs suggest flaskapp is on port 5000 but the config looks for flaskapp on port 5001
change flaskapp.conf to 5000 and dockerfile to 5000 seems to fix this
no more 502 error

when entering a non-integer value for quantity field, error is returned. looking into wtforms.validators for integers...
fixed by adding import IntegerField

when submitting valid data, redirection is broken (goes to localhost%2Clocalhost:port)
the flask documentation doesnt include the leading slash slash, attempting to fix by removing leading '/' in @app.route
nvm that returns an error
the proper fix is to edit the flaskapp.conf file and remove the redundant 'proxy_set_header Host' line

now the redirection works, but the output is ... incomplete. it appears that the database is not read properly or not written to properly
time to rtfm... the flask sqlalchemy manual
seems the models.py file needs an \_\_init__ and \_\_repr__ function 
still not printing... I either need a str method or to alter the call to be repr

after including a \_\_str__ method, there still was no output to the page. in response, I'm going to convert the 'results' list into a multiline string

to get the 'multiline' string I have to change the mimetype of the data (when interpreted as html, the '\n' newline character is disregarded, hence I needed to use the a mimetype of 'text/plain')

## bonus
at this point, I don't see any more bugs, so let's add a bit of functionality: i want to include a new page where you can see the database items without requiring an insert first

just duplicate the html form button (with a different name) which calls a duplicate success() method (with a different name. I could have simply called the same one 'success' page but I wanted a distinct url).
