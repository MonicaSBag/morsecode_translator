from tkinter import Tk, Canvas, Entry, Button, END
from tkinter import messagebox

joined_morse_code = ''
# MORSE CODE ALPHABET. NORMAL ALPHABET TO MORSE CODE
normal_to_morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                   "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                   "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                   "y": "-.--", "z": "--..", 1: ".----", 2: "..---", 3: "...--", 4: "....-", 5: ".....", 6: "-....",
                   7: "--...", 8: "---..", 9: "----.", 0: "-----", " ": " "}
# MORSE CODE TO ALPHABET
morse_to_normal = {normal_to_morse[value]: value for (value) in normal_to_morse}
control_list = [key for key in normal_to_morse]
control_list2 = [key for key in morse_to_normal]


def traduce():
    try:
        try_again = "y"
        while try_again == "y":
            user_request = entry_widget1.get().lower()
            # CHANGE TO MORSE CODE
            try:
                str = " "
                user_text = list(user_request)  # USER INPUT TO LIST
                morse_code = [normal_to_morse[letter] for letter in
                              user_text]  # TAKE THE VALUES FROM THE DICTIONARY WITH THE SAME KEY
                joined_morse_code = str.join(morse_code)  # MAKE IT A STRING TO PRINT TO THE USER
                return return_text.insert(0, joined_morse_code)  # PRINT IN THE INSERT TOOL
            # CHANGE TO NORMAL ALPHABET
            except KeyError:
                str = ""
                user_text2 = user_request.split()  # USER INPUT TO LIST. SPLIT WITHIN THE BLANK SPACES
                normal_alphabet = [morse_to_normal[code] for code in
                                   user_text2]  # TAKE THE VALUES FROM THE DICTIONARY WITH THE SAME KEY
                joined_morse_code = str.join(normal_alphabet)
                return return_text.insert(0, joined_morse_code)  # PRINT IN THE INSERT TOOL
    except KeyError:
        messagebox.showinfo(title="Character not valid", message="Sorry\n"
                                                                 "Please check your text for any not-valid character.")


def clear():
    entry_widget1.delete(0, END)
    return_text.delete(0, END)


# LAYOUT
window = Tk()
window.title = "MORSE CODE"
window.config(width=500, height=300, padx=50, pady=50)
canva = Canvas(width=500, height=250, highlightthickness=0)
title_label = canva.create_text(250, 10, text="MORSE CODE", font=("Times", 20))
description_label2 = canva.create_text(240, 65, text="You can traduce both ways!\n"
                                                     "These program contains only the Morse Code Alphabet and numbers\n"
                                                     "It does not contain any this characters groups:\n"
                                                     "(ñ, á, é, í, ó, ú, !, @, #, $,.., %)", font=("Times", 11))
description_label = canva.create_text(160, 115, text="Write the text you would like to traduce:", font=("Times", 12))
canva.grid(column=3, row=0, columnspan=3)
entry_widget1 = Entry(width=70, )
user_input = canva.create_window(250, 140, window=entry_widget1)
second_label = canva.create_text(68, 165, text="Final text:", font=("Times", 12))
return_text = Entry(width=70)
return_ans = canva.create_window(250, 190, window=return_text)
traduce_text = Button(text="Traduce", font=("Times", 10), width=11, command=traduce, padx=25)
traduce_text.grid(column=3, row=2)
clear_button = Button(text="Clear", font=("Times", 10), width=11, command=clear, padx=25)
clear_button.grid(column=5, row=2)
window.mainloop()
