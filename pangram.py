"""14. Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"""

def pangram(my_input):
    my_list = []
    for letter in my_input:
        capital_letter = letter.capitalize()
        ascii_number = ord(capital_letter)
        if 65 <= ascii_number <= 90:
            my_list.append(ascii_number)
    a_to_z_list = range(65,91)
    bucket_list = list(a_to_z_list)
    for ascii in my_list:
        if ascii in bucket_list:
            bucket_list.remove(ascii)
            print(bucket_list)
    if bucket_list == [ ]:
        print("It's a pangram")
    else:
        print("it's not pangram")

        return


result = pangram("The quick brown fox")
print(result)
#take the number