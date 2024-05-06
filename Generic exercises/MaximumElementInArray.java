//Write a Java program to find the largest element in an array.

import java.util.*;

public class MaximumElementInArray {
	
    public static void main(String[] args) {
        int x;
        ArrayList<Integer> lista = new ArrayList<Integer>();
        lista.add(2708);
        lista.add(287);
        lista.add(5432);
        lista.add(5672);
        lista.add(122);
        lista.add(289);
        lista.add(273);
        lista.add(245);
        lista.add(268);
        lista.add(23);
        Collections.sort(lista);
        x = lista.get(lista.size() - 1);
        System.out.println(x);
    }
}
