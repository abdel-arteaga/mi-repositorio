import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class PasswordValidator implements Runnable {
    private String password;

    public PasswordValidator(String password) {
        this.password = password;
    }

    @Override
    public void run() {
        if (isValidPassword(password)) {
            System.out.println("La contraseña '" + password + "' es válida.");
        } else {
            System.out.println("La contraseña '" + password + "' no es válida.");
        }
    }

    private boolean isValidPassword(String password) {
        // Longitud mínima de 8 caracteres
        if (password.length() < 8) {
            return false;
        }

        // Presencia de caracteres especiales
        Pattern specialCharPattern = Pattern.compile("[^a-zA-Z0-9]");
        Matcher specialCharMatcher = specialCharPattern.matcher(password);
        if (!specialCharMatcher.find()) {
            return false;
        }

        // Uso de al menos dos letras mayúsculas
        Pattern upperCasePattern = Pattern.compile("[A-Z]");
        Matcher upperCaseMatcher = upperCasePattern.matcher(password);
        int upperCaseCount = 0;
        while (upperCaseMatcher.find()) {
            upperCaseCount++;
        }
        if (upperCaseCount < 2) {
            return false;
        }

        // Uso de al menos tres letras minúsculas
        Pattern lowerCasePattern = Pattern.compile("[a-z]");
        Matcher lowerCaseMatcher = lowerCasePattern.matcher(password);
        int lowerCaseCount = 0;
        while (lowerCaseMatcher.find()) {
            lowerCaseCount++;
        }
        if (lowerCaseCount < 3) {
            return false;
        }

        // Uso de al menos un número
        Pattern numberPattern = Pattern.compile("[0-9]");
        Matcher numberMatcher = numberPattern.matcher(password);
        if (!numberMatcher.find()) {
            return false;
        }

        return true;
    }

    public static void main(String[] args) {
        String[] passwords = {"Password123!", "Passw0rd!", "P@ssw0rd", "Pa$$w0rd123"};

        for (String password : passwords) {
            Thread thread = new Thread(new PasswordValidator(password));
            thread.start();
        }
    }
}
