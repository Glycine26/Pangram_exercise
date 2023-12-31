class my_Pangram_class():
    def pangram(self, my_input):
        capital_input = set(my_input.upper())
        print(capital_input)
        a_to_z_set = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

        if capital_input & a_to_z_set == a_to_z_set:
            print("It's a Pangram")
        else:
            print("It's not a Pangram")


my_pangram = my_Pangram_class()
# result = my_pangram.pangram("The ick brown fox jumps over the lazy dog")
result = my_pangram.pangram("The fox jumps over the lazy dog. Here is the summary of Fox And The Goat story with pictures. Once upon a time, a fox was roaming in search of water. The fox was very thirsty, and he came across an old well in a village. He tried peering into the well to see if it had water, and the fox had to leap onto the wall of the well to look inside. The fox slipped and fell into the well and drank the water. Now, he struggled to come out of the well as he could not jump high enough. He had to wait the whole night to get help from someone. A goat happened to pass by the well and saw the fox strucked inside it.The fox instantly thought of a cunning idea to use this opportunity to his advantage. He said to the innocent goat that the water in the well was very refreshing and told him to jump inside and relish it. The goat jumped into the well and drank the water, and fell for the fox’s trap. Fox and the goat both were now stranded in the old well. The goat asked the fox for a way to climb out of the well. The fox said that he would climb on the back of the goat and go out and then help the goat to climb out as well. The goat once again agreed without thinking twice, and the fox then climbed onto the back of the goat and was able to come out of the well. Once the fox was out of the well, he began to walk away. The fox said to the goat that he should have thought of a way to climb out of the well before jumping inside. The innocent goat was now in need of help himself.")
print(result)
# check once