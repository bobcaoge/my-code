package iterator_pattern;
public class Main {
    public static void main(String[] args) {
        Menu arrayListMenu = new ArrayListMenu();
        Menu arrayMenu = new ArrayMenu();
        Waitress waitress = new Waitress(arrayListMenu, arrayMenu);
        waitress.printMenu();
    }
}
