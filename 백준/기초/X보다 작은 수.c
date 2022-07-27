# include <stdio.h>
int main(void){
    int N, X;
    scanf("%d %d", &N, &X);
    for (int i=1; i<=N; i++){
        int a;
        scanf("%d ", &a);
        if (X>a) printf("%d ", a);
    }
    return 0;
}
