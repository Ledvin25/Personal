package data;
import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONTokener;

import java.io.FileReader;

public class JSONLoader {

    public JSONObject Load() {
        try {
            // Cargar el archivo JSON
            FileReader reader = new FileReader("src\\data\\default.json");
            JSONTokener tokener = new JSONTokener(reader);
            JSONObject json = new JSONObject(tokener);
            reader.close();
            return json;
        } catch (Exception e) {
            e.printStackTrace();
            return null; 
        }

        
    }

    // Metodo para obtener los nombres de las empresas de buses y devolver una lista de strings
    public String[] getEnterprise()
    {
        JSONObject json = Load();
        JSONArray empresasDeBuses = json.getJSONArray("empresas_de_buses");
        String[] enterprises = new String[empresasDeBuses.length()];
        for (int i = 0; i < empresasDeBuses.length(); i++) {
            JSONObject empresa = empresasDeBuses.getJSONObject(i);
            String nombreEmpresa = empresa.getString("nombre");
            enterprises[i] = nombreEmpresa;
        }
        return enterprises;
    }

    // Metodo para obtener los buses de la empresa seleccionada

    public String[] getBuses(String empresa)
    {
        JSONObject json = Load();

        // Obtener las empresas de buses
        JSONArray empresasDeBuses = json.getJSONArray("empresas_de_buses");

        // Recorrer las empresas de buses
        for (int i = 0; i < empresasDeBuses.length(); i++) 
        {
            JSONObject empresaDeBus = empresasDeBuses.getJSONObject(i);

            String nombreEmpresa = empresaDeBus.getString("nombre");

            if (nombreEmpresa.equals(empresa)) 
            {
                JSONArray buses = empresaDeBus.getJSONArray("buses");
                
                String[] busesString = new String[buses.length()];
                
                for (int j = 0; j < buses.length(); j++) 
                {
                    JSONObject bus = buses.getJSONObject(j);
                    String placa = bus.getString("placa");
                    int capacidad = bus.getInt("capacidad");
                    busesString[j] = placa + " - " + capacidad;
                }

                return busesString;
            }
        }
        return null;
    }

    // Metodo para obtener las rutas de la empresa seleccionada

    public String[] getRutas(String empresa)
    {
        JSONObject json = Load();

        // Obtener las empresas de buses
        JSONArray empresasDeBuses = json.getJSONArray("empresas_de_buses");

        // Recorrer las empresas de buses
        for (int i = 0; i < empresasDeBuses.length(); i++) 
        {
            JSONObject empresaDeBus = empresasDeBuses.getJSONObject(i);

            String nombreEmpresa = empresaDeBus.getString("nombre");

            if (nombreEmpresa.equals(empresa)) 
            {
                JSONArray rutas = empresaDeBus.getJSONArray("rutas");
                
                String[] rutasString = new String[rutas.length()];
                
                for (int j = 0; j < rutas.length(); j++) 
                {
                    JSONObject ruta = rutas.getJSONObject(j);
                    String nombreRuta = ruta.getString("nombre");
                    rutasString[j] = nombreRuta;
                }

                return rutasString;
            }
        }
        return null;
    }

    // Metodo para obtener el id de la ruta seleccionada

    public int getRutaId(String empresa, String ruta)
    {
        JSONObject json = Load();

        // Obtener las empresas de buses
        JSONArray empresasDeBuses = json.getJSONArray("empresas_de_buses");

        // Recorrer las empresas de buses
        for (int i = 0; i < empresasDeBuses.length(); i++) 
        {
            JSONObject empresaDeBus = empresasDeBuses.getJSONObject(i);

            String nombreEmpresa = empresaDeBus.getString("nombre");

            if (nombreEmpresa.equals(empresa)) 
            {
                JSONArray rutas = empresaDeBus.getJSONArray("rutas");
                
                for (int j = 0; j < rutas.length(); j++) 
                {
                    JSONObject rutaDeBus = rutas.getJSONObject(j);
                    String nombreRuta = rutaDeBus.getString("nombre");
                    if (nombreRuta.equals(ruta)) 
                    {
                        int id = rutaDeBus.getInt("id");
                        return id;
                    }
                }
            }
        }
        return 0;
    }

    // Metodo para obtener la tarifa de la ruta seleccionada

    public int getTarifa(String empresa, String ruta)
    {
        JSONObject json = Load();

        // Obtener las empresas de buses
        JSONArray empresasDeBuses = json.getJSONArray("empresas_de_buses");

        // Recorrer las empresas de buses
        for (int i = 0; i < empresasDeBuses.length(); i++) 
        {
            JSONObject empresaDeBus = empresasDeBuses.getJSONObject(i);

            String nombreEmpresa = empresaDeBus.getString("nombre");

            if (nombreEmpresa.equals(empresa)) 
            {
                JSONArray rutas = empresaDeBus.getJSONArray("rutas");
                
                for (int j = 0; j < rutas.length(); j++) 
                {
                    JSONObject rutaDeBus = rutas.getJSONObject(j);
                    String nombreRuta = rutaDeBus.getString("nombre");
                    if (nombreRuta.equals(ruta)) 
                    {
                        int tarifa = rutaDeBus.getInt("tarifa");
                        return tarifa;
                    }
                }
            }
        }
        return 0;
    }

    // Metodo para obtener las paradas de la ruta seleccionada

    public String[] getParadas(String empresa, String ruta)
    {
        JSONObject json = Load();

        // Obtener las empresas de buses
        JSONArray empresasDeBuses = json.getJSONArray("empresas_de_buses");

        // Recorrer las empresas de buses
        for (int i = 0; i < empresasDeBuses.length(); i++) 
        {
            JSONObject empresaDeBus = empresasDeBuses.getJSONObject(i);

            String nombreEmpresa = empresaDeBus.getString("nombre");

            if (nombreEmpresa.equals(empresa)) 
            {
                JSONArray rutas = empresaDeBus.getJSONArray("rutas");
                
                for (int j = 0; j < rutas.length(); j++) 
                {
                    JSONObject rutaDeBus = rutas.getJSONObject(j);
                    String nombreRuta = rutaDeBus.getString("nombre");
                    if (nombreRuta.equals(ruta)) 
                    {
                        JSONArray paradas = rutaDeBus.getJSONArray("paradas");
                        String[] paradasString = new String[paradas.length()];
                        for (int k = 0; k < paradas.length(); k++) 
                        {
                            JSONObject parada = paradas.getJSONObject(k);
                            String nombreParada = parada.getString("nombre");
                            int posicion = parada.getInt("posicion");
                            boolean terminal = parada.getBoolean("terminal");

                            paradasString[k] = nombreParada + " - " + posicion + " - " + terminal;
                        }
                        return paradasString;
                    }
                }
            }
        }
        return null;
    }
}