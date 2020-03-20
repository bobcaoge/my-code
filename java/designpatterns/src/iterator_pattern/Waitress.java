package iterator_pattern;

public class Waitress {
    private Menu arrayListMenu;
    private Menu arrayMenu;
    public Waitress(Menu arrayListMenu, Menu arrayMenu){
        this.arrayListMenu = arrayListMenu;
        this.arrayMenu = arrayMenu;
    }
    public void printMenu(){
        printMenu(arrayListMenu.createIterator());
        System.out.println();
        printMenu(arrayMenu.createIterator());
    }
    private void printMenu(Iterator iterator){
        while (iterator.hasNext()){
            System.out.println(iterator.Next());
        }
    }
}
