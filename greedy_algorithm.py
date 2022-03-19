import time

states_needed = set(['ms', 'spb', 'lo', 'murm', 'vor', 'st', 'kr'])
stations = {}
stations['kone'] = set(['ms', 'lo', 'murm', 'st', 'kr' ])
stations['kwo'] = set(['spb', 'lo', 'vor', 'st', 'kr'])
stations['khtree'] = set(['st', 'kr'])
stations['kfour'] = set(['ms', 'kr'])
stations['kfive'] = set(['spb', 'lo', 'murm', 'kr'])
final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print (final_stations)