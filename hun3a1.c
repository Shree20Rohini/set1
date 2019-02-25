//shree
#include<stdio.h>
void main()
{
int i,j,k,l,n,m;
scanf("%d %d",&m,&n);
int a[m][n],b[m][n];
for(i=0;i<m;i++)
for(j=0;j<n;j++){
scanf("%d",&a[i][j]);
b[i][j]=a[i][j];}
for(i=0;i<m;i++)
{
	for(j=0;j<n;j++)
	{
		if(b[i][j]==0)
		{
			for(k=i,l=0;l<m;l++)
			a[k][l]=0;
			for(l=j,k=0;k<n;k++)
			a[k][l]=0;
		}
	}
	}
	for(i=0;i<m;i++)
	{
	for(j=0;j<n;j++)
	printf("\n%d",a[i][j]);
	printf("\n");
}
		
}
