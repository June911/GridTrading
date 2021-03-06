import os, sys

def get_results_path():
    return os.path.join(os.getcwd(), "results")

def get_data_path():
    return os.path.join(os.getcwd(), "data")

# handle print
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w", encoding="utf-8")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
