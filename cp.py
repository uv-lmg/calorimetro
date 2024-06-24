import matplotlib.pyplot as plt

time = []
temperature = []

# Remember that Q is equal to the TOTAL energy consumed, in Joules.
#print("Q (in Joules) = ")
#Q = input()

#print("Mass (in grams) = ")
#mass = input()

#print("Degrees of change = ")
#chosen_change = input()

# Test values
Q = 2160000
mass = 15
chosen_change= 1

with open("output.txt", "r") as file:
    for line in file:
        t, temp = line.split()
        time.append(float(t))
        temperature.append(float(temp))

reference_value = temperature[0]

critical_times = []
critical_temps = []

for i, temp in enumerate(temperature):
    if temp == reference_value - chosen_change:
        critical_times.append(time[i])
        critical_temps.append(temp)
        reference_value = temp

    else:
        target_value = reference_value - chosen_change
        closest_value = min(temperature, key=lambda x: abs(x - target_value))
        if closest_value == temp: #and closest_value != critical_temps[-1]:
            critical_times.append(time[i])
            critical_temps.append(temp)
            reference_value = temp

temp_sum = critical_temps[0] - critical_temps[-1]
deltaTime = []

for j, taken in enumerate(critical_times):
    deltaTime.append(critical_times[j] - critical_times[j-1]) if j != 0 else deltaTime.append(critical_times[j])
    
specific_heat = Q/(mass*temp_sum)

print("Total change in temperature: " + str(temp_sum))
print("Total specific heat: " + str(specific_heat) + " J/(kg*K)")

plt.plot(critical_temps, deltaTime, marker='o', linestyle='-')
plt.xlabel('Temperature (Celsius)')
plt.ylabel("Seconds per " + str(chosen_change) + " degrees of change")
plt.title('Time against temperature change')
plt.grid(True)
plt.show()
