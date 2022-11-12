import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class IEEE_task3 {

    public static void main(String[] args) {

        List<Integer> list = new ArrayList<Integer>();

        Scanner input = new Scanner(System.in);
        System.out.println("Please enter the number of elements in the list:");
        int num = input.nextInt();
        System.out.println("Please enter the first element");
        for(int i = 0; i < num; i++){
            list.add(input.nextInt());
            if (i < num-1) {
                System.out.println("Please enter the next element");
            }else break;
        }

        System.out.println(forLoop(list));
        System.out.println(whileLoop(list));
        System.out.println(recursion(list));
    }
    static int forLoop(List<Integer> list){
        int sum = 0;
        for(int number : list){
            sum+=number;
        }
        return sum;
    }

    static int whileLoop(List<Integer> list){
        int sum = 0;
        int i = 0;
        while(i < list.size()){
            sum+=list.get(i);
            i++;
        }
        return sum;
    }

    static int recursion(List<Integer> list,int index){
        if(index <= 0) return 0;
        return recursion( list, index - 1) + list.get(index-1);
    }

    //constructor to call it in a more natural way
    static int recursion(List<Integer> list){
        int index = list.size();
        return recursion(list,index);
    }

}
