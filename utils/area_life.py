import time

class Life:
    def __init__(self, min_ratio, life_threshold=10):
        self.min_ratio = min_ratio
        self.life_threshold = life_threshold
        self.born = time.time()
        self.count =[0]*100 #File to store the count of active and inactive states
        self.area_on = False  # Indicateur pour savoir si l'area est active
        
    def update(self, computation):
        nb_regions = 0
        if computation.region_candidates is not None:
            nb_regions += len(computation.region_candidates)
        if computation.region_empty is not None:
            nb_regions += len(computation.region_empty)
        area_on = (nb_regions > 0)
        self.count.pop(0)
        if area_on:
            self.count.append(1)
        else:
            self.count.append(0)
        if sum(self.count) / len(self.count) < self.min_ratio:
            self.born = time.time()
            self.area_on = False
        else:
            self.area_on = True