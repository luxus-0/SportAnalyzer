class ActivityStatistics:

    def __init__(self):
        self.distance_m = 0.0
        self.moving_time_s = 0
        self.elapsed_time_s = 0

        self.avg_speed = 0.0
        self.max_speed = 0.0

        self.avg_heart_rate = None
        self.max_heart_rate = None

        self.total_elevation_gain = 0.0