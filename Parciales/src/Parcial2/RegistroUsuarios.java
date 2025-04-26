import java.util.ArrayList;
import java.util.Scanner;

public class RegistroUsuarios {
    private ArrayList<Usuario> usuarios;

    public RegistroUsuarios() {
        usuarios = new ArrayList<>();
    }

    public void registrarUsuario(String nombre, String correoElectronico, String contrasena) {
        if (Validador.validarNombre(nombre) && Validador.validarCorreoElectronico(correoElectronico) && Validador.validarContrasena(contrasena)) {
            Usuario usuario = new Usuario(nombre, correoElectronico, contrasena);
            usuarios.add(usuario);
            System.out.println("Usuario registrado exitosamente.");
        } else {
            System.out.println("Error en la validación de los datos del usuario.");
        }
    }

    public void mostrarUsuarios() {
        for (Usuario usuario : usuarios) {
            System.out.println("Nombre: " + usuario.getNombre());
            System.out.println("Correo Electrónico: " + usuario.getCorreoElectronico());
            System.out.println("Contraseña: " + usuario.getContrasena());
            System.out.println("-------------------------");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        RegistroUsuarios registro = new RegistroUsuarios();

        while (true) {
            System.out.println("1. Registrar usuario");
            System.out.println("2. Mostrar usuarios");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir el salto de línea

            if (opcion == 1) {
                System.out.print("Ingrese nombre: ");
                String nombre = scanner.nextLine();
                System.out.print("Ingrese correo electrónico: ");
                String correo = scanner.nextLine();
                System.out.print("Ingrese contraseña: ");
                String contrasena = scanner.nextLine();
                registro.registrarUsuario(nombre, correo, contrasena);
            } else if (opcion == 2) {
                registro.mostrarUsuarios();
            } else if (opcion == 3) {
                break;
            } else {
                System.out.println("Opción no válida.");
            }
        }

        scanner.close();
    }
}
