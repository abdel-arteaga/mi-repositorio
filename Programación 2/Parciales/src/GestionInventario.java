import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Producto {
    String nombre;
    int cantidadInicial;
    int cantidadVendida;

    Producto(String nombre, int cantidadInicial) {
        this.nombre = nombre;
        this.cantidadInicial = cantidadInicial;
        this.cantidadVendida = 0;
    }

    int calcularDisponibilidad() {
        return cantidadInicial - cantidadVendida;
    }

    boolean haySuficienteStock(int cantidad) {
        return calcularDisponibilidad() >= cantidad;
    }

    void vender(int cantidad) {
        if (haySuficienteStock(cantidad)) {
            cantidadVendida += cantidad;
        } else {
            System.out.println("No hay suficiente stock para la venta.");
        }
    }

    void duplicarInventario() {
        if (calcularDisponibilidad() == 0) {
            cantidadInicial *= 2;
            cantidadVendida = 0;
        }
    }

    void mostrarInformacion() {
        System.out.println("Producto: " + nombre);
        System.out.println("Cantidad Inicial: " + cantidadInicial);
        System.out.println("Cantidad Vendida: " + cantidadVendida);
        System.out.println("Disponibilidad: " + calcularDisponibilidad());
    }
}

public class GestionInventario {
    private static Map<String, Producto> inventario = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Ingresar producto");
            System.out.println("2. Vender producto");
            System.out.println("3. Duplicar inventario");
            System.out.println("4. Mostrar inventario");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir nueva línea

            switch (opcion) {
                case 1:
                    ingresarProducto(scanner);
                    break;
                case 2:
                    venderProducto(scanner);
                    break;
                case 3:
                    duplicarInventario(scanner);
                    break;
                case 4:
                    mostrarInventario();
                    break;
                case 5:
                    System.out.println("Saliendo...");
                    return;
                default:
                    System.out.println("Opción no válida.");
            }
        }
    }

    private static void ingresarProducto(Scanner scanner) {
        System.out.print("Nombre del producto: ");
        String nombre = scanner.nextLine();
        System.out.print("Cantidad inicial: ");
        int cantidadInicial = scanner.nextInt();
        scanner.nextLine(); // Consumir nueva línea
        inventario.put(nombre, new Producto(nombre, cantidadInicial));
    }

    private static void venderProducto(Scanner scanner) {
        System.out.print("Nombre del producto: ");
        String nombre = scanner.nextLine();
        System.out.print("Cantidad a vender: ");
        int cantidad = scanner.nextInt();
        scanner.nextLine(); // Consumir nueva línea
        Producto producto = inventario.get(nombre);
        if (producto != null) {
            producto.vender(cantidad);
        } else {
            System.out.println("Producto no encontrado.");
        }
    }

    private static void duplicarInventario(Scanner scanner) {
        System.out.print("Nombre del producto: ");
        String nombre = scanner.nextLine();
        Producto producto = inventario.get(nombre);
        if (producto != null) {
            producto.duplicarInventario();
        } else {
            System.out.println("Producto no encontrado.");
        }
    }

    private static void mostrarInventario() {
        for (Producto producto : inventario.values()) {
            producto.mostrarInformacion();
        }
    }
}
//End