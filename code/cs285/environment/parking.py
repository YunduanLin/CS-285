import numpy as np

EARTH_D = 6371

class parking_block():
    def __init__(self, params):
        self.id = params['BLOCKFACE_ID']
        self.loc = (params['LONGITUDE'], params['LATITUDE'])
        self.cap = params['SPACE_NUM']
        self.occupied = 0

class parking_env():
    def __init__(self, df):
        self.t = 0
        mat_distance = self.great_circle_v(df['LONGITUDE'].values, df['LATITUDE'].values)
        self.blocks = [parking_block(record) for record in df.to_dict('records')]

    def great_circle_v(self, lon, lat):
        lon, lat = np.radians(lon), np.radians(lat)
        return EARTH_D * np.arccos(np.sin(lat) * np.sin(lat).reshape(-1, 1) \
                + np.cos(lat) * np.cos(lat).reshape(-1, 1) * np.cos(lon-lon.reshape(-1, 1)))

    def step(self, a):
        return

    def _get_obs(self):
        pass

    def reset_model(self):
        pass

    def viewer_setup(self):
        pass