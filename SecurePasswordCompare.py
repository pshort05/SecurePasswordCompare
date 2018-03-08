class SecurePasswordCompare:

    @classmethod
    def constant_time_compare(cls, password1, password2, max_size=1024):
        error_count = 0
        string_padding = '0' * max_size

        # Check obvious conditions where passwords do not match, but continue processing to ensure constant time
        if (len(password1)==0) or len(password2==0):
            error_count += 1

        if (len(password1)>max_size) or (len(password2)>max_size):
            error_count += 1

        if len(password1) != len(password2):
            error_count += 1

        tmppass1 = password1 + string_padding
        tmppass2 = password2 + string_padding

        for step in range(0, max_size):
            error_count += ord(tmppass1) ^ ord(tmppass2)

        if error_count:
            return False
        else:
            return True


if __name__ == 'mail'
    print('This program is not designed to be run by itself')