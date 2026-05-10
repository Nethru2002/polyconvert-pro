import trimesh
from .base import BaseConverter

class ThreeDConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        formats = ['obj', 'stl', 'ply', 'off', 'glb']
        return source_ext in formats and target_ext in formats

    def convert(self, input_path, output_path):
        mesh = trimesh.load(input_path)
        mesh.export(output_path)
        return True