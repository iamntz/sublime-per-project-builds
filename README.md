sublime-per-project-builds
==========================
### What is this?
Did you ever had a project with multiple build systems on Subilme Text? I know I did and was pretty annoying to change build systems every now and then. Therefore I made this neat plugin, which displays a small popup with all builds defined in a project. Plain and simple :)

### Add this into your sublime-project file:
```json
"build_systems":
	[
		{
			"name": "Grunt Tasks:ALL",
			"shell_cmd": "grunt --no-color",
			"working_dir": "${project_path}"
		},
		{
			"name": "Grunt Tasks:CSS",
			"shell_cmd": "grunt css --no-color",
			"working_dir": "${project_path}"
		},
		{
			"name": "Grunt Tasks:JS",
			"shell_cmd": "grunt js --no-color",
			"working_dir": "${project_path}"
		}
	]
```


### Add this in your `.sublime-keymap` file
(and probably change the shortcut?)

```json
{ "keys": ["ctrl+shift+b"], "command": "build_selector" }
```


### Extra configuration
- "default": Sets the default selected build system (put here the "name")
- "autorun_when_single": Automatically runs the only available build system
- "autorun_default_timeout": Automatically runs the default if user doesn't change option (setting another thing than number will disable it)

### This is a example:
```json
"build_systems":
	[
		{
			"default": "Grunt Tasks:CSS",
			"autorun_when_single": true,
			"autorun_default_timeout": 5.0
		},
		{
			"name": "Grunt Tasks:ALL",
			"shell_cmd": "grunt --no-color",
			"working_dir": "${project_path}"
		},
		{
			"name": "Grunt Tasks:CSS",
			"shell_cmd": "grunt css --no-color",
			"working_dir": "${project_path}"
		},
		{
			"name": "Grunt Tasks:JS",
			"shell_cmd": "grunt js --no-color",
			"working_dir": "${project_path}"
		}
	]
```

![](http://img.iamntz.com/jing/2013-02-27_17h26_06.png)

_This is tested only on Sublime Text 3. I'm not planning to offer support for ST2_
