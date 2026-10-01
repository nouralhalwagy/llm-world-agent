world = {
    "robot":{"location": "table", "holding": None},
    "objects": {
        "red_cup": {"location": "table", "fragile": True},
        "book": {"location": "shelf", "fragile": False},
        "key": {"location": "drawer", "fragile": False}
    },
    "places": ["table", "shelf", "drawer", "box"]
    
}

def look() -> str:
    """Shows where the robot actually is, and what he's doing now."""
    r = world["robot"]
    objs = {n:o["location"] for n,o in world["objects"].items()}
    return f"Robot is at {r['location']}, holding {r['holding']}. Objects: {objs}. Places: {world['places']}"



def move_to(place: str) -> str:
    """Moves the robot to a new place."""
    if place not in world["places"]:
        return f"Place '{place}' does not exist."
    world["robot"]["location"] = place
    return f"Robot moved to {place}."



def pick_up(obj: str) -> str:
    """ picks up an object at the robot's current location. """
    r= world["robot"]
    if r["holding"]:
        return f"Robot is already holding {r['holding']}."
    o = world["objects"].get(obj)
    if o is None:
        return f"Object '{obj}' does not exist."
    if o["location"] != r["location"]:
        return f"Object '{obj}' is not at the robot's current location."
    r["holding"] = obj
    o["location"] = "held"
    return f"Robot picked up {obj}."



def put_down() -> str:
    """ puts down the object the robot is holding at the robot's current location. """
    r = world["robot"]
    if not r["holding"]:
        return "Robot is not holding anything."
    obj = r["holding"]
    world["objects"][obj]["location"] = r["location"]
    r["holding"] = None
    return f"Robot put down {obj} at {r['location']}."

