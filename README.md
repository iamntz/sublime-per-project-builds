sublime-per-project-builds
==========================
### What is this?
Did you ever had a project with multiple build systems on Subilme Text? I know I did and was pretty annoying to change build systems every now and then. Therefore I made this neat plugin, which displays a small popup with all builds defined in a project. Plain and simple :)

### Add this in your `.sublime-keymap` file
(and probably change the shortcut?)

```json
{ "keys": ["ctrl+shift+b"], "command": "build_selector" }
```

_This is tested only on Sublime Text 3. I'm not planning to offer support for ST2_
