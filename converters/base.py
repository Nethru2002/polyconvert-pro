from abc import ABC, abstractmethod

class BaseConverter(ABC):
    @abstractmethod
    def can_handle(self, source_ext, target_ext):
        """Check if this plugin can handle the conversion"""
        pass

    @abstractmethod
    def convert(self, input_path, output_path):
        """Perform the actual conversion"""
        pass