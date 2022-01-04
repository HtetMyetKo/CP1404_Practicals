from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    """Main program."""

    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):

        """Build the Kivy GUI."""

        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):

        for name in self.names:
            return name
            self.root.ids.main.add_widget(name)


DynamicLabelsApp().run()