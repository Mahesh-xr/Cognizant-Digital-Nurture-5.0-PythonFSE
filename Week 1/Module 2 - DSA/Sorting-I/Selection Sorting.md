Reference : https://takeuforward.org/sorting/selection-sort-algorithm/

```java
import java.util.*;

public class tUf {
    static void selection_sort(int arr[], int n) {
        for (int i = 0; i < n - 1; i++) {
            int mini = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[mini]) {
                    mini = j;
                }
            }
            //swap
            int temp = arr[mini];
            arr[mini] = arr[i];
            arr[i] = temp;
        }

        System.out.println("After selection sort:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {

        int arr[] = {13, 46, 24, 52, 20, 9};
        int n = arr.length;
        System.out.println("Before selection sort:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        selection_sort(arr, n);
    }
}
```



**Approach:**

The algorithm steps are as follows:

1. First, we will select the range of the unsorted array using a loop (say i) that indicates the starting index of the range.  
    The loop will run forward from 0 to n-1. The value i = 0 means the range is from 0 to n-1, and similarly, i = 1 means the range is from 1 to n-1, and so on.  
    (_Initially, the range will be the whole array starting from the first index._)
    
2. Now, in each iteration, we will select the minimum element from the range of the unsorted array using an inner loop.
3. 
4. After that, we will swap the minimum element with the first element of the selected range(_in step 1_). 
5. Finally, after each iteration, we will find that the array is sorted up to the first index of the range. 

**Note:** _Here, after each iteration, the array becomes sorted up to the first index of the range. That is why the starting index of the range increases by 1 after each iteration. This increment is achieved by the outer loop and the starting index is represented by variable_ **_i_** _in the following code. And the inner loop(_**_i.e. j_**_) helps to find the minimum element of the range_ **[i…..n-1].**