package com.company;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //int[][] board = {
        //        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        //        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        //        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        //        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        //        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        //        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        //        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        //        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        //        {0, 0, 0, 0, 8, 0, 0, 7, 9},
        //};
        int[][] board = getBoard();
        if(solve(board)==true){
            System.out.println("Solved");
            printBoard(board);
        }else{
            System.out.println("Keine Lösung");
            printBoard(board);
        }
    }
    public static int[] getEmpty(int[][] board){
        int[] position = {10,10};
        for(int i = 0;i < board.length;i++){
            for(int j=0;j<board[i].length;j++){
                if(board[i][j]==0){
                    position[0] = i;
                    position[1] = j;
                    return position;
                }
            }
        }
        return position;
    }

    public static boolean checkValid(int i,int[][]board,int[]position){
        //horizontal
        for(int index=0;index<board[position[0]].length;index++){
            if(board[position[0]][index] == i){
                return false;
            }
        }
        //vertikal
        for(int index=0;index<board.length;index++){
            if(board[index][position[1]] == i){
                return false;
            }
        }
        //box
        int x = (position[1]/3)*3;
        int y = (position[0]/3)*3;
        for(int index=0;index<3;index++){
            for(int index2=0;index2<3;index2++){
                if(board[y+index][x+index2]==i){
                    return false;
                }
            }
        }
    return true;
    }
    public static void printBoard(int[][]board){
        for(int i=0;i<9;i++){
            System.out.println(Arrays.toString(board[i]));
        }
    }
    public static boolean solve(int[][] board){
        int[] position = getEmpty(board);
        if(position[0]==10){
            return true;
        }else{
            for (int i = 1; i <= 9; i++) {
                if (checkValid(i,board,position) == true) {
                    board[position[0]][position[1]] = i;
                    if(solve(board) == true){
                        return true;
                    }
                }
            }
        }
        board[position[0]][position[1]]=0;
        return false;
    }
    public static int[][] getBoard() {
            boolean kontrolle = false;
            int[][] board = new int[9][];
            while(kontrolle == false){
                int x=0;
                Scanner eingabe = new Scanner(System.in);
                for(int j=0;j<9;j++){
                    int[] line = new int[9];
                    int sum=0;
                    System.out.println("Geben Sie die " + (j+1) +". Zeile ein:");
                    String zeile = eingabe.nextLine();

                    for(int i=0; i<zeile.length();i++){
                        String item = String.valueOf(zeile.charAt(i));
                        if(!item.equals(" ")){
                            line[sum]=Integer.parseInt(item);
                            sum++;
                        }
                    }
                    board[x] = line;
                    x++;
                }
                for(int[] liste:board){
                    System.out.println(Arrays.toString(liste));
                }
                System.out.println("Is this the board you want to solve?[y/n]");
                String antwort = eingabe.nextLine();
                if(antwort.equals("y")){
                    kontrolle = true;
                }
            }

            return board;
        }
}
