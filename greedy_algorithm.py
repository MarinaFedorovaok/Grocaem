states_needed = set(['ms', 'spb', 'lo', 'murm', 'vor', 'st', 'kr'])
stations = {}
stations['kone'] = set(['ms', 'lo', 'murm', 'st', 'kr' ])
stations['kwo'] = set(['spb', 'lo', 'vor', 'st', 'kr'])
stations['khtree'] = set(['st', 'kr'])
stations['kfour'] = set(['ms', 'kr'])
stations['kfive'] = set(['spb', 'lo', 'murm', 'kr'])
final_stations = set()
best_station = None
states_covered = set()
while states_needed:
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            print(best_station)
            states_covered = covered
            print(states_covered)
        states_needed -= states_covered
        print(states_needed)
        final_stations.add(best_station)
        print(final_stations)
print (final_stations)

