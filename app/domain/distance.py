class Distance:
    meters: float

    def __init__(self, meters):
        self.meters = meters

    def add(self, other: "Distance") -> "Distance":
        return Distance(self.meters + other.meters)