#include<stdio.h>

int main(int arg , char**args){
    #ifndef ONLINE_JUDGE
        freopen(args[1],"r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    int a,b;
    scanf("%d %d",&a,&b);
    printf("%d",a-b);
}