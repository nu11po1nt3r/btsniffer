import simplepyble

if __name__ == "__main__":
    adapters = simplepyble.Adapter.get_adapters() 
  
    if len(adapters) == 0:
        print("No adapters found")


    def printAdapters():
    #Query the user to pick an adapter
         for i, adapter in enumerate(adapters):
            print(f"adapter id: {adapter.identifier()}")
            print(f"adapter address: {adapter.address()}")
            print(f"adapter initialized: {adapter.initialized()}\n")
            print(f"connected peripherals: {len(adapter.get_paired_peripherals())}")
        
            print(f"{i+1} adapter(s) found.\n") 
            
    adapter = adapters[0]
    
    #call adapter function
    printAdapters()
    print("[1] scan")
    print("[2] adapter info")
    print("[0] exit ")
    parameter = int(input(" "))
    
    match parameter:

        case 0:
            print("goodbye")
            exit()

        case 1:
            print(f"Selected adapter: {adapter.identifier()} {adapter.address()}")
            adapter.set_callback_on_scan_start(lambda: print("Scan started."))
            adapter.scan_for(10000) # scan for 5 seconds
            adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
            peripherals = adapter.scan_get_results() #get peripherals
    
            for i, peripheral in enumerate(peripherals):
                print(f"{i} id: {peripheral.identifier()} address: {peripheral.address()}")

            #Query the user to pick a peripheral
            choice = int(input("peripheral id: "))
    
            
            peripheral = peripherals[choice]  
            peripheral.connect()
            print("\n")    
            print(f"{peripheral.identifier()} details:")
            print(f"address: {peripheral.address()}")
            print(f"address type: {peripheral.address_type()}")
            print(f"rssi: {peripheral.rssi()}")
            print(f"transmit power: {peripheral.tx_power()}")
            print(f"mtu: {peripheral.mtu()}")
            print(f"connected: {peripheral.is_connected()}")
            print(f"connectable: {peripheral.is_connectable()}")
            print(f"manufacturer data: {bytes(peripheral.manufacturer_data())}")
                    
            services = peripheral.services()
            service_characteristic_pair = []
            print(" ")
        
            print(f"({len(services)}) service(s) found:") 
            for service in services: #insert into service(s) array
                for characteristic in service.characteristics():
                    service_characteristic_pair.append((service.uuid(), characteristic.uuid()))
     
                print(f"service id: {service.uuid()}")
                print(f"({len(service.characteristics())}) characteristics found:")
            #print(f"characteristics: {(service.characteristics())}")
                for characteristic in service.characteristics():
                    print(f"\tuuid: {characteristic.uuid()}\t")
                    print(f"\tdata: {bytes(peripheral.read(service.uuid(), characteristic.uuid()))}")
                    print(f"\t({len(characteristic.descriptors())}) descriptor(s) found: ")
               
                    for descriptor in characteristic.descriptors():
                        print(f"\t\tdescriptors: {descriptor.uuid()}")
                        print(f"\t\tdata: {bytes(peripheral.descriptor_read(service.uuid(), characteristic.uuid(), descriptor.uuid()))}")
                        print("")
                print("")    
            print(f"disconnecting from {peripheral.identifier()}")
            peripheral.disconnect()
            print("disconnected")
            
            print("[1] scan")
            print("[2] adapter info")
            print("[0] exit ")
            parameter = int(input(" "))
    
        case 2: 
            printAdapters()
            print("[1] scan")
            print("[2] adapter info")
            print("[0] exit ")
            parameter = int(input(" "))


       
    
    


