import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ConsecutivePasswordValidator implements Runnable {
    private String password;

    public ConsecutivePasswordValidator(String password) {
        this.password = password;
    }

    @Override
    public void run() {
        boolean isValid = isValidPassword(password);
        String result = "La contraseña '" + password + "' es " + (isValid ? "válida." : "no válida.");
        System.out.println(result);
        logResult(result);
    }

    private boolean isValidPassword(String password) {
        if (password.length() < 8) {
            return false;
        }

        Pattern specialCharPattern = Pattern.compile("[^a-zA-Z0-9]");
        Matcher specialCharMatcher = specialCharPattern.matcher(password);
        if (!specialCharMatcher.find()) {
            return false;
        }

        Pattern upperCasePattern = Pattern.compile("[A-Z]");
        Matcher upperCaseMatcher = upperCasePattern.matcher(password);
        long upperCaseCount = upperCaseMatcher.results().count();
        if (upperCaseCount < 2) {
            return false;
        }

        Pattern lowerCasePattern = Pattern.compile("[a-z]");
        Matcher lowerCaseMatcher = lowerCasePattern.matcher(password);
        long lowerCaseCount = lowerCaseMatcher.results().count();
        if (lowerCaseCount < 3) {
            return false;
        }

        Pattern numberPattern = Pattern.compile("[0-9]");
        Matcher numberMatcher = numberPattern.matcher(password);
        if (!numberMatcher.find()) {
            return false;
        }

        return true;
    }

    private void logResult(String result) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("password_validation_log.txt", true))) {
            writer.write(result);
            writer.newLine();
        } catch (IOException e) {
            System.err.println("Error al escribir en el archivo de registro: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String[] passwords = {"Password123!", "Passw0rd!", "P@ssw0rd", "Pa$$w0rd123"};

        ExecutorService executor = Executors.newFixedThreadPool(passwords.length);
        for (String password : passwords) {
            executor.submit(new ConsecutivePasswordValidator(password));
        }
        executor.shutdown();
    }
}
