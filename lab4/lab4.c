#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#define N 5

void print_arrey(int a[],int n ){
    for(int i=0; i < n; i++){

        printf("%d ", a[i]);
    }
    printf("\n");
}

int cucle_x(int x[]){
    int temp = x[2] ^ x[3];
    
    for (int i=N-1; i>0; i--){
        x[i] = x[i-1];

    }
    int last_bit = x[N-1];
    x[0] = temp;
    return last_bit;
}

int cucle_y(int y[]){
    int temp = y[1] ^ y[2];
    
    for (int i=N-1; i>0; i--){
        y[i] = y[i-1];

    }
    int last_bit = y[N-1];
    y[0] = temp;

    return last_bit;
}

int main(){
  
    int x[] = {0,1,1,1,1};
    int y[] = {1,0,1,1,0};
    int size = 31;
    int last_x[size], last_y[size];
    int psevdo[size];
    //print_arrey(x,n);
    last_x[0]=x[0];
    last_y[0]=y[0];
    for(int i=1; i < size; i++){
        last_x[i] = cucle_x(x);
        last_y[i] = cucle_y(y);
        //psevdo[i] = last_x ^ last_y; 
        //print_arrey(x,n);
        
    }


    for(int i=0; i < size; i++){
        psevdo[i] = last_x[i] ^ last_y[i]; 
        
    }
    
    
    print_arrey(psevdo,size);
}

