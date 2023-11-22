#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#define N 5

void print_arrey(int a[],int n ){
    for(int i=0; i < n; i++)
    {

        printf("%d ", a[i]);
    }
    printf("\n");
}

int cycle_x(int x[]){
    int temp = x[2] ^ x[3];
    
    for (int i=N-1; i>0; i--)
    {
        x[i] = x[i-1];

    }
    int last_bit = x[N-1];
    x[0] = temp;
    return last_bit;
}

int cycle_y(int y[]){
    int temp = y[1] ^ y[2];
    
    for (int i=N-1; i>0; i--)
    {
        y[i] = y[i-1];

    }
    int last_bit = y[N-1];
    y[0] = temp;

    return last_bit;
}

int cycle_shift_psevdo(int psevdo[], int size){
    int temp = psevdo[size-1];
    for (int i = size - 1; i > 0; i--)
    {
        psevdo[i] = psevdo[i-1];
    }
    psevdo[0] = temp;

}

void print_preambula(int n){
    //printf("| Shift ");
    for(int i = 0; i < n; i++){
        printf("| b%2d ",i);

    }
    printf("| Autocorrelate|\n");

}
void print_shift_psevdo(int a[], int n){
    
    for(int i = 0; i < n; i++){
        printf("|  %d  ",a[i]);

    }
    
}

int autocorrelate(int orig[], int new[], int size){
    int yes = 0, no = 0;
    for(int i = 0; i < size; i++){
        if ( orig[i] == new[i] ){
            yes += 1;
        }
        else
            no += 1;
    }
    return (yes - no);
}

int Correlations(int a[], int b[], int size){
    int correl = 0 ;

    for (int i=0; i < size; i++){
        correl+= a[i]*b[i] ;   
    }
    return correl;
}

int main(){
  
    int x[] = {0,1,1,1,1};
    int y[] = {1,0,1,1,0};
    int x1[] = {1,0,0,0,0};
    int y1[] = {1,0,0,0,1};
    int size = 31;
    int last_x[size], last_y[size];
    int psevdo[size], orig_psevdo[size], new_psevdo[size];
    int up_auto = 0;
    //print_arrey(x,n);
    last_x[0]=x[0];
    last_y[0]=y[0];
    for(int i=1; i < size; i++){
        last_x[i] = cycle_x(x);
        last_y[i] = cycle_y(y);   
    }


    for(int i=0; i < size; i++){
        psevdo[i] = last_x[i] ^ last_y[i]; 
  
    }
    last_x[0]=x[0];
    last_y[0]=y[0];
    for(int i=1; i < size; i++){
        last_x[i] = cycle_x(x1);
        last_y[i] = cycle_y(y1);   
    }

    for(int i=0; i < size; i++){
        new_psevdo[i] = last_x[i] ^ last_y[i]; 
  
    }

    for(int i=0; i < size; i++){
        orig_psevdo[i] = psevdo[i]; 
  
    }

    print_preambula(size);
    print_shift_psevdo(psevdo,size);
    up_auto = autocorrelate(orig_psevdo,psevdo,size);
    printf("| %2d/%2d        |\n", up_auto, size);

    for(int i=0; i < size; i++){
        cycle_shift_psevdo(psevdo,size);
        print_shift_psevdo(psevdo,size);
        up_auto = autocorrelate(orig_psevdo,psevdo,size);
        printf("| %2d/%2d        |\n", up_auto, size);
    }
    printf("Исходная последовательность: ");
    print_arrey(orig_psevdo,size);
   
    printf("Новая последовательность:    ");
    print_arrey(new_psevdo,size);
    int correl = Correlations(new_psevdo,orig_psevdo,size);
    printf("Значение взаимной корреляции исходной и новой последовательностей : %d", correl);
}

