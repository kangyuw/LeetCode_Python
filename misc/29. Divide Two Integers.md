### [29\. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

Difficulty: **Medium**  

Related Topics: [Math](https://leetcode.com/tag/math/), [Binary Search](https://leetcode.com/tag/binary-search/)


Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing `dividend` by `divisor`.

The integer division should truncate toward zero, which means losing its fractional part. For example, `truncate(8.345) = 8` and `truncate(-2.7335) = -2`.

**Note:**

*   Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2<sup>31</sup>,  2<sup>31</sup> − 1]. For this problem, assume that your function **returns 2<sup>31</sup> − 1 when the division result overflows**.

**Example 1:**

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
```

**Example 2:**

```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
```

**Example 3:**

```
Input: dividend = 0, divisor = 1
Output: 0
```

**Example 4:**

```
Input: dividend = 1, divisor = 1
Output: 1
```

**Constraints:**

*   `-2<sup>31</sup> <= dividend, divisor <= 2<sup>31</sup> - 1`
*   `divisor != 0`

### Alternatives

* a = -a
* a >> 1 代替 a / 2
* ㄇ<< 1 代替 a * 2

## Solution 1: 連續減

Time: O(n) 太慢了

```
class Solution {
public:
    int divide(int dividend, int divisor) {
        int subtractions = 0;
        while(dividend - divisor >= 0){
            subtractions++;
            dividend -= divisor;
        }
        return subtractions;
    }
};
```

但如果有任一個數字是負數, 這招就行不通了

也要避免使用 ```abs```, 容易造成 overflow

```
class Solution {
public:
    int divide(int dividend, int divisor) {
        int negatives = 0;
        if (dividend<0){
            negatives++;
            dividend = -dividend;
        }
        
        if (divisor<0){
            negatives++;
            divisor = -divisor;
        }
        
        int subtractions = 0;
        while (dividend - divisor >= 0){
            subtractions++;
            dividend -= divisor;
        }
        
        if (negatives == 1){
            subtractions = -subtractions;
        }
        
        return subtractions;
    }
};
```
還需要處理極端特殊狀況: INT_MIN / -1, 直接計算會造成 overflow

```
class Solution {
public:
    int divide(int dividend, int divisor) {

        // Special case: overflow.
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        /* We need to convert both numbers to negatives
         * for the reasons explained above.
         * Also, we count the number of negatives signs. */
        int negatives = 2;
        if (dividend > 0) {
            negatives--;
            dividend = -dividend;
        }
        if (divisor > 0) {
            negatives--;
            divisor = -divisor;
        }

        /* Count how many times the divisor has to be added
         * to get the dividend. This is the quotient. */
        int quotient = 0;
        while (dividend - divisor <= 0) {
            dividend -= divisor;
            quotient--;
        }

        /* If there was originally one negative sign, then
         * the quotient remains negative. Otherwise, switch
         * it to positive. */
        if (negatives != 1) {
            return -quotient;
        }
        return quotient;
    }
};
```

## Solution 2: 減去 2 的次方 Exponential Search

$2^* * divisor$ 找到最接近 dividend 的數字, 重複這個過程

Time: O(log n * log n)

+ 最壞的情況: 每次減掉最接近的數字後, 剩下的數字比一半又少一點點, 又得做一次 search.

```
int HALF_INT_MIN = -1073741824;

int divide(int dividend, int divisor) {

    // 防止 overflow
    if (dividend == INT_MIN && divisor == -1) {
        return INT_MAX;
    }

    // 轉換負數
    int negatives = 2;
    if (dividend > 0) {
        negatives--;
        dividend = -dividend;
    }
    if (divisor > 0) {
        negatives--;
        divisor = -divisor;
    }

    int quotient = 0;
    
    while (divisor >= dividend) {

        int powerOfTwo = -1;
        int value = divisor;
        /* Check if double the current value is too big. If not, continue doubling.
        * If it is too big, stop doubling and continue with the next step */
        while (value >= HALF_INT_MIN && value + value >= dividend) {
            value += value;
            powerOfTwo += powerOfTwo;
        }
        quotient += powerOfTwo;
        dividend -= value;
    }

    if (negatives != 1) {
        quotient = -quotient;
    }
    return quotient;
}
```

### Solution 3: 增加 2 的次方

兩個表格

powersOfTwo: 儲存 2 的次方, 之後從這邊調用商數

doubles: 儲存 divisor * 2的次方

從後面遍歷 doubles, 遇到比 dividend 較小的元素

dividend -= double\[i]

quotient += powersOfTwo

Time: O(log n)

Space: O(log n)

```
class Solution {
public:
    int HALF_INT_MIN = -1073741824;

    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) {
        return INT_MAX;
        }
        
        int negatives = 2;
        if (dividend > 0) {
            negatives--;
            dividend = -dividend;
        }
        if (divisor > 0) {
            negatives--;
            divisor = -divisor;
        }
        
        std::vector<int> doubles;
        std::vector<int> powersOfTwo;
        
        int powerOfTwo = -1;
        while (divisor >= dividend){
            doubles.push_back(divisor);
            powersOfTwo.push_back(powerOfTwo);
            if (divisor < HALF_INT_MIN){
                break;
            }
            divisor += divisor;
            powerOfTwo += powerOfTwo;
        }
        
        int quotient = 0;
        for (int i = doubles.size() - 1; i >= 0; i--) {
            if (doubles[i] >= dividend) {
                quotient += powersOfTwo[i];
                dividend -= doubles[i];
            }
        }
        
        if (negatives != 1) {
        return -quotient;
        }
        return quotient;
    }
};
```