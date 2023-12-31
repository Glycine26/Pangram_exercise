import string
class my_Pangram_class():
    def pangram(self, my_input):
        capital_input = set(my_input.upper())
        #print(capital_input)
        a_to_z_set = set(string.ascii_uppercase)
        #print(a_to_z_set)

        if capital_input & a_to_z_set == a_to_z_set:
            print("It's a Pangram")
        else:
            print("It's not a Pangram")


my_pangram = my_Pangram_class()
# result = my_pangram.pangram("The ick brown fox jumps over the lazy dog")
result = my_pangram.pangram("The quick brown fox  over the lazy dog")
print(result)
# check once