import csv


def fn_oldschool(annee_de_sortie):
    if annee_de_sortie < 2006:
        return True
    else:
        return False


def fn_encode(nom_du_jeu, editeur, genre, annee_de_sortie, plateforme, note):
    file_csv = "projet_jeuxdugrenier.csv"
    header = ["nom_du_jeu", "editeur", "genre", " annee_de_sortie", "plateforme", "note"]
    data = [nom_du_jeu, editeur, genre, annee_de_sortie, plateforme, note]
    with open(file_csv, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)


def fn_question(question):
    return input(question)


q_nom_du_jeu = "Nom du jeu:"
nom_du_jeu = fn_question(q_nom_du_jeu)
q_editeur = "Editeur : "
editeur = fn_question(q_editeur)
q_genre = "Genre : "
genre = fn_question(q_genre)
q_annee_de_sortie = "Année de sortie :"
annee_de_sortie = int(fn_question(q_annee_de_sortie))
q_plateforme = "Plateforme : "
plateforme = fn_question(q_plateforme)
q_note = "Note : "
note = fn_question(q_note)
fn_encode(nom_du_jeu, editeur, genre, annee_de_sortie, plateforme, note)

if fn_oldschool(annee_de_sortie):
    print(nom_du_jeu,"","est ancien")
else:
    print(nom_du_jeu,"","est récent")