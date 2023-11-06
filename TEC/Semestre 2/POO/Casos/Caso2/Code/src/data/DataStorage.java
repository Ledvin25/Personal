package data;

import java.io.*;
import java.util.List;

import model.BusLine;

public class DataStorage {

    // Bus
    public void save(List<BusLine> busLine, String fileName) {
        try (ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(fileName))) {
            outputStream.writeObject(busLine);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<BusLine> load(String fileName) {
        List<BusLine> busList = null;
        try (ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream(fileName))) {
            busList = (List<BusLine>) inputStream.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return busList;
    }
}