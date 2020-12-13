import numpy as np

EARTH_D = 6371

class parking_block():
    def __init__(self, params, dist):
        # params are from csv file
        # dist records the distance between each two blocks

        self.block_id = params['BLOCKFACE_ID']
        self.loc = (params['LONGITUDE'], params['LATITUDE'])
        self.capacity = params['SPACE_NUM']
        self.occupied = 0   # the count of occupied meters
        self.backup_block = np.argsort(dist)    # the priority of back-up blocks

class vehicle():
    def __init__(self, params):
        self.loc_arrive = params['id']
        self.loc_current = params['id']
        self.parked = False
        self.remaining_time = 0

    def decrease_1(self):
        self.remaining_time -= 1

class parking_env():
    def __init__(self, df):
        self.t = 0
        mat_distance = self.great_circle_v(df['LONGITUDE'].values, df['LATITUDE'].values)
        self.blocks = [parking_block(record, mat_distance[i]) for i, record in enumerate(df.to_dict('records'))]
        self.vehicles = []

    # calculate the great circle distance for all the blocks with matrix form
    def great_circle_v(self, lon, lat):
        lon, lat = np.radians(lon), np.radians(lat)
        return EARTH_D * np.arccos(np.sin(lat) * np.sin(lat).reshape(-1, 1) \
                + np.cos(lat) * np.cos(lat).reshape(-1, 1) * np.cos(lon-lon.reshape(-1, 1)))

    def generate_demand(self):
        return

    # simulate the parking behavior with choice model
    def do_simulation(self):
        # parked vehicles
        ind_vehicles = []
        for i, vehicle in enumerate(self.vehicles):
            vehicle.decrease_1()
            if vehicle.remaining_time == 0:
                self.blocks[vehicle.loc_current].occupied -= 1
            else:
                ind_vehicles.append(i)
        self.vehicles = self.vehicles[ind_vehicles]

        # parking vehicles

        return

    # given the action, simulate the process and get the reward
    def step(self, a):
        d = self.generate_demand()
        self.do_simulation()
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