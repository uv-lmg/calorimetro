import matplotlib.pyplot as plt

time = []
temperature = []

#print("Q (in Joules) = ")
#Q = input()
Q = 30

#print("Mass (in kg) = ")
#mass = input()
mass = 1

#print("Degrees of change: ")
#chosen_one = input()
chosen_one = 1

with open("output.txt", "r") as file:
    for line in file:
        t, temp = line.split()
        time.append(float(t))
        temperature.append(float(temp))

reference_value = temperature[0]

critical_times = []
critical_temps = []

for i, temp in enumerate(temperature):
    if temp == reference_value - chosen_one:
        critical_times.append(time[i])
        critical_temps.append(temp)
        reference_value = temp

    else:
        target_value = reference_value - chosen_one
        closest_value = min(temperature, key=lambda x: abs(x - target_value))
        if closest_value == temp:
            critical_times.append(time[i])
            critical_temps.append(temp)
            reference_value = temp

temp_sum = critical_temps[0] - critical_temps[-1]
        
# temporary prints
print(critical_temps)
print(critical_times)
print(temp_sum)

specific_heat = Q/(mass*temp_sum)
print("Total specific heat: " + str(specific_heat) + " J/(kg*K)")

plt.plot(critical_temps, critical_times, marker='o', linestyle='-')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Seconds per degrees of change')
plt.title('Time against temperature change')
plt.grid(True)
plt.show()
