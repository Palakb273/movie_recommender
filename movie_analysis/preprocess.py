import ast
def parse_genres(x):
    try:
        genres=ast.literal_eval(x)
        return[d["name"].lower().replace(" ","")for d in genres]
    except:
        return[]
def parse_actors(x):
    try:
        actors=ast.literal_eval(x)
        return[d["name"].lower().replace(" ","")for d in actors[:3]]
    except:
        return[]
def parse_director(x):
    try:
        crew=ast.literal_eval(x)
        for d in crew:
            if d["job"]=="Director":
                return d["name"].lower().replace(" ","")
        return None
    except:
        return None
print("succesfully run")
    
