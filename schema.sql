CREATE TABLE IF NOT EXISTS agency (
    agency_id TEXT PRIMARY KEY,
    agency_name TEXT,
    agency_url TEXT,
    agency_timezone TEXT,
    agency_lang TEXT,
    agency_phone TEXT
);

CREATE TABLE IF NOT EXISTS calendar_dates (
    service_id TEXT,
    date TEXT,
    exception_type INTEGER
);

CREATE TABLE IF NOT EXISTS calendar (
    service_id TEXT PRIMARY KEY,
    monday INTEGER,
    tuesday INTEGER,
    wednesday INTEGER,
    thursday INTEGER,
    friday INTEGER,
    saturday INTEGER,
    sunday INTEGER,
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE IF NOT EXISTS routes (
    route_id TEXT PRIMARY KEY,
    agency_id TEXT,
    route_short_name TEXT,
    route_long_name TEXT,
    route_desc TEXT,
    route_type TEXT,
    route_colour TEXT,
    route_text_colour TEXT,
    FOREIGN KEY (agency_id) REFERENCES agency(agency_id)
);

CREATE TABLE IF NOT EXISTS shapes (
    shape_id TEXT PRIMARY KEY,
    shape_pt_lat TEXT,
    shape_pt_lon TEXT,
    shape_pt_sequence TEXT,
    shape_dist_traveled TEXT
);

CREATE TABLE IF NOT EXISTS stop_times (
    trip_id TEXT,
    arrival_time TEXT,
    departure_time TEXT,
    stop_id TEXT,
    stop_sequence INTEGER,
    stop_headsign TEXT,
    pickup_type INTEGER,
    drop_off_type INTEGER,
    shape_distance_traveled TEXT,
    timepoint INTEGER,
    stop_note_id TEXT,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id),
    FOREIGN KEY (stop_id) REFERENCES stops(stop_id),
    FOREIGN KEY (stop_note_id) REFERENCES notes(note_id)
);

CREATE TABLE IF NOT EXISTS stops (
    stop_id TEXT PRIMARY KEY,
    stop_name TEXT,
    stop_lat TEXT,
    stop_lon TEXT,
    location_type INTEGER,
    parent_station TEXT,
    wheelchair_boarding INTEGER,
    platform_code TEXT
);

CREATE TABLE IF NOT EXISTS trips (
    route_id TEXT,
    service_id TEXT,
    trip_id TEXT PRIMARY KEY,
    trip_headsign TEXT,
    direction_id INTEGER,
    block_id TEXT,
    shape_id TEXT,
    wheelchair_accessible INTEGER,
    trip_note_id TEXT,
    route_direction TEXT,
    FOREIGN KEY (route_id) REFERENCES routes(route_id),
    FOREIGN KEY (service_id) REFERENCES calendar(service_id),
    FOREIGN KEY (trip_note_id) REFERENCES notes(note_id)
);
 
CREATE TABLE IF NOT EXISTS notes (
    note_id TEXT,
    note_text TEXT
);



