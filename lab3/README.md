# Занятие №3. Корреляция дискретных сигналов

## Задание
1. Напишите на языке C/C++ функцию вычисления корреляции и
нормализованной корреляции между массивами a, b и с

<img src = "photo/mass.png">

2. Выведите в терминале полученные значения в виде таблицы

## Реализация:

- Функция для Корелляции:
```c
int Correlations(int a[], int b[]){
    int correl = 0 ;

    for (int i=0; i < 8; i++){
        correl+= a[i]*b[i] ;   
    }
    return correl;
}
```

- Функция для Нормализованной корелляции:
```c
float Norm_Correlat(int a[], int b[]){
    int sum_a=0, sum_b = 0, cor_a_b=0;
    for (int i = 0; i < 8; i++ ){
        sum_a+=a[i]*a[i];
        sum_b+=b[i]*b[i];
    }
    cor_a_b = Correlations(a,b);
    float res =(cor_a_b/sqrt(sum_a*sum_b));
    return res;
}
```

<img src = "photo/correl.png">