import numpy as np

EARTH_D = 6371

class parking_block():
    def __init__(self, params, dist):
        self.id = params['BLOCKFACE_ID']
        self.loc = (params['LONGITUDE'], params['LATITUDE'])
        self.cap = params['SPACE_NUM']
        self.occupied = 0
        self.backup_block = np.argsort(dist)

class parking_env():
    def __init__(self, df):
        self.t = 0
        mat_distance = self.great_circle_v(df['LONGITUDE'].values, df['LATITUDE'].values)
        self.blocks = [parking_block(record, mat_distance[i]) for i, record in enumerate(df.to_dict('records'))]

    def great_circle_v(self, lon, lat):
        lon, lat = np.radians(lon), np.radians(lat)
        return EARTH_D * np.arccos(np.sin(lat) * np.sin(lat).reshape(-1, 1) \
                + np.cos(lat) * np.cos(lat).reshape(-1, 1) * np.cos(lon-lon.reshape(-1, 1)))

    def generate_demand(self):
        return

    def do_simulation(self):
        return

    def step(self, a):
        d = self.generate_demand()
        for i, block in enumerate(self.blocks):
            for u in range(d[i]):
                self.do_simulation()
        return

    def _get_obs(self):
        pass

    def reset_model(self):
        pass

    def viewer_setup(self):
        pass