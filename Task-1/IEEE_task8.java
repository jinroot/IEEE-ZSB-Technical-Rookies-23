import java.util.LinkedList;

class IEEE_task8 {

    public static void main(String[] args) {

        LinkedList<String> linkedList = new LinkedList<>();

        linkedList.add("Toyota");
        linkedList.add("Maserati");
        linkedList.add("Ford");
        linkedList.add("BMW");
        linkedList.addFirst("Hyundai");

        for (int i = 0; i < linkedList.size(); i++) {

            System.out.println(linkedList.get(i));
        }
    }
}