# include <stdio.h>
int main(void ){
    int h, m;
    scanf("%d %d", &h, &m);
    if (m-45>=0) printf("%d %d", h, m-45);
    else if (h-1>=0 && m-45<0) printf("%d %d", h-1, m-45+60);
    else printf("%d %d", h-1+24, m-45+60);
    return 0;
}
