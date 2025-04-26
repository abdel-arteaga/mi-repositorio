import java.util.Scanner;

public class CalculadoraGeometrica {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Seleccione la figura geometrica:");
            System.out.println("1. Circulo");
            System.out.println("2. Cuadrado");
            System.out.println("3. Triangulo");
            System.out.println("4. Rectangulo");
            System.out.println("5. Pentagono");
            System.out.println("6. Salir");
            System.out.print("Opcion: ");
            int figura = scanner.nextInt();

            if (figura == 6) {
                System.out.println("Saliendo...");
                break;
            }

            System.out.println("Seleccione la operacion:");
            System.out.println("1. Area");
            System.out.println("2. Perimetro");
            System.out.print("Opcion: ");
            int operacion = scanner.nextInt();

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
                default:
                    System.out.println("Opcion no valida.");
            }
        }
    }

    private static void calcularCirculo(Scanner scanner, int operacion) {
        System.out.print("Ingrese el radio del circulo: ");
        double radio = scanner.nextDouble();
        if (operacion == 1) {
            double area = Math.PI * Math.pow(radio, 2);
            System.out.println("Area del circulo: " + area);
        } else if (operacion == 2) {
            double perimetro = 2 * Math.PI * radio;
            System.out.println("Perimetro del circulo: " + perimetro);
        } else {
            System.out.println("Operacion no valida.");
        }
    }

    private static void calcularCuadrado(Scanner scanner, int operacion) {
        System.out.print("Ingrese el lado del cuadrado: ");
        double lado = scanner.nextDouble();
        if (operacion == 1) {
            double area = Math.pow(lado, 2);
            System.out.println("Area del cuadrado: " + area);
        } else if (operacion == 2) {
            double perimetro = 4 * lado;
            System.out.println("Perimetro del cuadrado: " + perimetro);
        } else {
            System.out.println("Operacion no valida.");
        }
    }

    private static void calcularTriangulo(Scanner scanner, int operacion) {
        System.out.print("Ingrese la base del triangulo: ");
        double base = scanner.nextDouble();
        System.out.print("Ingrese la altura del triangulo: ");
        double altura = scanner.nextDouble();
        if (operacion == 1) {
            double area = (base * altura) / 2;
            System.out.println("Area del triangulo: " + area);
        } else if (operacion == 2) {
            System.out.print("Ingrese el lado 1 del triangulo: ");
            double lado1 = scanner.nextDouble();
            System.out.print("Ingrese el lado 2 del triangulo: ");
            double lado2 = scanner.nextDouble();
            System.out.print("Ingrese el lado 3 del triangulo: ");
            double lado3 = scanner.nextDouble();
            double perimetro = lado1 + lado2 + lado3;
            System.out.println("Perimetro del triangulo: " + perimetro);
        } else {
            System.out.println("Operacion no valida.");
        }
    }

    private static void calcularRectangulo(Scanner scanner, int operacion) {
        System.out.print("Ingrese la longitud del rectangulo: ");
        double longitud = scanner.nextDouble();
        System.out.print("Ingrese el ancho del rectangulo: ");
        double ancho = scanner.nextDouble();
        if (operacion == 1) {
            double area = longitud * ancho;
            System.out.println("Area del rectangulo: " + area);
        } else if (operacion == 2) {
            double perimetro = 2 * (longitud + ancho);
            System.out.println("Perimetro del rectangulo: " + perimetro);
        } else {
            System.out.println("Operacion no valida.");
        }
    }

    private static void calcularPentagono(Scanner scanner, int operacion) {
        System.out.print("Ingrese el lado del pentagono: ");
        double lado = scanner.nextDouble();
        if (operacion == 1) {
            System.out.print("Ingrese el apotema del pentagono: ");
            double apotema = scanner.nextDouble();
            double area = (5 * lado * apotema) / 2;
            System.out.println("Area del pentagono: " + area);
        } else if (operacion == 2) {
            double perimetro = 5 * lado;
            System.out.println("Perimetro del pentagono: " + perimetro);
        } else {
            System.out.println("Operacion no valida.");
        }
    }
}
