
import java.util.Scanner;

public class IEEE_task7 {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("Please enter a number:");
        int num = input.nextInt();
        int revNum=0;
        while(num !=0) {
            int rightMostDigit = num % 10;
            revNum = revNum * 10 + rightMostDigit;
            num /= 10;
        }
        System.out.println(revNum);
    }
}