from pathlib import Path
from typing import Union

def write_file(filepath: Union[str, Path], content: str) -> None:
    path = Path(filepath)
    
    if not str(path).endswith('.txt'):
        path = Path(str(path) + '.txt')
    
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

def append_file(filepath: Union[str, Path], content: str) -> None:
    path = Path(filepath)
    
    if not str(path).endswith('.txt'):
        path = Path(str(path) + '.txt')
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with path.open('a', encoding='utf-8') as f:
        f.write(content)

def read_file(filepath: Union[str, Path]) -> str:
    path = Path(filepath)
    
    if not str(path).endswith('.txt'):
        path = Path(str(path) + '.txt')
    
    return path.read_text(encoding='utf-8')
