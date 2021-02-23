#class - Template
#object - Instance of the class
#DRY - Do not repeat Yourself
#get_no of films(table)


from string import Template

my_template = Template('My name is davide')

print(my_template.substitute({'x': "davide"}))
