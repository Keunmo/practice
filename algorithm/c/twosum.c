#include <stdio.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i, j;
    for(i=0;i<=numsSize;i++){
        for(j=i+1;j<=numsSize;j++){
            if(nums[i]+nums[j]==target){
                return i, j;
            }
        }
    }
}

int main(void){
    twoSum();
}
