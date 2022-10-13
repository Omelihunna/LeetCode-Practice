class Solution:
    def toHex(self, num: int) -> str:
        m = dict.fromkeys(range(16), 0);
 
        digit = ord('0');
        c = ord('a');

        for i in range(16) :
            if (i < 10) :
                m[i] = chr(digit);
                digit += 1;

            else :
                m[i] = chr(c);
                c += 1
        res = "";

        # check if num is 0 and directly return "0"
        if (not num) :
            return "0";

        # if num>0, use normal technique as
        # discussed in other post
        if (num > 0) :
            while (num) :
                res = m[num % 16] + res;
                num //= 16;

        # if num<0, we need to use the elaborated
        # trick above, lets see this
        else :

            # store num in a u_int, size of u_it is greater,
            # it will be positive since msb is 0
            n = num + 2**32;

            # use the same remainder technique.
            while (n) :
                res = m[n % 16] + res;
                n //= 16;

        return res;