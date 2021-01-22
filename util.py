from pydantic import BaseModel


class NotEnoughNumbers(Exception):
    """ Elever quand les nombres de valeurs dans pile est inferieur à 2"""
    pass


class InvalidOperand(Exception):
    """ Elever quand l'operand n'est pas valide"""
    pass


class ErreurReponseModele(BaseModel):
    status: str
    msg: str


class BaseReponseModele(BaseModel):
    status: str
    pile: list


class OperationReponseModel(BaseReponseModele):
    operation: str
    resultat: float


operations = ["+", "-", "*", "/"]


def operand(pile: [], op: str) -> float:
    """
    Cette fonction fait l'operand demandé sur les deux derniers nombres de la pile,
    elle eleve une parmi 3 exceptions selon les conditions.
    :param pile: une liste qui continet les nombres
    :param op: l'operation a effectuer au 2 derniers nombres
    :return: float la resultat de la operation
    """
    if len(pile) < 2:
        raise NotEnoughNumbers("Vezillez verifier qu'il existe au moin 2 element à la pile")
    if op not in operations:
        raise InvalidOperand("Veuillez verifier que l'operand est valide")
    result = 0
    a, b = pile[-2], pile[-1]
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    else:
        if b == 0:
            raise ZeroDivisionError("Veuillez verifier que le dernier element de la pile n'est 0")
        else:
            result = a / b
    del pile[-2]
    del pile[-1]
    pile.append(result)
    return result
