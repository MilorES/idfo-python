import json

if __name__ == "__main__":
    try:
        file = open("amigos.json","r")
        amigos = json.load(file)
    except FileNotFoundError as err:
        print("Error IO")
    finally:
        if file is not None:
            file.close()

coches = [
    { "marca":"Seat", "model":"Ateca"},
    { "marca":"Seat", "model":"Ibiza"}
]

file = open("coches.json", "w")
json.dump(coches,file)
file.close()
