import jinja2
import json
import os

template_file = "1_monkeys_wearing_hats.j2"
json_parameter_file = "parameters2.json"
output_directory = "_output"

# read the contents from the JSON files
print("Read JSON parameter file...")
config_parameters = json.load(open(json_parameter_file))

# next we need to create the central Jinja2 environment and we will load
# the Jinja2 template file (the two parameters ensure a clean output in the
# configuration file)
print("Create Jinja2 environment...")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                         trim_blocks=True,
                         lstrip_blocks=True)
template = env.get_template(template_file)

# we will make sure that the output directory exists
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

f = open(os.path.join(output_directory, "problems.txt"), "w")
problem=1
# now create the templates
print("Create templates...")
for parameter in config_parameters:
    result = template.render(parameter)
    f.write("\n\nProblem : %d\n" % problem)
    f.write(result)
    problem+=1

print("File '%s' created..." % "problems.txt")
print("DONE")
f.close()