package Aeroport;

import java.util.ArrayList;

public class Pista {
    private String id; // Lo utilizamos para identificar a cada pista
    private int capacidadMaxima; // Numero max de aviones
    private Permiso permiso; // Para gestionar los permisos
    private ArrayList<String> listaEspera; // Lista de espera para los aviones
    private int avionesEnPista; // Numero de aviones en pista

    public Pista(String id, int capacidadMaxima, Permiso permiso) {
        this.id = id;
        this.capacidadMaxima = capacidadMaxima;
        this.permiso = permiso;
        this.listaEspera = new ArrayList<>();
        this.avionesEnPista = 0;
    }

    public synchronized void usarPista(String avion, boolean esAterrizaje) {
        try {
            // Solicita los permisos
            if (esAterrizaje) {
                permiso.solicitarPermisoAterrizaje();
            } else {
                permiso.solicitarPermisoDespegue();
            }

            // Si la pista se llena, el avión espera en la lista
            while (avionesEnPista >= capacidadMaxima) {
                System.out.println("Pista " + id + " llena. Avión " + avion + " en lista de espera.");
                listaEspera.add(avion);
                wait();
            }

            // El avión entra a la pista
            avionesEnPista++;
            System.out.println("Avión " + avion + " usando pista " + id + ". Tipo: " + (esAterrizaje ? "Aterrizaje" : "Despegue"));
            Thread.sleep(2000); // Simula la acción (2 segundos)

            // Sale de la pista
            System.out.println("Avión " + avion + " terminó de usar pista " + id + ".");
            avionesEnPista--;

            // Liberamos el permiso para poder continuar realizando acciones
            permiso.liberaPista();

            // Si hay aviones en espera, los añadimos a la pista que quede libre
            if (!listaEspera.isEmpty()) {
                listaEspera.remove(0); // Elimina el primer avión en espera
                notifyAll();
            }
            //aqui manejamos la excepcion
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("Hilo interrumpido durante el uso de la pista.");
        }
    }


    //getters
    public String getId() {
        return id;
    }

    public int getCapacidadMaxima() {
        return capacidadMaxima;
    }

    public synchronized int getAvionesEnPista() {
        return avionesEnPista;
    }
}
