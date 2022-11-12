

import java.util.Scanner;

public class IEEE_task2 {

    public static void main(String[] args) {


        Scanner input = new Scanner(System.in);
        System.out.println("Please enter a number:");
        int num = input.nextInt();

        System.out.println(fact(num));

    }
    static int fact(int num){
        if(num<0) {
            System.out.println("Please enter a positive number");
            return 0;
            }
        if(num<=0) return 1;
        return num*fact(num-1);
    }
        }

