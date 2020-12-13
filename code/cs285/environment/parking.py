import numpy as np

EARTH_D = 6371

class parking_block():
    def __init__(self, id, lon, lat, cap, params):
        self.id = id
        self.loc = (lon, lat)
        self.cap = cap
        self.occupied = 0

class parking_env():
    def __init__(self, df):
        self.t = 0
        self.mat_distance = self.great_circle_v(df['LONGITUDE'].values, df['LATITUDE'].values)
        self.blocks = parking_block()

    def great_circle_v(self, lon, lat):
        return EARTH_D * np.acos(np.sin(lat) * np.sin(lat).reshape(-1, 1) \
                + np.cos(lon) * np.cos(lon).reshape(-1, 1) * np.cos(lon-lon.reshape(-1, 1)))

    def step(self, a):
        return

    def _get_obs(self):
        pass

    def reset_model(self):
        pass

    def viewer_setup(self):
        pass