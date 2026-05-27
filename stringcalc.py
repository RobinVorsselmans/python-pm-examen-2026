"""String Calculator Kata"""


def add(expr: str) -> int:
    expr = _normalize_separators(expr)

    if not expr:
        return 0

    integers = _extract_integers(expr)
    _validate_integers(integers)

    return sum(_extract_integers(expr))


def _normalize_separators(expr: str) -> str:
    if expr.startswith("//"):
        custom_separator, expr = expr.split("\n", maxsplit=1)
        custom_separator = custom_separator[2:]
        expr = expr.replace(custom_separator, ",")

    return expr.replace("\n", ",")


def _extract_integers(expr: str) -> list[int]:
    return [int(i) for i in expr.split(",")]


def _validate_integers(integers: list[int]) -> None:
    negatives = [str(i) for i in integers if i < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {' '.join(negatives)}")
    return
