#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void print_arrey(int arr[],int start, int size){
    for (int i=start; i < size; i++){
        printf("%d ", arr[i]);
    }   
    printf("\n"); 
}



int main () {
    srand(time(NULL));
    int c =0;
    int len_N = 35 , len_G = 8, len_N_0 = len_N+len_G-1;
    int N[len_N];
    int N_0[len_N_0];
    int N_tx[len_N_0];
    int G[] = {1,0,1,0,0,1,1,1};

    for (int i=0; i < len_N; i++){
        N[i] = rand() % 2;
        N_0[i] = N[i];
        N_tx[i] = N[i];
    }


    //add zero
    for (int i = len_N; i < len_N_0; i++){
        N_0[i] = 0;
    }
    
    for (int i = 0; i < len_N; i++){
        if (N_0[i] == 1){
            for (int j =0; j < len_G; j++ ){
                N_0[i+j] = N_0[i+j] ^ G[j];
            }
        }
    }

    for (int i = len_N; i < len_N_0; i++){
        N_tx[i] = N_0[i];
    }
    printf("Data: \t ");
    print_arrey(N,0,len_N);
    printf("CRC TX:  ");
    print_arrey(N_0,len_N,len_N_0);
    printf("Data TX: ");
    print_arrey(N_tx,0,len_N_0);
    
    
    for (int i = 0; i < len_N_0; i++){
        if (N_tx[i] == 1){
            for (int j =0; j < len_G; j++ ){
                N_tx[i+j] = N_tx[i+j] ^ G[j];
            }
        }
    }

    int flag = 0;
    printf("CRC RX:  ");
    print_arrey(N_tx, len_N, len_N_0);

    for (int i = len_N; i < len_N_0; i++){
        if (N_tx[i] == 1){
            printf("Error data!");
            flag = 0;
            break;
        }
        else
            flag = 1;
    }

    if (flag == 1){
        printf("Successful!");
    }

    for (int i = 0; i < len_N+len_G-1; i++ ){

    }
        


    //for (int i = 0; i < len_N+len_G-1; i++){

    //}





}