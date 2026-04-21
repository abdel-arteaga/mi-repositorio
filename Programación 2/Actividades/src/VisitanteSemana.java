import java.util.Scanner;

public class VisitanteSemana {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Información del visitante
        System.out.print("Ingrese la edad del visitante: ");
        byte edad = scanner.nextByte();
        System.out.print("Ingrese el número de departamento que visita: ");
        short numeroDepartamento = scanner.nextShort();
        System.out.print("Ingrese el número de teléfono del visitante: ");
        int numeroTelefono = scanner.nextInt();
        System.out.print("Ingrese la identificación del visitante: ");
        long identificacion = scanner.nextLong();
        System.out.print("Ingrese la altura del visitante en metros: ");
        float altura = scanner.nextFloat();
        System.out.print("Ingrese el peso del visitante en kilogramos: ");
        double peso = scanner.nextDouble();
        System.out.print("Ingrese el género del visitante (M/F): ");
        char genero = scanner.next().charAt(0);
        System.out.print("¿Es residente del edificio? (true/false): ");
        boolean esResidente = scanner.nextBoolean();

        // Información de las visitas
        int totalVisitas = 0;
        double tiempoTotalEstadia = 0;

        for (int i = 0; i < 7; i++) {
            System.out.print("Ingrese el tiempo de estadía en horas para la visita " + (i + 1) + ": ");
            double tiempoEstadia = scanner.nextDouble();
            tiempoTotalEstadia += tiempoEstadia;
            totalVisitas++;
        }

        // Cálculos finales
        double tiempoPromedioEstadia = tiempoTotalEstadia / totalVisitas;
        String mayorOMenorEdad = (edad >= 18) ? "mayor de edad" : "menor de edad";

        // Impresión de los resultados
        System.out.println("\nInformación del Visitante:");
        System.out.println("Edad: " + edad);
        System.out.println("Número de Departamento: " + numeroDepartamento);
        System.out.println("Número de Teléfono: " + numeroTelefono);
        System.out.println("Identificación: " + identificacion);
        System.out.println("Altura: " + altura + " metros");
        System.out.println("Peso: " + peso + " kilogramos");
        System.out.println("Género: " + genero);
        System.out.println("Es Residente: " + esResidente);
        System.out.println("\nInformación de las Visitas:");
        System.out.println("Cantidad Total de Visitas: " + totalVisitas);
        System.out.println("Tiempo Promedio de Estadia: " + tiempoPromedioEstadia + " horas");
        System.out.println("El visitante es " + mayorOMenorEdad);
    }
}
