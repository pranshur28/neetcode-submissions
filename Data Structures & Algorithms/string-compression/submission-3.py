class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars) == 0:
            return 0

        write = 0
        i = 0 

        while i < len(chars):
            j = i
            

            while j < len(chars) and chars[j] == chars[i] :

                j = j + 1

            run_len = j - i 

            chars[write] = chars[i]
            write = write + 1 

            if run_len > 1:
                count_str = str(run_len)

                digit_index = 0 

                while digit_index < len(count_str):
                    chars[write] = count_str[digit_index]
                    write = write + 1
                    digit_index = digit_index + 1

            i = j

        return write 

