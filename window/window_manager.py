from tkinter import ttk
import tkinter


# Window class to control the GUI for the application
class JQWindowManager:
    def __init__(self, title: str, questions: str):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.questions = questions
        self.mainframe = ttk.Frame(self.root, padding="12")
        self.mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        self.__setup_frame()
        self.__build_widgets()

    def __setup_frame(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)  # make question_text grow

    def __build_widgets(self):
        # Question Display
        self.question_label = ttk.Label(self.mainframe, text="Welcome to the jq trainer!", wraplength=500)
        self.question_label.grid(column=0, row=0, sticky="W")
        self.question_label.config(font=("TkDefaultFont", 44))

        # Display box for Json file question
        # We will use this box to display the question prompt
        self.question_text = tkinter.Text(self.mainframe, height=5, width=80, state="disabled", wrap="word")
        self.question_text.grid(row=1, column=0, sticky="NSEW")
        # Placeholder data
        self.question_text.config(state="normal")
        self.question_text.insert("1.0", "Your JSON prompt will appear here...")
        self.question_text.config(state="disabled")

        # Add Scrollbar
        # self.scrollbar = tkinter.Scrollbar(self.mainframe, command=self.question_text.yview)
        # self.scrollbar.grid(row=1, column=1, sticky="NS")
        # self.question_text.config(yscrollcommand=self.scrollbar.set)

        # Input Field
        self.input_entry = ttk.Entry(self.mainframe, width=80)
        self.input_entry.grid(column=0, row=3, rowspan=3, pady=20, sticky="EW")
        self.input_entry.bind("<Return>", self.__handle_submit)

        # Feedback
        self.feedback_text = tkinter.Text(self.mainframe, height=5, width=80, wrap="word", state="disabled")
        self.feedback_text.grid(column=0, row=7, pady=10, sticky="EW")

    def load_question(self):
        question_text = self.questions
        self.question_text.config(state="normal")
        self.question_text.delete("1.0", "end")
        self.question_text.insert("1.0", question_text)
        self.question_text.config(state="disabled")

    def __handle_submit(self, event=None):
        query = self.input_entry.get()
        # Validate query here
        if query == "jq .":
            feedback = "✅ Correct!"
        else:
            feedback = "❌ Incorrect. Try again."

        self.__display_feedback(feedback)
        self.input_entry.delete(0, "end")

    def __display_feedback(self, message):
        self.feedback_text.config(state="normal")
        self.feedback_text.delete("1.0", "end")
        self.feedback_text.insert("1.0", message)
        self.feedback_text.config(state="disabled")

    def run(self):
        self.root.mainloop()
