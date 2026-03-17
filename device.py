import pyvisa
rm = pyvisa.ResourceManager('@py')
print("Connected devices:", rm.list_resources())
