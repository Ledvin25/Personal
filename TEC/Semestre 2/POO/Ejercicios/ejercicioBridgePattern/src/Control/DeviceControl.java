package Control;

import Device.DeviceBridge;

public abstract class DeviceControl {

    protected DeviceBridge deviceBridge;

    public DeviceControl() {}

    public abstract String getImageSize();

    public void setDeviceBridge(DeviceBridge deviceBridge) {
        this.deviceBridge = deviceBridge;
    }
    
    public abstract void reproducirSonido(int volumen);
}

