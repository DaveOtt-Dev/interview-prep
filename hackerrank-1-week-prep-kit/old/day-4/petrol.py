def truckTour(petrolpumps):
    # Write your code here    
    for startIndex in range(len(petrolpumps)):
        truckPetrol = 0
        index = startIndex
        while True:
            pumpPetrol = petrolpumps[index][0]
            nextPumpDistance = petrolpumps[index][1]
            
            truckPetrol += pumpPetrol
            
            index += 1
            if index >= len(petrolpumps):
                index = 0
            if index == startIndex:
                if truckPetrol > 0:
                    return index
                break

            truckPetrol -= nextPumpDistance
            if truckPetrol < 0:
                break
    
    
if __name__ == '__main__':
    result = truckTour([[1,5], [10,3], [3,4]])
    print(result)