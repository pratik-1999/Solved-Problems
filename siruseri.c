#include<stdio.h>
int score_check(int[],int[],int[],int);

int main()
{
  int low[10],high[10],n,score[10];
  printf("Enter the no of singers:");
  scanf("%d\n", &n );
  for(int i = 0; i < n; i++)
  {
    printf("Enter the lower limit of singer %d: ", i+1);
    scanf("%d\n", &low[i] );

    printf("Enter the higher limit of singer %d: ", i+1);
    scanf("%d\n", &high[i] );
  }

  score_check(low, high, score, n);
  for(int i = 0; i < n; i++)
  {
    printf(score[i]);
  }
  return 0;
}

int score_check(int a[],int b[],int c[],int n)
{
  for(int i = 0; i < n ; i++)
  {
    for(int j = 0; j < n; j++)
    {
      if(a[i] < a[j])
      {
        c[i] += 2;
      }
      else if(a[i] == a[j])
      {
        if(b[i] > b[j])
        {
          c[i] += 2;
        }
      }
    }
    return 0;
  }

}
