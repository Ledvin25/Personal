package Control;

import Device.DeviceBridge;

public class GoogleHome extends DeviceControl{
    
    public void setDeviceBridge(DeviceBridge deviceBridge) {
        this.deviceBridge = deviceBridge;
    }

    @Override
    public String getImageSize() {
        return deviceBridge.getRelacionAspecto();
    }

    @Override
    public void reproducirSonido(int volumen) {
        deviceBridge.reproducirSonido(volumen);; // Utiliza el puente para realizar la acción en el dispositivo de la casa
    }
}
