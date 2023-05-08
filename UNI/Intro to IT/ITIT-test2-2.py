E = int(input("Joules (only \"x\" * 10 ^ 23): "))
power = int(input("Power (only 234 * 10 ^ \"x\"): "))
c = 299792458
mass = (E*(10**power)) / (c**2)
print("{} kg".format(round(mass,2)))