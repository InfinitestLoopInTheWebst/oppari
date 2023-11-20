from pathlib import Path
from typing import Union

def get_file_path(
    root: Path,
    *args,
    return_type: Union[Path, str] = Path
) -> Union[Path, str]:
    if return_type == Path:
        return Path(root, *args)
    elif return_type == str:
        return str(Path(
            root,
            *args
        )).replace('\\', '/')
    raise ValueError('Invalid return type specified')
    
