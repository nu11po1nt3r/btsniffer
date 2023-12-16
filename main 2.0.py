import simplepyble
import time

def start(choice):
    #Query the user to pick a peripheral        
    peripheral = peripherals[choice]  

    try: 
        peripheral.connect()
    except TypeError:
        print(f"couldn't connect {peripheral}")
    except RuntimeError:
        print(f"couldn't connect to {peripheral}")
    else:
        print(f"connecting to {peripheral}") 

    print("\n")    
    print(f"{peripheral.identifier()} details:")
    print(f"address: {peripheral.address()}")
    print(f"address type: {peripheral.address_type()}")
    print(f"rssi: {peripheral.rssi()}")
    print(f"transmit power: {peripheral.tx_power()}")
    print(f"mtu: {peripheral.mtu()}")
    print(f"connected: {peripheral.is_connected()}")
    print(f"connectable: {peripheral.is_connectable()}")
    print(f"manufacturer data: {peripheral.manufacturer_data()}")
    #error handling for not compatible methods
    try:
        peripheral.is_paired()
    except TypeError:
        print("pairing: N/A")
    except RuntimeError:
        print("pairing: N/A")
    else:
        print(f"paired: {peripheral.is_paired()}")

    #start service navigation
    services = peripheral.services()
    service_characteristic_pair = []
    print(" ")

    print(f"({len(services)}) service(s) found:") 
    for service in services: #insert into service(s) array
        for characteristic in service.characteristics():
            service_characteristic_pair.append((service.uuid(), characteristic.uuid()))

        print(f"service id: {service.uuid()}")
        print(f"({len(service.characteristics())}) characteristics found:")
    
        for characteristic in service.characteristics():
            print(f"\tuuid: {characteristic.uuid()}\t")
            #checks if the characteristic is readable
            try: 
                peripheral.read(service.uuid(), characteristic.uuid())
            except TypeError:
                print("\t unreadable")
            except RuntimeError:
                print("\t unreadable")
            else:
                print(f"\tdata: {peripheral.read(service.uuid(), characteristic.uuid())}")
                
            print(f"\t({len(characteristic.descriptors())}) descriptor(s) found: ")
            for descriptor in characteristic.descriptors():
                print(f"\t\tdescriptors: {descriptor.uuid()}")
                try:
                    peripheral.descriptor_read(service.uuid(), characteristic.uuid(), descriptor.uuid())
                except TypeError:
                    print("\t\tunreadable")
                except RuntimeError:
                    print("\t\tunreadable")
                    
                else:
                    print(f"\t\tdata: {peripheral.descriptor_read(service.uuid(), characteristic.uuid(), descriptor.uuid())}")
        print("")   
        

def dumpHeaders(choice):
    peripheral = peripherals[choice] 
    print("\n")    
    print(f"{peripheral.identifier()} details:")
    print(f"address: {peripheral.address()}")
    print(f"address type: {peripheral.address_type()}")
    print(f"rssi: {peripheral.rssi()}")
    print(f"transmit power: {peripheral.tx_power()}")
    print(f"mtu: {peripheral.mtu()}")
    print(f"connected: {peripheral.is_connected()}")
    print(f"connectable: {peripheral.is_connectable()}")
    print(f"manufacturer data: {peripheral.manufacturer_data()}")
    #error handling for not compatible methods
    try:
        peripheral.is_paired()
    except TypeError:
        print("pairing: N/A")
    except RuntimeError:
        print("pairing: N/A")
    else:
        print(f"paired: {peripheral.is_paired()}")

    #start service navigation
    services = peripheral.services()
    service_characteristic_pair = []
    print(" ")

    print(f"({len(services)}) service(s) found:") 
    for service in services: #insert into service(s) array
        for characteristic in service.characteristics():
            service_characteristic_pair.append((service.uuid(), characteristic.uuid()))

        print(f"service id: {service.uuid()}")
        print(f"({len(service.characteristics())}) characteristics found:")
    
        for characteristic in service.characteristics():
            print(f"\tuuid: {characteristic.uuid()}\t")
            #checks if the characteristic is readable
            try: 
                peripheral.read(service.uuid(), characteristic.uuid())
            except TypeError:
                print("\t unreadable")
            except RuntimeError:
                print("\t unreadable")
            else:
                print(f"\tdata: {peripheral.read(service.uuid(), characteristic.uuid())}")
                
            print(f"\t({len(characteristic.descriptors())}) descriptor(s) found: ")
            for descriptor in characteristic.descriptors():
                print(f"\t\tdescriptors: {descriptor.uuid()}")
                try:
                    peripheral.descriptor_read(service.uuid(), characteristic.uuid(), descriptor.uuid())
                except TypeError:
                    print("\t\tunreadable")
                except RuntimeError:
                    print("\t\tunreadable")
                    
                else:
                    print(f"\t\tdata: {peripheral.descriptor_read(service.uuid(), characteristic.uuid(), descriptor.uuid())}")
        print("")   
        

if __name__ == "__main__":
    adapters = simplepyble.Adapter.get_adapters() 
  
    if len(adapters) == 0:
        print("No adapters found")
    
    for i, adapter in enumerate(adapters):
        print(f"adapter id: {adapter.identifier()}")
        print(f"adapter address: {adapter.address()}")
        print(f"adapter initialized: {adapter.initialized()}\n")
        print(f"connected peripherals: {len(adapter.get_paired_peripherals())}")

    print(f"{i+1} adapter(s) found.\n") 
    
    adapter = adapters[0]
    
    
    print(f"Selected adapter: {adapter.identifier()} {adapter.address()}")
    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.scan_for(10000) # scan for 5 seconds
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    peripherals = adapter.scan_get_results() #get peripherals
    
    for i, peripheral in enumerate(peripherals):
        print(f"{i} id: {peripheral.identifier()} address: {peripheral.address()}")
    
    
    choice = int(input("Enter periperal id: "))
    start(choice)
    while(choice !='q' or choice !='Q'):
        time.sleep(3)
        dumpHeaders(choice)

print(f"disconnecting from {peripheral.identifier()}")
peripheral.disconnect()
print("disconnected")

                
    
        


    
    
    

