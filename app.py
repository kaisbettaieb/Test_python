from fastapi import FastAPI, Query, Response
from util import NotEnoughNumbers, InvalidOperand, operand, BaseReponseModele, OperationReponseModel, \
    ErreurReponseModele
from typing import Union

app = FastAPI(title="Calculatrice RPN",
              description="Réalisation d’une calculatrice RPN (notation polonaise inversée) en mode client/serveur",
              version="0.1")
pile = []


@app.post("/api/0.1/ajouter", response_model=Union[BaseReponseModele, ErreurReponseModele])
def ajouter_elem(response: Response, elem: int):
    if isinstance(elem, int):
        pile.append(elem)
        response.status_code = 200
        return {"status": "Success", "pile": pile}
    else:
        response.status_code = 400
        return {"status": "Erreur", "msg": "L'element doit étre un entier"}


@app.get("/api/0.1/recuperer", response_model=BaseReponseModele)
def recuperer_pile(response: Response):
    response.status_code = 200
    return {"status": "Success", "pile": pile}


@app.delete("/api/0.1/nettoyer", response_model=BaseReponseModele)
def nettoyer_pile(response: Response):
    pile.clear()
    response.status_code = 200
    return {"status": "Success", "pile": pile}


@app.post("/api/0.1/operation", response_model=Union[OperationReponseModel, ErreurReponseModele])
def operation(
        response: Response, op: str = Query(None, title="Operation",
                                            description="L'operation que vous voullez appliquer "
                                                        "sur les deux derniers elements de la liste.")):
    if len(pile) < 2:
        response.status_code = 400
        return {"status": "Erreur", "msg": "Il doit y avoir au minimum deux éléments dans la pile"}
    try:
        result = operand(pile, op)
        response.status_code = 200
        return {"status": "Success", "pile": pile, "operation": op, "resultat": result}
    except NotEnoughNumbers as e:
        response.status_code = 500
        return {"status": "Erreur", "msg": e.args[0]}
    except InvalidOperand as e:
        response.status_code = 400
        return {"status": "Erreur", "msg": e.args[0]}
    except ZeroDivisionError:
        response.status_code = 500
        return {"status": "Erreur", "msg": "Veuillez verifier que le dernier nombre de la pile n'est pas un zero"}
