def fix_text(mystr):
    """
    Reverse non-parenthesized words and remove parentheses from the correct words.

    Args:
    - mystr: Input string containing words in reverse order and correct words in parentheses.

    Returns:
    - Fixed text with reversed non-parenthesized words and parentheses removed from correct words.
    """
    # Split the input string into words
    words = mystr.split()
    result = []

    # Iterate through each word
    for word in words:
        # If the word starts with '(', remove the parentheses
        if word[0] == '(':
            result.append(word[1:-1])
        else:
            # If the word is not in parentheses, reverse it
            result.append(word[::-1])

    # Join the fixed words to form the output text
    return ' '.join(result)

# Test the function
INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

print(fix_text(INPUT))

# Check if the fixed text matches the correct answer
if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
