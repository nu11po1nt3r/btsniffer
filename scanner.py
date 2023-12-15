import simplepyble

    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.scan_for(5000) # scan for 5 seconds
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    
    peripherals = adapter.scan_get_results() #get peripherals
    
    for i, peripheral in enumerate(peripherals):
        print(f" id: {peripheral.identifier()} address: {peripheral.address()}")
      
    #Query the user to pick a peripheral
    choice = input("enter peripheral id: ")
    peripheral = peripherals[int(choice)]
    print("\n")    
    print(f"{peripheral.identifier()} details:")
    print(f"address: {peripheral.address()}")
    print(f"address type: {peripheral.address_type()}")
    print(f"rssi: {peripheral.rssi()}")
    print(f"transmit power: {peripheral.tx_power()}")
    print(f"mtu: {peripheral.mtu()}")
    print(f"connected: {peripheral.is_connected()}")
    print(f"connectable: {peripheral.is_connectable()}")
    print(f"paired: {peripheral.is_paired()}")
    services = peripheral.services()
    service_characteristic_pair = []
    service_count = 0
    for service in services: #insert into service(s) array
        for characteristic in service.characteristics():
            service_characteristic_pair.append((service.uuid(), characteristic.uuid()))
            #print(f"service id: {service_characteristic_pair[i]}")
            print(f"characteristic: {characteristic[i][1]}")
        service_count= service_count + 1
            
    print(f"{service_count} service(s) found")     
        
    print("disconnecting...")
    peripheral.disconnect()