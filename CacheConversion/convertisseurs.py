# convertisseurs.py

class ConvertisseurCSVversJSON:
    def convertir(self, contenu: str) -> str:
        import json, csv, io
        lecteur = csv.DictReader(io.StringIO(contenu))
        return json.dumps(list(lecteur), ensure_ascii=False)

class ConvertisseurJSONversCSV:
    def convertir(self, contenu: str) -> str:
        import json, csv, io
        donnees = json.loads(contenu)
        if not donnees:
            return ""
        sortie = io.StringIO()
        writer = csv.DictWriter(sortie, fieldnames=donnees[0].keys(),
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(donnees)
        return sortie.getvalue()