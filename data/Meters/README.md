# Parking Meters Data Description

The data comes from [__DataSF__](https://data.sfgov.org/Transportation/Parking-Meters/8vzz-qzz9).

### Important features:

| Column Name | Description | Type |
| --- | --- | --- |
| POST_ID | Unique identifier of meter | Text |
| ON_OFFSTREET_TYPE | Whether the space is on the street or off‐street, e.g. metered parking lot--OFF Off‐street,ON On‐street | Categorical |
| PM_DISTRICT_ID | Parking Management District ID | Number |
| BLOCKFACE_ID | Blockface (side of street) ID | Number |
| METER_TYPE | How many spaces the meter manages-SS - Single‐space,MS - Multi‐space | Categorical |
| CAP_COLOR | Cap color describes the use and restrictions of the meter--Black - Motorcycle parking,Brown - Tour bus parking,Green - Short term parking,Grey - General metered parking,Purple - Boat trailer parking,Red - Six wheeled commercial vehicle parking,Yellow - Commercial vehicle parking | Categorical |
| OLD_RATE_AREA | Hourly rate zone of the meter; some variations within each zone--Area 1 - Downtown primarily \$3.50,Area 2 -Surrounding downtown primarily \$3.00,Area 3 -Residential neighborhood primarily \$2.00,Area 5 -SFpark area variable rates ranging from \$0.25 to \$6.00,MC1 -Motorcycle in Area 1 primarily \$0.70,MC2 -Motorcycle in Area 2 primarily \$0.60,MC3 -Motorcycle in Area 3 primarily \$0.40,MC5 -Motorcycle in SFpark area variable rates ranging from \$0.25 to \$6.00,Port 1 -Port‐owned at Fisherman’s Wharf \$2.50,Port 2 -Port‐owned at Fisherman’s Wharf \$2.50,Port 3 -Port‐owned at North Embarcadero \$2.00,Port 4 -Port‐owned at North Embarcadero \$2.00,Port 5 -Port‐owned at Downtown \$3.00,Port 6 -Port‐owned at Downtown \$3.00,Port 7 -Port‐owned at Downtown \$3.00,Port 8 -Port‐owned at Downtown \$3.00,Port 9 -Port‐owned at South Embarcadero \$1.00,Port 10 -Port‐owned at South Embarcadero \$1.00,Port 11 -Port‐owned at South Embarcadero \$1.00,Port 12 -Port‐owned at South Embarcadero \$1.00,PortMC1 -Port‐owned motorcycle rate \$0.25,PortMC2 -Port‐owned motorcycle rate at Ferry Building \$0.50,Tour Bus - \$9.00 for two hours | Categorical |
| STREET_ID | Street identifier | Number |
| STREET_NAME | Street name | Text |
| STREET_NUM | Approximate street number of meter | Number |
| LONGITUDE | Longitude of meter | Number |
| LATITUDE | Latitude of meter| Number |
| COLLECTION_ROUTE_DESC || Categorical |
| COLLECTION_ROUTE_SUBROUTE_DESC || Categorical |
| Neighborhoods || Number|
| Analysis Neighborhoods || Number |

We can use __BLOCKFACE_ID__ to define the parking blocks, but the problem might be the block contains too few meters.
