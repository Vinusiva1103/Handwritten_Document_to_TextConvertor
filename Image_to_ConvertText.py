import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import pyttsx3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Set the Tesseract executable path (update it based on your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to perform OCR on the input image
def perform_ocr(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    recognized_text = pytesseract.image_to_string(gray_image)
    return recognized_text

# Function to open a file dialog and process the selected image

def CameraCapture():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not access the camera.")
    else:
        # Capture a single frame from the camera
        ret, frame = camera.read()
        if ret:
            # Save the captured frame to a file (you can change the file format and filename)
            image_filename = "captured_image.jpg"
            cv2.imwrite(image_filename, frame)
            print(f"Image saved as {image_filename}")
            # Release the camera
            camera.release()
        else:
            print("Error: Failed to capture a frame.")
    # Close all OpenCV windows
    cv2.destroyAllWindows()


def APP():
    app = tk.Tk()
    app.title("Lens")
    # Set the window size (width x height)
    app.geometry("1500x850")
    # Disable window resizing (both horizontally and vertically)
    app.resizable(False, False)
    app.configure(bg="#1D242B")
    app.state("zoomed")

    image = Image.open("Lens1.png")
    image = ImageTk.PhotoImage(image)
    image_label1 = tk.Label(app, image=image, bg="#1D242B")
    image_label1.pack(padx=50, pady=60)
    image_label1.place(y=30, x=650)



    Sys_Title = tk.Label(app, text="Lens App is Easy to Convert Text", font=('Comfortaa', 30, 'bold'), bg="#1D242B",
                         fg="#FF1F1F")
    Sys_Title.pack()
    Sys_Title.place(y=180, x=500)
    Sys_Subtitle = tk.Label(app,
                            text="More than 10000 enterprises convert PDF Documents and images to actionable text with Nanonets",
                            font=('Comfortaa', 10, 'bold'), bg="#1D242B",
                            fg="#5D6E80")
    Sys_Subtitle.pack()
    Sys_Subtitle.place(y=250, x=500)

    Import_button = tk.Button(app,
                              text="Image to Text", command=main_screen,
                              bg="#0C72D7", fg="white", pady=2, padx=80, font=('Comfortaa', 12, 'bold'),
                              activebackground="#9C0000", activeforeground="white")
    Import_button.pack(pady=0, padx=20)
    Import_button.place(x=40, y=750)

    app.mainloop()



def main_screen():
    main_window = tk.Tk()
    main_window.title("Image to Text Coverter")
    # Set the window size (width x height)
    main_window.geometry("1500x850")
    # Disable window resizing (both horizontally and vertically)
    main_window.resizable(False, False)
    main_window.configure(bg="#1D242B")
    main_window.state("zoomed")

    image = Image.open("Lens1.png")
    image = ImageTk.PhotoImage(image)
    image_label1 = tk.Label(main_window, image=image, bg="#1D242B")
    image_label1.pack(padx=50,pady=60)
    image_label1.place(y=10,x=650)

    def open_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
        if file_path:
            extracted_text = perform_ocr(file_path)
            text_display.delete(1.0, tk.END)  # Clear the text display
            text_display.insert(tk.END, extracted_text)  # Display the extracted text

            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image=image)

            # Display the image on a label
            image_label_Update.config(image=photo)
            image_label_Update.photo = photo

    Sys_Title = tk.Label(main_window, text="Image to Text Coverter", font=('Comfortaa', 30, 'bold'), bg="#1D242B", fg="#FF1F1F")
    Sys_Title.pack()
    Sys_Title.place(y=145, x=550)
    Sys_Subtitle = tk.Label(main_window, text="More than 10000 enterprises convert PDF Documents and images to actionable text with Nanonets", font=('Comfortaa', 10, 'bold'), bg="#1D242B",
                            fg="#5D6E80")
    Sys_Subtitle.pack()
    Sys_Subtitle.place(y=210, x=500)


    imageUpdate = Image.open("Upload.png")
    imageUpdate = ImageTk.PhotoImage(imageUpdate)
    image_label_Update = tk.Label(main_window, image=imageUpdate, bg="#1D242B",)
    image_label_Update.pack(padx=200, pady=200)
    image_label_Update.place(x=20, y=250)

    # Create a multi-line text box (Text widget)
    text_display = tk.Text(main_window, wrap=tk.WORD,font=('Comfortaa', 11, 'bold'), bg="#1D242B", fg="#FFF",height=19,padx=20,pady=20)
    text_display.pack(padx=10, pady=10,expand=True)
    # Insert some initial text into the text box
    text_display.insert(tk.END, "")
    text_display.place(x=800, y=250)


    Import_button = tk.Button(main_window,
                              text="Import Image", command=open_image,
                              bg="#0C72D7", fg="white", pady=2, padx=80, font=('Comfortaa', 12, 'bold'),
                              activebackground="#9C0000", activeforeground="white")
    Import_button.pack(pady=0, padx=20)
    Import_button.place(x=40, y=750)
    TextConvert_button = tk.Button(main_window,command=CameraCapture,
                              text="Converter Text",
                              bg="#0C72D7", fg="white", pady=2, padx=80, font=('Comfortaa', 12, 'bold'),
                              activebackground="#9C0000", activeforeground="white")
    TextConvert_button.pack(pady=0, padx=20)
    TextConvert_button.place(x=350, y=750)
    def text_to_pdf():
        input_text = text_display.get("1.0", "end-1c")  # Get the text from the Text widget
        output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if input_text and output_pdf:
            c = canvas.Canvas(output_pdf, pagesize=letter)
            c.setFont("Helvetica", 12)

            lines = input_text.split('\n')
            for line in lines:
                c.drawString(100, 750, line)
                c.showPage()

            c.save()

            PdfPath.config(text=f"PDF file '{output_pdf}' has been generated.")
        else:
            PdfPath.config(text="Please enter text and select a destination for the PDF.")

    ConvertPDF_button = tk.Button(main_window,
                              text="Export PDF", command=text_to_pdf,
                              bg="#FF1F1F", fg="white", pady=2, padx=80, font=('Comfortaa', 12, 'bold'),
                              activebackground="#9C0000", activeforeground="white")
    ConvertPDF_button.pack(pady=20, padx=20)
    ConvertPDF_button.place(x=900, y=750)


    def text_to_speech():
        text = text_display.get("1.0", tk.END)

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty("rate", 150)  # Speed of speech (words per minute)
        engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

        # Convert and speak the text
        engine.say(text)
        engine.runAndWait()




    Speak_button = tk.Button(main_window,
                               text="Speak", command=text_to_speech,
                               bg="#FF1F1F", fg="white", pady=2, padx=80, font=('Comfortaa', 12, 'bold'),
                               activebackground="#9C0000", activeforeground="white")
    Speak_button.pack(pady=20, padx=20)
    Speak_button.place(x=1180, y=750)

    Sys_Subtitle2 = tk.Label(main_window,
                             text="We'll never sell or share your data. For more details,here's our Privacy Policy",
                             font=('Comfortaa', 10, 'bold'), bg="#1D242B",
                             fg="#5D6E80")
    Sys_Subtitle2.pack(pady=90,padx=10)
    Sys_Subtitle2.place(x=50, y=800)
    PdfPath = tk.Label(main_window,
                             text="",
                             font=('Comfortaa', 10, 'bold'), bg="#1D242B",
                             fg="#5D6E80")
    PdfPath.pack(pady=90, padx=10)
    PdfPath.place(x=700, y=800)

    main_window.mainloop()
    main_window.destroy()

if __name__ == "__main__":
    main_screen()


