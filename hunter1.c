#include<stdio.h>
long int c[10000];
int main()
{
    long int arr[10000],N,i;
    int f=0;
    scanf("%ld",&N);
    for(i=0;i<N;i++)
    {
        scanf("%ld",&arr[i]);
        c[arr[i]]++;
     }
     for(i=0;i<N;i++)
     {
          if(c[i]>1)
          {
          f=1;
          printf("%ld",i);
          }
      }
      if(f!=1)
      printf("unique");
      return 0;
 }
