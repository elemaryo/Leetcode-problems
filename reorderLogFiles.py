class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterlogs = []
        digitlogs = []
        result = []
        for i in range(len(logs)):
            singleLog = logs[i].split()
            # check after what comes first space is a letter or a number
            # put letter logs in own array
            if singleLog[1].isnumeric():
                digitlogs.append(logs[i])
            else:
                letterlogs.append(logs[i])

        # sort by first identifier
        letterlogs.sort(key=lambda x: x.split()[0])
        # sort by second identifier and after elements if they are similar
        letterlogs.sort(key=lambda x: x.split()[1:])
        # concat letter logs with digit logs
        result = letterlogs+digitlogs
        return result

# time complexity: o(nlogn) because of sorting cause for each element you need to compare it with log n other numbers to find its current index
# space complexity o(n)

# split():Split a string into a list where each word is a list item
# strip():Remove spaces at the beginning and at the end of the string
#isdigit or isnumeric
# lambda is used to sort with key
# join(): Join all items in a tuple into a string, using a specified character as separator:
