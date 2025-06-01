from tkinter import ttk
import tkinter
import subprocess
import tkinter.messagebox


# Window class to control the GUI for the application
class JQWindowManager:
    def __init__(self, title: str, questions):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.questions = questions
        self.mainframe = ttk.Frame(self.root, padding="12")
        self.mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        self.count = 0
        self.__setup_frame()
        self.__build_widgets()

    def __setup_frame(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=3)
        self.mainframe.rowconfigure(1, weight=1)  # make question_text grow
        self.mainframe.rowconfigure(3, weight=2)
        self.mainframe.columnconfigure(1, weight=2)  # feedback_text gets more priority

    def __build_widgets(self):
        # Question Display
        self.question_label = ttk.Label(self.mainframe, text="Welcome to the jq trainer!", wraplength=500)
        self.question_label.grid(column=0, row=0, sticky="W")
        self.question_label.config(font=("TkDefaultFont", 44))

        # Display box for Json file question
        # We will use this box to display the question prompt
        self.question_text = tkinter.Text(
            self.mainframe, height=5, width=50, padx=5, pady=5, state="disabled", wrap="word"
        )
        self.question_text.grid(row=1, column=0, sticky="NSEW")
        self.question_text.config(font=("TkDefaultFont", 24))
        self.load_question()

        # Input Field
        self.input_entry = ttk.Entry(self.mainframe, width=50)
        self.input_entry.grid(column=0, row=3, padx=5, pady=20, sticky="NSEW")
        self.input_entry.config(font=("Courier", 24))
        self.input_entry.bind("<Return>", self.__handle_submit)

        # Feedback
        self.feedback_text = tkinter.Text(self.mainframe, height=5, width=80, wrap="word", state="disabled")
        self.feedback_text.grid(column=1, row=0, rowspan=5, pady=10, sticky="NSEW")
        self.feedback_text.config(font=("Courier", 18), borderwidth=2, relief="sunken")

    def load_question(self, count: int = 0):
        if count == 0 and self.count != 0:
            count = self.count  # starting starts at 0, if count is passed load that question instead
        if count >= len(self.questions):
            # end game scenario
            self.end_game()
        question_text = self.questions[count].get("question")
        self.question_text.config(state="normal")
        self.question_text.delete("1.0", "end")
        self.question_text.insert("1.0", question_text)
        self.question_text.config(state="disabled")

    def expected_output(self, count: int = 0) -> str:
        """loads the expected output for the question number
        {
            "question": "How many women competed in the 1924 Olympics?",
            "expected_output": "23",
            "dataset": "olympics.json"
        }
        """
        if count == 0 and self.count != 0:
            count = self.count
        answer = self.questions[count].get("expected_output")
        return answer

    def __handle_submit(self, event=None):
        query = self.input_entry.get()
        expected = self.expected_output()
        try:
            result = subprocess.check_output(["jq", query, "./olympics.json"], stderr=subprocess.STDOUT).decode("utf-8")
        except subprocess.CalledProcessError as e:
            self.__display_feedback(f"❌ JQ Error:\n{e.output.decode('utf-8').strip()}")
            return
        # Correct/Wrong answer
        if str(result).strip() == expected:
            self.__display_feedback(f"✅ Correct!\nYour result:{str(result).strip()}\nExpected:{expected}")
            self.count += 1
            self.load_question(self.count)
        else:
            self.__display_feedback(f"❌ Incorrect. Try again.\nYour result:{str(result).strip()}\nExpected:{expected}")
        self.input_entry.delete(0, "end")

    def __display_feedback(self, message):
        self.feedback_text.config(state="normal")
        self.feedback_text.delete("1.0", "end")
        self.feedback_text.insert("1.0", message)
        self.feedback_text.config(state="disabled")

    def end_game(self):
        tkinter.messagebox.showinfo(
            "JQ Master!",
            "🚀 Data? Conquered.\n🧠 Brain? Buffed.\n🏅 Status? Certified JQ Wizard!\nGo flex those filters 💪\n🎉🎇🎆",
        )
        self.root.quit()

    def run(self):
        self.root.mainloop()
