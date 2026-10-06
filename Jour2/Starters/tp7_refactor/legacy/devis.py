# -*- coding: utf-8 -*-
# Module hérité « devis » — volontairement difficile à maintenir (TP 7).
# Ne pas modifier avant d'avoir un plan de refactor validé et des tests qui protègent le comportement.

resultats = []


def traiter(d):
    # d = {"client": "ACME", "lignes": [("Stylo", 10, 1.5)], "pays": "FR", "vip": False}
    total = 0
    for l in d["lignes"]:
        total = total + l[1] * l[2]
    if d["vip"] == True:
        if total > 1000:
            remise = total * 0.15
        else:
            remise = total * 0.05
    else:
        if total > 1000:
            remise = total * 0.1
        else:
            remise = 0
    ht = total - remise
    if d["pays"] == "FR":
        tva = ht * 0.2
    elif d["pays"] == "DE":
        tva = ht * 0.19
    elif d["pays"] == "BE":
        tva = ht * 0.21
    else:
        tva = 0
    ttc = ht + tva
    resultats.append((d["client"], round(ttc, 2)))
    s = ""
    s = s + "Client: " + d["client"] + "\n"
    s = s + "Total brut: " + str(round(total, 2)) + "\n"
    if remise > 0:
        s = s + "Remise: " + str(round(remise, 2)) + "\n"
    s = s + "Total HT: " + str(round(ht, 2)) + "\n"
    s = s + "TVA: " + str(round(tva, 2)) + "\n"
    s = s + "Total TTC: " + str(round(ttc, 2)) + "\n"
    return s


def resume():
    # résumé de tous les devis traités depuis le démarrage
    if len(resultats) == 0:
        return "Aucun devis"
    t = 0
    for r in resultats:
        t = t + r[1]
    m = 0
    for r in resultats:
        if r[1] > m:
            m = r[1]
    s = ""
    s = s + "Nombre de devis: " + str(len(resultats)) + "\n"
    s = s + "Total TTC cumulé: " + str(round(t, 2)) + "\n"
    s = s + "Devis le plus élevé: " + str(round(m, 2)) + "\n"
    return s
