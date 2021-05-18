class bubble{

    static void bubble_sort(int[] arr){
         int n= arr.length, temp;
         do{
             int flag=0;
             for(int i=1;i<n;i++){
                 if(arr[i]<arr[i-1]){
                     temp= arr[i];
                     arr[i]=arr[i-1];
                     arr[i-1]=temp;
                     flag=i;
                 }
             }
             n= flag;
         }while(n>0);
    }
    public static void main(String[] args) {
        int[] arr= {2,4,1};
        bubble_sort(arr);
        int n= arr.length;
        for(int i=0;i<n;i++)
        System.out.println(arr[i]);
    }
}