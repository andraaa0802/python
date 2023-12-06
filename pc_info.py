import psutil

cpu_percent=psutil.cpu_percent(interval= 1, percpu=True)
cpu_freq=psutil.cpu_freq(percpu=True)

print ("CPU usgae per core: ")
for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
    print(f"Core {i}: {percent}%  Frequency: {freq.current} MHz")

virtual_mem=psutil.virtual_memory()
swap=psutil.swap_memory()

print("\nVirtual memory: ")
print(f"Total: {virtual_mem.total / (1024 ** 3):.2f} GB")
print(f"Used: {virtual_mem.used / (1024 ** 3):.2f} GB")
print(f"Swap total: {swap.total / (1024 ** 3):.2f} GB")
print(f"Swap used: {swap.used / (1024 ** 3):.2f} GB")

network=psutil.net_io_counters()
print("\nNetwork information: ")
print(f"Bytes received: {network.bytes_recv}")
print(f"Bytes sent: {network.bytes_sent}")

try:
    temperatures=psutil.sensors_temperatures()
    if temperatures:
        print("\nTemperatures: ")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}")
    else:
        print("\nTemperature information unavailable.")
except AttributeError:
    print("\nTemperature informations unavailable.")

battery=psutil.sensors_battery()
if battery:
    plugged="Plugged in" if battery.power_plugged else "Not plugged in"
    print(f"\nBattery status: {plugged}, {battery.percent}%")
else:
    print(f"Battery information unavailable.")

disk=psutil.disk_usage('/')
print("\nDisk information:")
print(f"Total disk space: {disk.total/(1024 ** 3):.2f} GB")
print(f"Used disk space: {disk.used/(1024 ** 3):.2f} GB")
print(f"Free disk space: {disk.free/(1024 ** 3):.2f} GB")