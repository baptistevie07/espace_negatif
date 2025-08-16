import csv
import threading
import time
import os

class enregistrement():
    def __init__(self,filename):
        self._state = {
            "file": None,
            "writer": None,
            "lock": threading.Lock(),
            "frame_count": 0,
            "flush_every": 30,
            "fieldnames": ["timestamp","id","n_triangles", "distance_min", "angle_max", "min_count", "min_dist", "ratio_threshold", "nb_min_region", "min_density", "max_dist_between_2_persons", "ratio_area", "min_ratio", "life_threshold"]
        }
        self.data = {}
        self.filename = filename
        self.start_csv()
    def init_frame(self):
        self.data = {}
    def save_data(self,fieldname,data):
        #print(data)
        if False: #Test
            self.data[1] = {}
            self.data[2] = {}
            self.data[1][fieldname] = 3
            self.data[2][fieldname] = 4
            return
        print(data)
        for id,value in data.items():
            if id not in self.data:
                self.data[id] = {}
            self.data[id][fieldname] = value
    def start_csv(self, append=False, buffering=65536):
        """
        Ouvre le fichier et prépare un DictWriter.
        - fieldnames: liste/tuple de noms de colonnes
        - append: True = ajouter, False = recréer
        """
        if self._state["file"] is not None:
            return

        mode = "a" if append else "w"
        path = "records"
        os.makedirs(path, exist_ok=True)
        f = open(path+"/"+self.filename, mode, newline="", buffering=buffering)
        writer = csv.DictWriter(f, fieldnames=self._state["fieldnames"])

        if not append:
            writer.writeheader()

        self._state["writer"]=writer
        self._state["file"]=f
    

    def write_frame(self, timestamp=None):
        """
        Ajoute une ligne au CSV avec un dictionnaire.
        - data: dict {colonne: valeur}
        - timestamp: si fourni, remplace la clé 'timestamp' (si elle existe dans les fieldnames)
        """
        if self._state["writer"] is None:
            raise RuntimeError("start_csv() doit être appelé avant write_frame().")
        data=dict(self.data)  # Copie des données pour éviter les modifications concurrentes
        rows = []
        for id_key, inner in data.items():  # data = dict[id] -> dict
            # base: toutes les colonnes à None
            row = {k: None for k in self._state["fieldnames"]}

            # copier seulement les clés connues
            for k, v in inner.items():
                if k in row:
                    row[k] = v

            # id + timestamp
            row["id"] = id_key
            if "timestamp" in self._state["fieldnames"]:
                row["timestamp"] = timestamp if timestamp is not None else time.time()

            rows.append(row)

        with self._state["lock"]:
            print(rows)
            for r in rows:
                self._state["writer"].writerow(r)
                self._state["frame_count"] += 1

            fe = self._state["flush_every"]
            if fe > 0 and (self._state["frame_count"] % fe == 0):
                self._state["file"].flush()



    def stop_csv(self):
        if self._state["file"] is None:
            return
        with self._state["lock"]:
            self._state["file"].flush()
            self._state["file"].close()
            self._state.update({"file": None, "writer": None, "fieldnames": None})
