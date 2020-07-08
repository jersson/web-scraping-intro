from Mathematicians import Mathematicians

mathematicians = Mathematicians()
names = mathematicians.list_names()

print('Greatest Mathematicians of the Past')
for name in names:
    print('- {}'.format(name))
