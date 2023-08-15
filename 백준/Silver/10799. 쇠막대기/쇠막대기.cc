#include <stdio.h>
#include <stack>

std::stack <int> s;

int main(int argc, const char * argv[]) {
    char arr[100000] = {0};
    scanf("%s", arr);
    
    int cnt = 0;
    
    for(int i=0;arr[i]!='\0';i++){
        if (arr[i] == '('){
            s.push('(');
            if (arr[i+1] == ')'){
                s.pop();
                cnt += s.size();
                i++;
            }
        } else if (arr[i] == ')'){
            cnt++;
            s.pop();
        }
    }
    printf("%d", cnt);
    return 0;
}