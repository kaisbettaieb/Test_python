from fastapi import FastAPI

app = FastAPI(version="0.1")
pile = []


@app.post("/api/0.1/ajouter")
def ajouter_elem(elem: int):
    pile.append(elem)
    return {"success": pile}


@app.get("/api/0.1/recuperer")
def recuperer_pile():
    return {"pile": pile}


@app.delete("/api/0.1/nettoyer")
def nettoyer_pile():
    pile.clear()
    return {"pile": pile}

@app.get("/api/0.1/operation")
def operation(op: str):
    operations = ["+", "-", "*", "/"]
    if len(pile) < 2:
        return {"Erreur": "Il doit y avoir au minimum deux éléments dans la pile"}, 500
    if op not in operations:
        return {"Erreur": "Veuillez verifier que l'operation est correct (+,-,*,/)"}
