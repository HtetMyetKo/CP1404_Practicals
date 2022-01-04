
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934
"""CONSTANT"""

class MilesConverterApp(App):

    message = StringProperty()

    def build(self):

        """MAIN PROGRAM"""

        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):

        """CONVERSION"""

        value = self.handle_invalid()
        result = value * MILES_TO_KM_CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):

        """INCREMENT"""

        value = self.handle_invalid() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def handle_invalid(self):

        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()
