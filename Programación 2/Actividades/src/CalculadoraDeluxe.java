import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class CalculadoraDeluxe {

    private static List<String> resultados = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                mostrarMenuFiguras();
                int figura = scanner.nextInt();

                if (figura == 8) {
                    System.out.println("Saliendo...");
                    break;
                }

                if (figura == 7) {
                    mostrarResultados();
                    continue;
                }

                mostrarMenuOperaciones();
                int operacion = scanner.nextInt();

                realizarOperacion(scanner, figura, operacion);
            } catch (InputMismatchException e) {
                System.out.println("Error de entrada. Por favor, ingrese un numero valido.");
                scanner.next(); // Limpiar el buffer del scanner
            }
        }
    }

    private static void mostrarMenuFiguras() {
        System.out.println("Seleccione la figura geometrica:");
        System.out.println("1. Circulo");
        System.out.println("2. Cuadrado");
        System.out.println("3. Triangulo");
        System.out.println("4. Rectangulo");
        System.out.println("5. Pentagono");
        System.out.println("6. Potencia");
        System.out.println("7. Mostrar resultados");
        System.out.println("8. Salir");
        System.out.print("Opcion: ");
    }

    private static void mostrarMenuOperaciones() {
        System.out.println("Seleccione la operacion:");
        System.out.println("1. Area");
        System.out.println("2. Perimetro");
        System.out.println("3. Potencia");
        System.out.print("Opcion: ");
    }

    private static void realizarOperacion(Scanner scanner, int figura, int operacion) {
        switch (figura) {
            case 1:
                calcularCirculo(scanner, operacion);
                break;
            case 2:
                calcularCuadrado(scanner, operacion);
                break;
            case 3:
                calcularTriangulo(scanner, operacion);
                break;
            case 4:
                calcularRectangulo(scanner, operacion);
                break;
            case 5:
                calcularPentagono(scanner, operacion);
                break;
            case 6:
                calcularPotencia(scanner);
                break;
            default:
                System.out.println("Opcion no valida.");
        }
    }

    private static void calcularCirculo(Scanner scanner, int operacion) {
        try {
            System.out.print("Ingrese el radio del circulo: ");
            double radio = scanner.nextDouble();
            if (operacion == 1) {
                double area = Math.PI * Math.pow(radio, 2);
                resultados.add("Area del circulo: " + area);
                System.out.println("Area del circulo: " + area);
            } else if (operacion == 2) {
                double perimetro = 2 * Math.PI * radio;
                resultados.add("Perimetro del circulo: " + perimetro);
                System.out.println("Perimetro del circulo: " + perimetro);
            } else {
                System.out.println("Operacion no valida.");
            }
        } catch (InputMismatchException e) {
            System.out.println("Error de entrada. Por favor, ingrese un numero valido.");
            scanner.next(); // Limpiar el buffer del scanner
        }
    }

    private static void calcularCuadrado(Scanner scanner, int operacion) {
        try {
            System.out.print("Ingrese el lado del cuadrado: ");
            double lado = scanner.nextDouble();
            if (operacion == 1) {
                double area = Math.pow(lado, 2);
                resultados.add("Area del cuadrado: " + area);
                System.out.println("Area del cuadrado: " + area);
            } else if (operacion == 2) {
                double perimetro = 4 * lado;
                resultados.add("Perimetro del cuadrado: " + perimetro);
                System.out.println("Perimetro del cuadrado: " + perimetro);
            } else {
                System.out.println("Operacion no valida.");
            }
        } catch (InputMismatchException e) {
            System.out.println("Error de entrada. Por favor, ingrese un numero valido.");
            scanner.next(); // Limpiar el buffer del scanner
        }
    }

    private static void calcularTriangulo(Scanner scanner, int operacion) {
        try {
            System.out.print("Ingrese la base del triangulo: ");
            double base = scanner.nextDouble();
            System.out.print("Ingrese la altura del triangulo: ");
            double altura = scanner.nextDouble();
            if (operacion == 1) {
                double area = (base * altura) / 2;
                resultados.add("Area del triangulo: " + area);
                System.out.println("Area del triangulo: " + area);
            } else if (operacion == 2) {
                System.out.print("Ingrese el lado 1 del triangulo: ");
                double lado1 = scanner.nextDouble();
                System.out.print("Ingrese el lado 2 del triangulo: ");
                double lado2 = scanner.nextDouble();
                System.out.print("Ingrese el lado 3 del triangulo: ");
                double lado3 = scanner.nextDouble();
                double perimetro = lado1 + lado2 + lado3;
                resultados.add("Perimetro del triangulo: " + perimetro);
                System.out.println("Perimetro del triangulo: " + perimetro);
            } else {
                System.out.println("Operacion no valida.");
            }
        } catch (InputMismatchException e) {
            System.out.println("Error de entrada. Por favor, ingrese un numero valido.");
            scanner.next(); // Limpiar el buffer del scanner
        }
    }

    private static void calcularRectangulo(Scanner scanner, int operacion) {
        try {
            System.out.print("Ingrese la longitud del rectangulo: ");
            double longitud = scanner.nextDouble();
            System.out.print("Ingrese el ancho del rectangulo: ");
            double ancho = scanner.nextDouble();
            if (operacion == 1) {
                double area = longitud * ancho;
                resultados.add("Area del rectangulo: " + area);
                System.out.println("Area del rectangulo: " + area);
            } else if (operacion == 2) {
                double perimetro = 2 * (longitud + ancho);
                resultados.add("Perimetro del rectangulo: " + perimetro);
                System.out.println("Perimetro del rectangulo: " + perimetro);
            } else {
                System.out.println("Operacion no valida.");
            }
        } catch (InputMismatchException e) {
            System.out.println("Error de entrada. Por favor, ingrese un numero valido.");
            scanner.next(); // Limpiar el buffer del scanner
        }
    }

    private static void calcularPentagono(Scanner scanner, int operacion) {
        try {
            System.out.print("Ingrese el lado del pentagono: ");
            double lado = scanner.nextDouble();
            if (operacion == 1) {
                System.out.print("Ingrese el apotema del pentagono: ");
                double apotema = scanner.nextDouble();
                double area = (5 * lado * apotema) / 2;
                resultados.add("Area del pentagono: " + area);
                System.out.println("Area del pentagono: " + area);
            } else if (operacion == 2) {
                double perimetro = 5 * lado;
                resultados.add("Perimetro del pentagono: " + perimetro);
                System.out.println("Perimetro del pentagono: " + perimetro);
            } else {
                System.out.println("Operacion no valida.");
            }
        } catch (InputMismatchException e) {
            System.out.println("Error de entrada. Por favor, ingrese un numero valido.");
            scanner.next(); // Limpiar el buffer del scanner
        }
    }

    private static void calcularPotencia(Scanner scanner) {
        try {
            System.out.print("Ingrese la base: ");
            int base = scanner.nextInt();
            System.out.print("Ingrese el exponente: ");
            int exponente = scanner.nextInt();
            int resultado = calcularPotenciaRecursiva(base, exponente);
            resultados.add("Potencia: " + base + "^" + exponente + " = " + resultado);
            System.out.println("Potencia: " + base + "^" + exponente + " = " + resultado);
        } catch (InputMismatchException e) {
            System.out.println("Error de entrada. Por favor, ingrese un numero valido.");
            scanner.next(); // Limpiar el buffer del scanner
        }
    }

    private static int calcularPotenciaRecursiva(int base, int exponente) {
        if (exponente == 0) {
            return 1;
        } else {
            return base * calcularPotenciaRecursiva(base, exponente - 1);
        }
    }

    private static void mostrarResultados() {
        System.out.println("Resultados almacenados:");
        for (String resultado : resultados) {
            System.out.println(resultado);
        }
    }
}
