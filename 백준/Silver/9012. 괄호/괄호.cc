#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    int n;
    char arr[50];
    int *result;
    scanf("%d", &n);
    result = (int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++){
        scanf("%s", arr);
        int tmp = 0;
        for(int j=0;j<strlen(arr);j++){
            if(arr[j]=='('){
                tmp++;
            }
            else if(arr[j]==')'){
                tmp--;
                if (tmp<0){
                    result[i] = 0;
                    break;
                }
            }
        }
        if (tmp==0)
            result[i] = 1;
        else
            result[i] = 0;
    }
    
    for(int i=0;i<n;i++){
        if(result[i]==0)
            printf("NO");
        else if(result[i]==1)
            printf("YES");
        puts("");
    }
    return 0;
}