# Write your code here
def get_time(passengers, flights):
    source = flights.copy()
    destination = []
    time = 0
    if flights[0]<passengers[0]:
        return -1

    while len(passengers) > 0:
        if source:
            passenger_index=0
            for flight in source:
                passenger_index = int(search_passenger(passengers, flight))
                if passenger_index == -1:                        
                    break
                else:
                    passengers.pop(passenger_index)
                    destination.append(source.pop(0))
            time += 1
            
        else:
            time+=1
            source = destination.copy()
            destination = []
            passenger_index=0
            for flight in source:
                passenger_index = int(search_passenger(passengers, flight))
                if passenger_index == -1:                        
                    break
                else:
                    passengers.pop(passenger_index)
                    destination.append(source.pop(0))
            time += 1
    return time

        
def search_passenger(passengers, flight):
    for i in range(len(passengers)):
        if flight>=passengers[i]:
            return str(i)
        if i==len(passengers)-1:
            return -1

        
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    passengers = list(map(int, input().split()))
    flights = list(map(int, input().split()))
    flights.sort(reverse=True)
    passengers.sort(reverse=True)
    print(get_time(passengers, flights))