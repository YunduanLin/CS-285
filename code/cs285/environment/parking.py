import numpy as np

EARTH_D = 6371
MAX_E = 10
VOT = 0.1
SPEED = 30

class parking_block():
    def __init__(self, params, dist):
        # params are from csv file
        # dist records the distance between each two blocks

        self.block_id = params['BLOCKFACE_ID']
        self.loc = (params['LONGITUDE'], params['LATITUDE'])
        self.capacity = params['SPACE_NUM']
        self.occupied = 0   # the count of occupied meters
        self.dist = np.sort(dist)
        self.backup_block = np.argsort(dist)    # the priority of back-up blocks

    def is_full(self):
        return self.capacity == self.occupied

    def inc_v(self):
        self.occupied += 1

    def dec_v(self):
        self.occupied -= 1

class vehicle():
    def __init__(self, params):
        self.loc_arrive = params['id']
        self.ind_loc_current = 0
        self.cruising_dist = 0
        self.parked = False
        self.fee = 0
        self.remaining_time = 0

    def dec_time(self):
        self.remaining_time = self.remaining_time - 1 if self.remaining_time == 0 else 0

    def inc_ind_loc(self):
        self.ind_loc_current += 1

class parking_env():
    def __init__(self, df):
        self.t = 0
        mat_distance = self.great_circle_v(df['LONGITUDE'].values, df['LATITUDE'].values)
        self.blocks = [parking_block(record, mat_distance[i]) for i, record in enumerate(df.to_dict('records'))]
        self.vehicles = np.empty(1)

    # calculate the great circle distance for all the blocks with matrix form
    def great_circle_v(self, lon, lat):
        lon, lat = np.radians(lon), np.radians(lat)
        return EARTH_D * np.arccos(np.sin(lat) * np.sin(lat).reshape(-1, 1) \
                + np.cos(lat) * np.cos(lat).reshape(-1, 1) * np.cos(lon-lon.reshape(-1, 1)))

    # generate demand for each block at time t
    def generate_demand(self):
        return np.ones(len(self.blocks))

    def simulate_v_park(self, v, p):
        ind_cur_block = self.blocks[v.loc_arrive].backup_block[v.ind_loc_current]
        if not self.blocks[ind_cur_block].is_full():
            if np.random.rand() > 0.1:
                v.parked = True
                self.blocks[ind_cur_block].inc_v()
                v.remaining_time = 2
                v.fee = v.remaining_time * p[ind_cur_block]
            else:
                v.inc_ind_loc()
                new_ind_block = self.blocks[v.loc_arrive].backup_block[v.ind_loc_current]
                v.cruising_dist = self.blocks[ind_cur_block].dist[new_ind_block]


    # simulate the parking behavior with choice model
    def do_simulation(self, a):
        self.t += 1

        # parked vehicles
        ind_vehicles = []
        for i, v in enumerate(self.vehicles):
            v.decrease_time()
            if v.remaining_time == 0:
                self.blocks[v.loc_current].dec_v()
            else:
                ind_vehicles.append(i)
        self.vehicles = self.vehicles[ind_vehicles]

        # parking vehicles
        num_parked_vehicles = len(self.vehicles)
        d = self.generate_demand()
        for block in self.blocks:
            self.vehicles = np.append(self.vehicles, [vehicle({'id': block}) for _ in range(d[block])])
        for t_e in range(MAX_E-1):
            for v in self.vehicles[num_parked_vehicles:]:
                if not v.parked:
                    self.simulate_v_park(v, a)

        reward = 0
        for v in self.vehicles[num_parked_vehicles:]:
            reward += v.fee - v.cruising_dist * SPEED

        return reward

    # given the action, simulate the process and get the reward
    def step(self, a):
        reward = self.do_simulation(a)

        return reward

    def _get_obs(self):
        pass

    def reset_model(self):
        pass

    def viewer_setup(self):
        pass