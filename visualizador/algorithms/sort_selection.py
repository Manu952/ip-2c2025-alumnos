items = []
n = 0
i = 0      
j = None   
def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      
    j = None

def step():
    global items, n, i, j

    if i >= n:
        return {"done": True}

   
    if j is None:
        j = i
        return {"a": j, "b": j - 1 if j > 0 else j, "swap": False, "done": False}

    # Si estamos en una posición válida y hay que mover el elemento hacia la izquierda
    if j > 0 and items[j - 1] > items[j]:
        items[j - 1], items[j] = items[j], items[j - 1]
        j -= 1
        return {"a": j, "b": j + 1, "swap": True, "done": False}

    # Si ya no hay que desplazar más, pasamos al siguiente elemento
    i += 1
    j = None

    return {"a": i - 1, "b": i, "swap": False, "done": False}
