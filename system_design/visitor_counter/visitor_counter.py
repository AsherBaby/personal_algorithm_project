"""
Count how many visitors has come to store in an hour with precision to a minute.
"""
from datetime import datetime, timedelta


class VisitorCounter:

    def __init__(self):
        self.time_bucket = [[datetime.now(), 0] for _ in range(60)]
        self.total_count = 0
        self.start_time = datetime.now()

    def log(self, dt):
        # dt: datetime
        idx = (dt - self.start_time) % timedelta(hours=1) // timedelta(minutes=1)
        if dt - self.time_bucket[idx][0] < timedelta(hours=1):
            self.time_bucket[idx][1] += 1
            self.total_count += 1
        else:
            self.total_count -= self.time_bucket[idx][1] - 1
            self.time_bucket[idx] = [dt, 1]

    def get(self):
        return self.total_count
