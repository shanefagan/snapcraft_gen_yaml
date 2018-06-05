"""Generate the snapcraft YAML per release for CI."""
import yaml
import datetime

app_name = 'test'
summary = 'Testing generation of snapcraft.yaml on the fly'
description = 'This is designed to run mostly on jenkins and be able ' \
'to run before snapcraft to automagically do version control'
snap_dict = dict()
snap_dict['name'] = app_name
version = datetime.datetime.now().strftime('%Y%m%d')
snap_dict['version'] = version
snap_dict['summary'] = summary
snap_dict['description'] = description

snap_dict['grade'] = 'devel'
snap_dict['confinement'] = 'devmode'

part_name = "my-snap-name"
plugin = 'python'
python_version = 'python3'
source = '.'
app_parts = dict()
app_parts['{}'.format(part_name)] = dict()
app_parts['{}'.format(part_name)]['plugin'] = plugin
app_parts['{}'.format(part_name)]['python-version'] = python_version
app_parts['{}'.format(part_name)]['source'] = source

snap_dict['parts'] = app_parts

cmd = 'bin/main'
snap_dict['apps'] = dict()
snap_dict['apps']['{}'.format(app_name)] = dict()
snap_dict['apps']['{}'.format(app_name)]['command'] = cmd
with open('snapcraft.yaml', 'w') as yaml_file:
    yaml.safe_dump(snap_dict, yaml_file)
