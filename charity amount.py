
def charityAllocation(profits):
    CharityCompanyAmount = {"A": 0, "B": 0,"C": 0}

    for i in range(len(profits)):
        smallest = min(CharityCompanyAmount, key = lambda x: CharityCompanyAmount.get(x))
        CharityCompanyAmount[smallest]+=i
        print(str(CharityCompanyAmount) + "\n")

profits = [25, 8, 2, 35, 15, 120, 55, 42]

charityAllocation(profits)


"""     CharityCompanyKeys = ["A", "B", "C"]
        for j in range(len(CharityCompanyKeys)):
            if 
            
            CharityCompanyAmount[j] ==  CharityCompanyAmount[j+1] & j > j+1 &  :
                CharityCompanyAmount[j]+=i
                CharityArray.append(j)

                            else: """