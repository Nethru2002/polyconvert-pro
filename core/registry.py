import concurrent.futures
from tqdm import tqdm

class ConverterRegistry:
    def __init__(self):
        self._converters = []

    def register(self, converter_instance):
        self._converters.append(converter_instance)

    def get_converter(self, source_ext, target_ext):
        for converter in self._converters:
            if converter.can_handle(source_ext, target_ext):
                return converter
        return None

    def convert_batch(self, tasks, max_workers=4):
        """
        tasks: list of tuples (input_path, output_path, converter_obj)
        """
        results = []
        with tqdm(total=len(tasks), desc="Converting Files") as pbar:
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {executor.submit(t[2].convert, t[0], t[1]): t for t in tasks}
                for future in concurrent.futures.as_completed(futures):
                    results.append(future.result())
                    pbar.update(1)
        return results

registry = ConverterRegistry()