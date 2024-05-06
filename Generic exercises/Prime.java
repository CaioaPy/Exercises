//Write a Java program to figure out if the elementis prime or not.

import java.util.*;

public class Prime {
    public static void main(String[] args) {
        int x = 0;
        int num;
        Scanner leitor = new Scanner(System.in);
        System.out.println("Insert the number: ");
        num = leitor.nextInt();
        leitor.close();
        for (int n = 1; n <= num; n++) {
            if (num % n == 0) {
                x++;
            } else {
            }
        }
        if (x != 2) {
            System.out.println("Not prime!");
        } else if (x == 2) {
            System.out.println("Prime!");
        }
    }
}