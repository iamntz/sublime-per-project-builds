import sublime, sublime_plugin

class BuildSelector(sublime_plugin.WindowCommand):
  def run(self):
    win                = self.window
    project            = win.project_data();
    self.build_systems =  project.get('build_systems');
    panel_systems      = []

    for i in range(len(self.build_systems)):
      panel_systems.append( self.build_systems[i].get('name') )
    self.window.show_quick_panel(panel_systems, self.start_building)

  def start_building( self, selected_index ):
    if( selected_index == -1 ):
      return
    selected_build = self.build_systems[selected_index]
    self.window.run_command("set_build_system", { "file": selected_build.get('name') })
    self.window.run_command("build")