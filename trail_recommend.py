import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


def states():
    return ["None", "MA", "NH", "MI", "VT", "CT", "RI"]


class TrailRec(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Trail Recommender")
        self.geometry(f"{1100}x{580}")

        # when defining the row and col of the over arching grid

        # create tabview
        self.tab_view_filters = customtkinter.CTkTabview(self, width=250, height=100)
        self.tab_view_filters.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tab_view_filters.add("Trail Preferences")
        self.tab_view_filters.add("Tab 2")
        self.tab_view_filters.add("Tab 3")
        self.tab_view_filters.tab("Trail Preferences").grid_columnconfigure(3, weight=1)  # configure grid of individual tabs
        self.tab_view_filters.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # self.tabview.tab("tabX") assigns the obect to the given tabX tab
        self.states_menu = customtkinter.CTkOptionMenu(self.tab_view_filters.tab("Trail Preferences"), dynamic_resizing=True,
                                                       values=states())

        self.states_menu.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tab_view_filters.tab("Trail Preferences"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=0, column=1, padx=20, pady=(10, 10))

        self.switch_dog_friendly = customtkinter.CTkSwitch(self.tab_view_filters.tab("Trail Preferences"), text=f"Dog Friendly")
        self.switch_dog_friendly.grid(row=0, column=2, padx=20, pady=(10, 10))

        self.search_button = customtkinter.CTkButton(self.tab_view_filters.tab("Trail Preferences"), text="Search",
                                                     command=self.open_input_dialog_event)
        self.search_button.grid(row=2, column=5, padx=20, pady=(10, 10))

        self.label_tab_2 = customtkinter.CTkLabel(self.tab_view_filters.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, width=1000, height=400,
                                                                 label_text="Trail results")
        self.scrollable_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        example_image = customtkinter.CTkImage(Image.open("images/smile_face.png"))
        for i in range(100):
            trail_result = customtkinter.CTkTextbox(master=self.scrollable_frame)
            #trail_result.image_create(0.0, image=example_image)
            trail_result.insert(50.0, "this is a test image")
            trail_result.grid(row=i, column=0, padx=10, pady=(0, 20))
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)
            #self.scrollable_frame_switches.append(trail_result)
        # self.scrollable_frame.pack(expand=False)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = TrailRec()
    app.mainloop()
