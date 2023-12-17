import simplepyble
from collections.abc import Iterable


def notify(byte: Iterable[bytes]) -> None:
    return byte

def sendPayload():

    serviceID = '00001523-1212-efde-1523-785feabcd111'
    descriptorID = '00002902-0000-1000-8000-00805f9b34fb'
    characteristicID = '00001524-1212-efde-1523-785feabcd111'
    payLoad = bytes('\x0f\x0f', 'utf-8')

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
    
    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.scan_for(10000) # scan for 5 seconds
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    peripherals = adapter.scan_get_results() #get peripherals
    
    for i, peripheral in enumerate(peripherals):
        print(f"[{i}] \t{peripheral.address()} {peripheral.identifier()}")
    
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
    print(f"manufacturer data: {peripheral.manufacturer_data()}")

    descriptor_count = 0        
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
                descriptor_count = descriptor_count + 1
                print(f"\t\tdescriptors: {descriptor.uuid()}")
                print(f"\t\tdata: {bytes(peripheral.descriptor_read(service.uuid(), characteristic.uuid(), descriptor.uuid()))}")
                print("")
        print("")    
    
     
    if descriptor_count == 0:
        print("no descriptors found")
        print("disconnecting")
        peripheral.disconnect()
        print("disconnected")
        exit()
    else:
        #write to the uuid and send payload
        print(f"SENDING {payLoad} to {descriptorID}")
        peripheral.descriptor_write(serviceID, characteristicID, descriptorID, bytes(payLoad))
        
        print("PAYLOAD SENT") 
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
    print("Goodbye")

            
            
sendPayload()



       
    
    


