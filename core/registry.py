class ConverterRegistry:
    def __init__(self):
        self._converters = []

    def register(self, converter_instance):
        """Adds a new converter to the system"""
        self._converters.append(converter_instance)

    def get_converter(self, source_ext, target_ext):
        """Finds the right converter for the job"""
        for converter in self._converters:
            if converter.can_handle(source_ext, target_ext):
                return converter
        return None

# Global instance to be used across the app
registry = ConverterRegistry()