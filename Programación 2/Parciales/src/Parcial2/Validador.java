import java.util.regex.Pattern;

public class Validador {
    private static final String NOMBRE_REGEX = "^[a-zA-Z\\s]+$";
    private static final String CORREO_REGEX = "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$";
    private static final String CONTRASENA_REGEX = "^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{8,}$";

    public static boolean validarNombre(String nombre) {
        return Pattern.matches(NOMBRE_REGEX, nombre);
    }

    public static boolean validarCorreoElectronico(String correo) {
        return Pattern.matches(CORREO_REGEX, correo);
    }

    public static boolean validarContrasena(String contrasena) {
        return Pattern.matches(CONTRASENA_REGEX, contrasena);
    }
}
