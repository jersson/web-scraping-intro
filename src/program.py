from .Mathematicians import Mathematicians

mathematicians = Mathematicians()
names = mathematicians.list_names(10)

print('Greatest Mathematicians of the Past')
for name in names:
    print('- {}'.format(name))
