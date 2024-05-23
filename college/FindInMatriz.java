// Leia uma matriz 20 x 20. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final escrever a localização (linha e coluna) ou uma mensagem de “não encontrado”.

import java.util.*;

public class Main {
    public static int[][] createMatriz(int linhas, int colunas) {
        int[][] arraynome = new int[linhas][colunas];
        return arraynome;
    }
    
    public static void DefineValues(int[][] array, int linhas, int colunas) {
        Random rando = new Random();
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                int randd = rando.nextInt(1000);
                array[i][j] = randd;
            }
        }
    }
    
    public static void PrintArray(int[][] array, int linhas, int colunas) {
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                System.out.print(array[i][j] + " ");
            } System.out.print("\n");
        } 
    }
    public static boolean SearchForX(int[][] array, int linhas, int colunas, int constante, boolean found) {
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                if (array[i][j] == constante) {
                    found = true;
                    break;
                }
                else {
                    continue;
                }
            }
        }
        return found;
    }
    
    
	public static void main(String[] args) {
        Random rand = new Random();
        int L = 20, C = 20;
        int constante = rand.nextInt(1000);
        int[][] matriz = createMatriz(L, C);
        boolean found = false;
        System.out.println("Matriz criada aleatóriamente: \n");
        DefineValues(matriz, L, C);
        PrintArray(matriz, L, C);
        System.out.println("Valor selecionado aleatóriamente: " + constante);
        System.out.println("Verificando se '" + constante + "' existe na matriz...");
        found = SearchForX(matriz, L, C, constante, found);
        if (found) {
            System.out.println(constante + " existe na matriz!");
        }
        else {
            System.out.println(constante + " não existe na matriz!");
        }
    }
}
