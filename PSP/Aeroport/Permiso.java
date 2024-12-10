package Aeroport;
/*programa para la gestion de aeropuerto:


- Aviones; despegar o aterrizar / tiempo que dura la acción
	*Permiso para desp o aterri

- Pistas; Capacidades (distintas entre distintas pistas)
	* puede 1 o mas dependiendo
	*exclusivas de aterri o excl de desp
	*Permiso

guardar pistas en arrays
aviones aterrizan o despegan en la primera pista dispo que haya
para ello vemos la capacidad (ocupado/libre)


(Cola de pistas para que vayan entrando de forma aleatoria aviones)
Clase Permiso (tipo)

lock
unlock
.await
.signal
.signal */

public class Permiso {
    private boolean pistaLibre = true;
    private boolean soloAterrizaje;
    private boolean soloDespegue;

    public Permiso(boolean soloAterrizaje, boolean soloDespegue) {
        this.soloAterrizaje = soloAterrizaje;
        this.soloDespegue = soloDespegue;
    }

    public synchronized void solicitarPermisoAterrizaje() {
        while (!pistaLibre || soloDespegue) {
            try {
                wait(); 
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); 
                System.out.println("Hilo interrumpido, solicitando permiso para aterrizar...");
                return; 
            }
        }
        pistaLibre = false; 
    }

    public synchronized void solicitarPermisoDespegue() {
        while (!pistaLibre || soloAterrizaje) {
            try {
                wait(); 
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); 
                System.out.println("Hilo interrumpido, solicitando permiso para despegar.");
                return; 
            }
        }
        pistaLibre = false; 
    }

    public synchronized void liberaPista() {
        pistaLibre = true;
        notifyAll();
    }

    public boolean esSoloDespegue() {
        return soloDespegue;
    }

    public boolean esSoloAterrizaje() {
        return soloAterrizaje;
    }

    public void cambioEntreTipo(boolean soloAterrizaje, boolean soloDespegue) {
        this.soloAterrizaje = soloAterrizaje;
        this.soloDespegue = soloDespegue;
        notifyAll();
    }

    public void pistaMixta(boolean soloAterrizaje, boolean soloDespegue) {
        this.soloAterrizaje = false;
        this.soloDespegue = false;
        notifyAll();
    }
}

