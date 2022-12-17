public class q1 {
    public static void main(String[] args){
        int list1[] = {1,2,4};
        int list2[] = {1,3,4};
        int list1Length = list1.length;
        int list2Length = list2.length;
        int[] arr = new int[list1Length+list2Length];
        int k =0,i=0,j=0;
        while (i < list1Length && j < list2Length) {
            if (list1[i] <= list2[j]) {
                arr[k] = list1[i];
                i++;
            }
            else {
                arr[k] = list2[j];
                j++;
            }
            k++;

        }
        while (i < list1Length) {
            arr[k] = list1[i];
            i++;
            k++;
        }
        while (j < list2Length) {
            arr[k] = list2[j];
            j++;
            k++;
        }
        for (int f = 0; f < arr.length; f++)
            System.out.print(arr[f] + " ");
        System.out.println();
    }

}
