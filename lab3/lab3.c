#include <stdio.h>



int Correlations(int a[], int b[]){
    int correl = 0 ;

    for (int i=0; i < 8; i++){
        correl+= a[i]*b[i] ;   
    }
    
    return correl;
}



int main(){

    int a[] =  {4, 2, 8, -2, -4, -4, 1, 3};  //15 var
    int b[]=   {2, 4, 7, 0, -3, -4, 2, 5};
    int c[]=   {-5, -1, 3, -4, 2, -6, 4, -1};
    
    int corr_a_b = Correlations(a,b);
    int corr_a_c = Correlations(a,c);
    int corr_b_c = Correlations(b,c);
    printf("\n%d", corr_a_b);
    printf("\n%d", corr_a_c);
    printf("\n%d", corr_b_c);
}