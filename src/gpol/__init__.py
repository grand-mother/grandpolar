import pathlib

def get_path_gp300():
    here = pathlib.Path(__file__)
    return here.parent.parent.parent / "gp300"