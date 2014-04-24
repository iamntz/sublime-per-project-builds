# pylint: disable=F0401,C0111,W0232,E1101
import sublime_plugin
from threading import Timer

class BuildSelector(sublime_plugin.WindowCommand):
    def run(self):
        win = self.window
        project = win.project_data()
        self.build_systems = project.get("build_systems") #Get all sections
        self.config = self.build_systems.pop(0) #Get the config section and remove it from list
        self.timer = None
        self.default_index = 0
        self.already_run = False

        panel_names = []
        for index, build_system in enumerate(self.build_systems):
            name = build_system.get("name")
            if name == self.config.get("default"):
                self.default_index = index
            panel_names.append(name)

        timeout = self.config.get("autorun_default_timeout")
        timeout_valid = type(timeout) == type(int()) or type(timeout) == type(float())
        if len(panel_names) == 0: #Nothing to show
            return
        elif len(panel_names) == 1 and self.config.get("autorun_when_single"):
            self.start_building(0)
        elif timeout_valid and timeout == 0: #If timeout is 0, just run the default
            self.start_building(self.default_index)
        else: #Create the panel
            if timeout_valid:
                #Create the timeout timer, this will start another timer with real timeout
                #why this? because we need to avoid some random on_highlight triggers that ocurrs when creating panel...
                timer = Timer(0.2, self.start_timeout, [timeout])
                timer.start()
            self.window.show_quick_panel(
                panel_names,
                on_select = self.start_building,
                on_highlight = self.on_changed_selection,
                selected_index = self.default_index
            )

    def start_timeout(self, timeout):
        self.timer = Timer(timeout, self.on_autorun_timeout)
        self.timer.start()

    def cancel_timer(self):
        if self.timer != None:
            self.timer.cancel()
            self.timer = None

    def on_changed_selection(self, _):
        self.cancel_timer()

    def on_autorun_timeout(self):
        self.start_building(self.default_index)

    def start_building(self, selected_index):
        if self.already_run: #This was run before (happens when autoruns calls start_building, probably running start_building triggers the closing of panel)
            return
        self.already_run = True
        self.cancel_timer()
        if selected_index == -1: #User cancelled
            return
        selected_build = self.build_systems[selected_index]
        self.window.run_command("set_build_system", { "file": selected_build.get("name") })
        self.window.run_command("build")