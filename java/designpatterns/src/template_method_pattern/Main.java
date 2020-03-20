package template_method_pattern;

import java.util.Arrays;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int num = 7;
        Duck[] ducks = new Duck[7];
        for (int i = 0; i < num; i++) {
            ducks[i] = new Duck("duck"+i, new Random().nextInt(1000));
        }
        for (int j = 0; j < num; j++) {
            System.out.println(ducks[j].toString());
        }
        System.out.println();
        Arrays.sort(ducks);

        for (int j = 0; j < num; j++) {
            System.out.println(ducks[j].toString());
        }

    }
}
