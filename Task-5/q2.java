import java.util.Scanner;
import java.util.Stack;
import java.util.Scanner;  

public class q2{
  public static boolean isValid(String s) {
    Stack<Integer> p = new Stack<>();
    for(int i = 0; i < s.length(); i++) {
        int q = "(){}[]".indexOf(s.substring(i, i + 1));
        if(q % 2 == 1) {
            if(p.isEmpty() || p.pop() != q - 1) return false;
        } else p.push(q);
    }
    return p.isEmpty();
  }

public static void main(String[] args) {
  
  Scanner input = new Scanner(System.in);
  String inp = input.nextLine();
  System.out.println(isValid(inp));

}
}