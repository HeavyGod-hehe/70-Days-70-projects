from pathlib import Path


file_path = Path("logs") / "app.log"



tally = {}
status_tally = {}
route_tally = {}
total_requests = 0

with open(file_path, "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) != 6:
            print("skipping invalid log line",line.strip())
            continue
        log = parts[2]
        status_code = parts[5]
        route = parts[4]
        if route not in route_tally:
            route_tally[route] = 0
        route_tally[route]+=1
        if status_code not in status_tally:
            status_tally[status_code] = 0
        status_tally[status_code]+=1
        if log not in tally:
            tally[log] = 0
        tally[log]+=1
        total_requests+=1
    print(tally)
    print(status_tally)
    print(route_tally)
    most_requested_route = max(route_tally,key=route_tally.get)
    print("Most requested route:", most_requested_route)
    print("Request count:", route_tally[most_requested_route])
    print(total_requests)