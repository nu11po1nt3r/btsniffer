import simplepyble
import time

def dump():
    adapters = simplepyble.Adapter.get_adapters() 
    adapter = adapters[0]
    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.scan_for(10000) # scan for 10 seconds
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    peripherals = adapter.scan_get_results() #get peripherals
    
    for i, peripheral in enumerate(peripherals):
        print(f"[{i}] \t{peripheral.address()} {peripheral.identifier()} ")
    
    #Query the user to pick a peripheral    
    choice = input("Enter peripheral id: ")   
    peripheral = peripherals[int(choice)]  

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
                
def scan():
    
    adapters = simplepyble.Adapter.get_adapters() 
    adapter = adapters[0]
    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.scan_for(10000) # scan for 10 seconds
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    peripherals = adapter.scan_get_results() #get peripherals
    
    for i, peripheral in enumerate(peripherals):
        print(f"[{i}] \t{peripheral.address()} {peripheral.identifier()} ")
    
def menu():
    print("\n")
    print("[1] scan [2] dump [3] quit")
    choice = input("")
    return choice

# ---------- MAIN PROGRAM ---------------------------
if __name__ == "__main__":
    adapters = simplepyble.Adapter.get_adapters() 
    adapter = adapters[0]
    print("\n")
    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.scan_for(10000) # scan for 10 seconds
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    peripherals = adapter.scan_get_results() #get peripherals
    
    print(f"Selected adapter: {adapter.identifier()} {adapter.address()}")


    #get peripherals, dump, and ask questions
    choice = menu()

    # meat and potatoes of the menu **shrugs** I tried...
    while(choice != 5):
        if int(choice) == 1:
            scan()
        elif int(choice) == 2:
            dump()
        elif int(choice) == 3:
            print(f"Goodbye")
            exit()
        elif int(choice) == 4:
            choice = menu()
        elif int(choice) <= 1 or int(choice) > 3:
            choice = menu()
        
        choice = menu()
       
    
    

                
    
        


    
    
    

