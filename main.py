import customtkinter as ctk
from tabs.add_tab import AddProductFrame
from tabs.search_tab import SearchProductFrame
from tabs.report_tab import ReportProductFrame
from tabs.config_tab import ConfigProductFrame

ctk.set_default_color_theme("green")

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("StyleHub - DashBoard")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_navbar()
        self.create_content_area()
        self.create_frames()

        show_frame(self.add_frame)

    def create_navbar(self):
        frame_nav = ctk.CTkFrame(self, width=200, height=720, corner_radius=10, border_width=1, border_color='green')
        frame_nav.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        add_button = ctk.CTkButton(frame_nav, text="Add", command=lambda: show_frame(self.add_frame))
        add_button.grid(row=0, column=0, pady=10, padx=20, sticky="ew")

        search_button = ctk.CTkButton(frame_nav, text="Search", command=lambda: show_frame(self.search_frame))
        search_button.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        report_button = ctk.CTkButton(frame_nav, text="Reports", command=lambda: show_frame(self.report_frame))
        report_button.grid(row=3, column=0, pady=10, padx=20, sticky="ew")

        config_button = ctk.CTkButton(frame_nav, text="Configs", command=lambda: show_frame(self.config_frame))
        config_button.grid(row=4, column=0, pady=10, padx=20, sticky="ew")

    def create_content_area(self):
        content_frame = ctk.CTkFrame(self, width=1080, height=720, corner_radius=10, border_width=1,
                                     border_color='green')
        content_frame.grid(row=0, column=1, sticky="nswe", padx=(10, 5), pady=10)

        center_frame = ctk.CTkFrame(content_frame, width=1080, height=720, corner_radius=10, fg_color="transparent")
        center_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.center_frame = center_frame

    def create_frames(self):
        self.add_frame = AddProductFrame(self.center_frame)
        self.search_frame = SearchProductFrame(self.center_frame)
        self.report_frame = ReportProductFrame(self.center_frame)
        self.config_frame = ConfigProductFrame(self.center_frame)
        self.update_frame = None
        for frame in (self.add_frame, self.search_frame, self.report_frame, self.config_frame):
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)


def show_frame(frame):
    frame.tkraise()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
