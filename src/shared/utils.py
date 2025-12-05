from pathlib import Path

def read_input(day: int, part: int = 1) -> str:
    """
    Lê o arquivo de input de um dia específico.
    
    Args:
        day: número do dia (1, 2, 3...)
        part: número da parte (1 ou 2), default 1
    
    Returns:
        Conteúdo do arquivo como string
    """
    project_root = Path(__file__).parent.parent
    input_file = project_root / f"day{day}" / "data" / f"puzzle_part{part}_input.txt"

    with open(input_file, 'r') as f:
        return f.read()

def parse_lines(text: str) -> list[str]:
    """
    Divide texto em linhas, removendo espaços extras e linhas vazias.
    
    Args:
        text: texto com múltiplas linhas
    
    Returns:
        Lista de linhas limpas
    """
    return [line.strip() for line in text.strip().split('\n') if line.strip()]
