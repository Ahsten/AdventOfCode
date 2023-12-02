def part1():
    with open("inputs/day1.txt") as f:
        calibration_sum = 0
        for line in f:
            nums = []
            for char in line:
                if char.isnumeric():
                    nums.append(char)
            
            firstNum = nums[0]
            lastNum = nums.pop()
            cal_value = int(str(firstNum) + str(lastNum))    
            calibration_sum += cal_value
        
    print(calibration_sum)

word_digits = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

def part2():
    with open("inputs/day1.txt") as f:
        calibration_sum = 0
        for line in f:
            for key in word_digits:
                if line.find(key) != -1:
                    line = line.replace(key, word_digits[key])

                
            print(line)
            nums = []
            for char in line:
                if char.isnumeric():
                    nums.append(char)
            
            firstNum = nums[0]
            lastNum = nums.pop()
            cal_value = int(str(firstNum) + str(lastNum))    
            calibration_sum += cal_value
        
    print(calibration_sum)

part1()
part2()
