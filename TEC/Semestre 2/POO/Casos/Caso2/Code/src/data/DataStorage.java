package data;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

public class DataStorage {
    private ObjectMapper objectMapper = new ObjectMapper();
    private String dataFileName = "data.json";

    public void save(Data data) {
        try {
            objectMapper.writeValue(new File(dataFileName), data);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Data load() {
        try {
            File file = new File(dataFileName);
            if (file.exists()) {
                return objectMapper.readValue(file, Data.class);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}