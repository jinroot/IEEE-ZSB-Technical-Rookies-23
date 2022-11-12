import java.util.Scanner;

public class IEEE_task4 {

    public static void main(String[] args){


        Scanner input = new Scanner(System.in);
        System.out.println("Please enter a number:");
        int num = input.nextInt();
        int sum = 0;
        for(int i = 1; i <= num; i++){
            sum+= i;
        }
        System.out.println("The sum of elements from 1 to your number is: "+sum);
    }
}
