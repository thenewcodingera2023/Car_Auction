# Car_Auction Car Auction Application [If you are reading this Mr Mccourt,  I have proved myself to be the worthy one]

#Importing neccessary Libraries
from customtkinter import *
from PIL import Image
import webbrowser
import random
import customtkinter
import subprocess
from desktop_notifier import DesktopNotifier
import platform

#My library


if platform.system() == "Windows": #Check User Platform
    #Use Library
    notifier = DesktopNotifier()
    #Function for sending desktop/user message
    def notify(title, text):
        notifier.send(title=title, message=text)
    #Windows/Linux Version
else:
    #MacOS Version

    #Blank
    CMD = '''
    on run argv
    display notification (item 2 of argv) with title (item 1 of argv)
    end run
    '''
    #Initate Function for Mac OS Users
    def notify(title, text):
        subprocess.call(['osascript', '-e', CMD, title, text])


#Variables Initation ---
Car_Brand = ["Porsche", "Mercedes", "Triumph", "Peugeot", "Honda", "Mini", "Jaguar", "Aston", "BMW", "Ford"] #Cars
reserve_price = [] # Reserve Price - Random Generated For More Excitement!
for i in range(1,11): #Range 
    price = random.randint(1000,5000) # Generate numbers randomly ranging from 1000 - 5000
    reserve_price.append(price) # Add generated number to list
bid_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Bid Data incase User Bids
Andrew = False #Competitor - Later
sold = [False, False, False, False, False, False, False, False, False, False] #Sales Status Of Cars [On Stock or not On Stock?]
bid_competition = [] #Default Bidding 
for i in range(1,11):
    bid_ai = random.randint(5001,9000)# Generate numbers randomly ranging from 1000 - 5000
    bid_competition.append(bid_ai) # Add generated number to list
topay = 0 #Total Money To Be Paid


# Side Functions    
def bomb(name): #THis Function Is For Destroying Windows.
    name.destroy()
    name.quit()

def rick(): #Logging in With Google Function But I am Too Lazy
    return webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')

def nuke():
    Main_GUI.destroy()
    Main_GUI.quit()



#Car Info UI

def car_display():
    global car_screen
    bomb(Main_GUI)
    car_screen = CTk()
    car_screen.geometry('1000x900')
    car_screen.resizable(0,0)
    car_screen.title("Da Den")
    #--- Images

    porsche_data = Image.open("porsche-model.png")
    mercedes_data = Image.open("mercedes.png")
    triumph_data = Image.open("triumph.png")
    Peugeot_data = Image.open("peugeot.png")
    honda_data = Image.open("honda.png")
    mini_data = Image.open('mini.png')
    jaguar_data = Image.open('jaguar.png')
    aston_data = Image.open('aston.png')
    bmw_data = Image.open('bmw.png')
    ford_data = Image.open('ford.png')


    porsche = CTkImage(dark_image=porsche_data, light_image=porsche_data, size=(288,162))
    mercedes = CTkImage(dark_image=mercedes_data, light_image=mercedes_data, size=(254,143))
    triumph = CTkImage(dark_image=triumph_data, light_image=triumph_data, size=(259, 194))
    Peugeot = CTkImage(dark_image=Peugeot_data, light_image=Peugeot_data, size=(276, 145))
    honda = CTkImage(dark_image=honda_data, light_image=honda_data, size=(264, 130))
    mini = CTkImage(dark_image=mini_data, light_image=mini_data, size=(269, 174))
    jaguar = CTkImage(dark_image=jaguar_data, light_image=jaguar_data, size=(262, 175))
    aston = CTkImage(dark_image=aston_data, light_image=aston_data, size=(288, 162))
    bmw = CTkImage(dark_image=bmw_data, light_image=bmw_data, size=(322, 194))
    ford = CTkImage(dark_image=ford_data, light_image=ford_data, size=(288, 162))

    #---
    Outer_Car_Frame = CTkFrame(master=car_screen, width=1000, height=880, fg_color="#ffffff")
    Outer_Car_Frame.pack_propagate(0)
    Outer_Car_Frame.pack(side="top")

    car_frame = CTkFrame(master=Outer_Car_Frame, width=500, height=880, fg_color="#ffffff")
    car_frame.pack_propagate(0)
    car_frame.pack(side="left")
    CTkLabel(master=car_frame, text="Porsche ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20),image=porsche, compound='right').pack(anchor="w", pady=(0, 5), padx=(25,0))
    CTkLabel(master=car_frame, text="Mercedes ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=mercedes, compound='right').pack(anchor="w", pady=(20, 5), padx=(25,0))
    CTkLabel(master=car_frame, text="Triumph ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=triumph, compound='right').pack(anchor="w", pady=(20, 5), padx=(25,0))
    CTkLabel(master=car_frame, text="Peugeot ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=Peugeot, compound='right').pack(anchor="w", pady=(20, 5), padx=(25,0))
    CTkLabel(master=car_frame, text="Ford ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=ford, compound='right').pack(anchor="w", pady=(20, 5), padx=(25,0))


    #---


    Second = CTkFrame(master=Outer_Car_Frame, width=500, height=880, fg_color="#ffffff")
    Second.pack_propagate(0)
    Second.pack(side="right")
    CTkLabel(master=Second, text="Honda ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=honda, compound='right').pack(anchor="w", pady=(0, 5), padx=(0, 25))
    CTkLabel(master=Second, text="Mini ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=mini, compound='right').pack(anchor="w", pady=(20, 5), padx=(0, 25))
    CTkLabel(master=Second, text="Jaguar ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=jaguar, compound='right').pack(anchor="w", pady=(20, 5), padx=(0, 25))
    CTkLabel(master=Second, text="Aston Martin ", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=aston, compound='right').pack(anchor="w", pady=(20, 5), padx=(0, 25))
    CTkLabel(master=Second, text="BMW", text_color="#601E88", anchor="e", justify="left", font=("Arial Bold", 20), image=bmw, compound='right').pack(anchor="w", pady=(20, 5), padx=(0, 25))
    #---

    CTkButton(master=car_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), compound='bottom', command=main_screen).pack()

    #---
    car_screen.mainloop()

#Car Stats UI

class car_info:
    def __init__(self):
        if 'Main_GUI' in globals():
            try:
                Main_GUI.destroy()
            except Exception:
                pass
        if 'vip_screen' in globals():
            try:
                vip_screen.destroy()
            except Exception:
                pass
        self.app = customtkinter.CTk()
        self.app.title("")
        self.app.geometry("350x300")
        self.app.minsize(350, 300)
        self.app.maxsize(350, 300)

        self.car_stats()

        self.app.mainloop()

    def car_stats(self):
        title_label = customtkinter.CTkLabel(self.app, text="Model Exploration", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)


        form_frame = customtkinter.CTkFrame(self.app)
        form_frame.pack(padx=20, pady=20)


        product_name_label = customtkinter.CTkLabel(form_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, padx=10, pady=5)


        self.product_name_combo_box = customtkinter.CTkComboBox(form_frame, values=Car_Brand)
        self.product_name_combo_box.grid(row=0, column=1, padx=10, pady=5)

        # create a button to submit the bidding
        submit_button = customtkinter.CTkButton(self.app, text="View Car", command=self.view)
        submit_button.pack(pady=10)

        self.exit_button = customtkinter.CTkButton(self.app, text='Exit', command=self.destroy_window)
        self.exit_button.pack(pady=(20,0))


    def destroy_window(self):
        self.app.destroy()
        main_screen()

    def view(self):
        data = self.product_name_combo_box.get()
        self.app.destroy()
        self.app.quit()
        if data in globals():
            globals()[data]() 



#View Bid UI


class PriceBoard:
    def __init__(self):
        bomb(Main_GUI)
        self.app = customtkinter.CTk()
        self.app.title("Bidding Application")
        self.app.geometry("700x500")
        self.app.minsize(700, 500)
        self.app.maxsize(700, 500)

        self.reserve()

        self.app.mainloop()



    def reserve(self):
        main_frame = customtkinter.CTkFrame(self.app, width=700, height=400)
        main_frame.pack_propagate(0)
        main_frame.pack(side='top')

        left_frame = customtkinter.CTkFrame(main_frame, width=350, height=400)
        left_frame.pack_propagate(0)
        left_frame.pack(side='left')

        title_label = customtkinter.CTkLabel(left_frame, text="Reserve Price View", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        inside_left_frame = customtkinter.CTkFrame(left_frame)
        inside_left_frame.pack(padx=20, pady=20)


        product_name_label = customtkinter.CTkLabel(inside_left_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, padx=10, pady=5)


        self.product_name_combo_box = customtkinter.CTkComboBox(inside_left_frame, values=Car_Brand)
        self.product_name_combo_box.grid(row=0, column=1, padx=10, pady=5)


        submit_button = customtkinter.CTkButton(left_frame, text="Look For Reserve Price", command=self.search)
        submit_button.pack(pady=10)

        result_label = customtkinter.CTkLabel(left_frame, text="Reserve Price: ")
        result_label.pack(pady=10)

        self.result_entry = customtkinter.CTkEntry(left_frame, justify='center')
        self.result_entry.pack(pady=5)

        right_frame = customtkinter.CTkFrame(main_frame, width=350, height=400)
        right_frame.pack_propagate(0)
        right_frame.pack(side='right')


        title_label = customtkinter.CTkLabel(right_frame, text="Current Bidding Price View", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)


        inside_right_frame = customtkinter.CTkFrame(right_frame)
        inside_right_frame.pack(padx=20, pady=20)

        product_name_label = customtkinter.CTkLabel(inside_right_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, padx=10, pady=5)


        self.product_name_combo_box2 = customtkinter.CTkComboBox(inside_right_frame, values=Car_Brand)
        self.product_name_combo_box2.grid(row=0, column=1, padx=10, pady=5)


        submit_button = customtkinter.CTkButton(right_frame, text="Look For Bidding Price", command=self.search2)
        submit_button.pack(pady=10)

        result_label = customtkinter.CTkLabel(right_frame, text="Current Bidding Price: ")
        result_label.pack(pady=10)

        self.result_entry2 = customtkinter.CTkEntry(right_frame, justify='center')
        self.result_entry2.pack(pady=5)

        self.exit_button = customtkinter.CTkButton(self.app, text='Exit', command=self.destroy_window)
        self.exit_button.pack(pady=(20,0))





    def search(self):
        car_index_number = Car_Brand.index(self.product_name_combo_box.get())
        self.result_entry.delete(0, 'end')
        self.result_entry.insert(0,"$"+str(reserve_price[car_index_number]))

    def search2(self):
        car_index_number = Car_Brand.index(self.product_name_combo_box2.get())
        self.result_entry2.delete(0, 'end')
        self.result_entry2.insert(0,"$"+str(bid_competition[car_index_number]))

    def destroy_window(self):
        self.app.destroy()
        main_screen()

#Bid UI



class BiddingApp:
    def __init__(self):
        bomb(Main_GUI)
        self.app = customtkinter.CTk()
        self.app.title("Bidding Application")
        self.app.geometry("700x500")
        self.app.minsize(700, 500)
        self.app.maxsize(700, 500)

        self.bid()

        self.app.mainloop()

    def bid(self):




        title_label = customtkinter.CTkLabel(self.app, text="Bidding Application", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)


        form_frame = customtkinter.CTkFrame(self.app)
        form_frame.pack(padx=20, pady=20)


        product_name_label = customtkinter.CTkLabel(form_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, padx=10, pady=5)


        self.product_name_combo_box = customtkinter.CTkComboBox(form_frame, values=Car_Brand)
        self.product_name_combo_box.grid(row=0, column=1, padx=10, pady=5)


        bidding_price_label = customtkinter.CTkLabel(form_frame, text="Bidding Price:")
        bidding_price_label.grid(row=1, column=0, padx=10, pady=5)


        self.bidding_price_entry = customtkinter.CTkEntry(form_frame)
        self.bidding_price_entry.grid(row=1, column=1, padx=10, pady=5)


        # create a button to submit the bidding
        submit_button = customtkinter.CTkButton(self.app, text="Submit Bidding", command=self.collection)
        submit_button.pack(pady=10)

        # create a label for the result
        result_label = customtkinter.CTkLabel(self.app, text="Bidding Result:")
        result_label.pack(pady=10)

        # create a text field for the result
        self.result_entry = customtkinter.CTkEntry(self.app, justify="center")
        self.result_entry.pack(pady=5)

        self.result_show = customtkinter.CTkEntry(self.app, width=300, justify="center")
        self.result_show.pack(pady=5)

        result_label = customtkinter.CTkLabel(self.app, text="Current Bidding Price For Item:")
        result_label.pack(pady=10)

        self.result_bid = customtkinter.CTkEntry(self.app, justify="center")
        self.result_bid.pack(pady=5)

        self.exit_button = customtkinter.CTkButton(self.app, text='Exit', command=self.destroy_window)
        self.exit_button.pack(pady=(20,0))

    def destroy_window(self):
        self.app.destroy()
        main_screen()  

    def collection(self):
        Andrew = random.choice([True, False])
        print(Andrew)
        number_stat = self.bidding_price_entry.get()
        car_index_number = Car_Brand.index(self.product_name_combo_box.get())
        print(car_index_number)
        print(number_stat)
        if int(number_stat) > int(bid_competition[car_index_number]): 
            if Andrew == False:
                bid_competition[car_index_number] = number_stat
                bid_data[car_index_number] = number_stat
                self.result_entry.delete(0, 'end')
                self.result_show.delete(0, 'end')
                self.result_bid.delete(0, 'end')
                self.result_entry.insert(0, "Success!")
                self.result_show.insert(0, "Bid "+str(Car_Brand[car_index_number])+" Successful For $"+str(number_stat)+"!")
                self.result_bid.insert(0, "$"+str(bid_competition[car_index_number]))
                notify('From Andrew', 'You are just lucky...')

            else:
                bid_competition[car_index_number] = int(number_stat)+random.randint(100,1500)
                self.result_entry.delete(0, 'end')
                self.result_show.delete(0, 'end')
                self.result_bid.delete(0, 'end')
                self.result_entry.insert(0, "ERROR 404!!!")
                self.result_show.insert(0, "Andrew Has A Surprise For You!")
                self.result_bid.insert(0, "$"+str(bid_competition[car_index_number]))
                notify('From Andrew', 'I HAVE OUTBIDDED YOU. TRY AGAIN NEXT TIME HAHAH!')

        else:
            self.result_entry.delete(0, 'end')
            self.result_show.delete(0, 'end')
            self.result_bid.delete(0, 'end')
            self.result_entry.insert(0, "Failed. Please check!")
            self.result_bid.insert(0, "$"+str(bid_competition[car_index_number]))


#Check UI

class Status_Check:
    def __init__(self):
        bomb(Main_GUI)
        self.app = customtkinter.CTk()
        self.app.title("Bidding Application")
        self.app.geometry("700x500")
        self.app.minsize(700, 500)
        self.app.maxsize(700, 500)

        self.status_cash()

        self.app.mainloop()



    def status_cash(self):
        main_frame = customtkinter.CTkFrame(self.app, width=700, height=400)
        main_frame.pack_propagate(0)
        main_frame.pack(side='top')

        left_frame = customtkinter.CTkFrame(main_frame, width=350, height=400)
        left_frame.pack_propagate(0)
        left_frame.pack(side='left')

        title_label = customtkinter.CTkLabel(left_frame, text="Sales Status View", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        inside_left_frame = customtkinter.CTkFrame(left_frame)
        inside_left_frame.pack(padx=20, pady=20)


        product_name_label = customtkinter.CTkLabel(inside_left_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, padx=10, pady=5)


        self.product_name_combo_box = customtkinter.CTkComboBox(inside_left_frame, values=Car_Brand)
        self.product_name_combo_box.grid(row=0, column=1, padx=10, pady=5)


        submit_button = customtkinter.CTkButton(left_frame, text="Check Status", command=self.search)
        submit_button.pack(pady=10)

        result_label = customtkinter.CTkLabel(left_frame, text="Current Status:")
        result_label.pack(pady=10)

        self.result_entry = customtkinter.CTkEntry(left_frame, width=200, justify="center")
        self.result_entry.pack(pady=5)

        right_frame = customtkinter.CTkFrame(main_frame, width=350, height=400)
        right_frame.pack_propagate(0)
        right_frame.pack(side='right')


        title_label = customtkinter.CTkLabel(right_frame, text="Current Bidding Status", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)


        inside_right_frame = customtkinter.CTkFrame(right_frame)
        inside_right_frame.pack(padx=20, pady=20)

        product_name_label = customtkinter.CTkLabel(inside_right_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, padx=10, pady=5)


        self.product_name_combo_box2 = customtkinter.CTkComboBox(inside_right_frame, values=Car_Brand)
        self.product_name_combo_box2.grid(row=0, column=1, padx=10, pady=5)


        submit_button = customtkinter.CTkButton(right_frame, text="Check Status", command=self.search2)
        submit_button.pack(pady=10)

        result_label = customtkinter.CTkLabel(right_frame, text="Current Status:")
        result_label.pack(pady=10)

        self.result_entry2 = customtkinter.CTkEntry(right_frame, width=300, justify="center")
        self.result_entry2.pack(pady=5)

        self.exit_button = customtkinter.CTkButton(self.app, text='Exit', command=self.destroy_window)
        self.exit_button.pack(pady=(20,0))






    def search(self):
        car_index_number = Car_Brand.index(self.product_name_combo_box.get())
        if sold[car_index_number] == False:
            self.result_entry.delete(0, 'end')
            self.result_entry.insert(0,str(Car_Brand[car_index_number]+" Is On Stock!"))
        else:
            self.result_entry.delete(0, 'end')
            self.result_entry.insert(0,str(Car_Brand[car_index_number]+" Is Not On Stock!"))



    def search2(self):
        car_index_number = Car_Brand.index(self.product_name_combo_box2.get())
        if bid_data[car_index_number] == 0:
            self.result_entry2.delete(0, 'end')
            self.result_entry2.insert(0,str(Car_Brand[car_index_number]+" Has Not Been Bidded By User!"))
        else:
            self.result_entry2.delete(0, 'end')
            self.result_entry2.insert(0,str(Car_Brand[car_index_number]+" Has Been Bidded By User!"))

    def destroy_window(self):
        self.app.destroy()
        main_screen()


# Personal Crap

class Personal:
    def __init__(self):
        bomb(Main_GUI)
        self.app = customtkinter.CTk()
        self.app.title("Bidding Application")
        self.app.geometry("700x500")
        self.app.minsize(700, 500)
        self.app.maxsize(700, 500)

        self.cucu()

        self.app.mainloop()



    def cucu(self):
        main_frame = customtkinter.CTkFrame(self.app, width=700, height=400)
        main_frame.pack_propagate(0)
        main_frame.pack(side='top')

        left_frame = customtkinter.CTkFrame(main_frame, width=350, height=400)
        left_frame.pack_propagate(0)
        left_frame.pack(side='left')

        title_label = customtkinter.CTkLabel(left_frame, text="Personal Stats", font=("Arial", 20, "bold"))
        title_label.pack(pady=15)

        customtkinter.CTkLabel(left_frame, text="Cars Bidded: ").pack(pady=8)

        for i in range(len(bid_data)):
            if int(bid_data[i]) > 0:
                if sold[i] == False:
                    customtkinter.CTkLabel(left_frame, text=Car_Brand[i]).pack()
                else:
                    pass
            else:
                pass

        customtkinter.CTkLabel(left_frame, text="Cars Purchased: ").pack(pady=8)

        for i in range(len(sold)):
            if int(sold[i]) == True:
                customtkinter.CTkLabel(left_frame, text=Car_Brand[i]).pack()
            else:
                pass


        customtkinter.CTkLabel(left_frame, text="Outgoing Transactions: $"+str(topay)).pack(pady=5)



        right_frame = customtkinter.CTkFrame(main_frame, width=350, height=400)
        right_frame.pack_propagate(0)
        right_frame.pack(side='right')


        title_label = customtkinter.CTkLabel(right_frame, text="Purchase", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)


        inside_right_frame = customtkinter.CTkFrame(right_frame)
        inside_right_frame.pack(padx=20, pady=20)

        product_name_label = customtkinter.CTkLabel(inside_right_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, padx=10, pady=5)




        self.product_name_combo_box2 = customtkinter.CTkComboBox(inside_right_frame, values=Car_Brand)
        self.product_name_combo_box2.grid(row=0, column=1, padx=10, pady=5)


        submit_button = customtkinter.CTkButton(right_frame, text="Purchase", command=self.buy)
        submit_button.pack(pady=10)

        result_label = customtkinter.CTkLabel(right_frame, text="Status:")
        result_label.pack(pady=10)

        self.result_entry2 = customtkinter.CTkEntry(right_frame, width=300, justify='center')
        self.result_entry2.pack(pady=5)

        self.exit_button = customtkinter.CTkButton(self.app, text='Exit', command=self.destroy_window)
        self.exit_button.pack(pady=(20,0))

    def buy(self):
        global topay
        car_index_number = Car_Brand.index(self.product_name_combo_box2.get())
        if int(bid_data[car_index_number]) != 0 and sold[car_index_number] == False:
            topay+=int(bid_data[car_index_number])
            sold[car_index_number] = True
            self.result_entry2.delete(0, 'end')
            self.result_entry2.insert(0,"Purchase "+str(Car_Brand[car_index_number])+" Successful for $"+str(bid_data[car_index_number]))
        else:
            self.result_entry2.delete(0, 'end')
            self.result_entry2.insert(0,"Purchase Failed. Check Bid Or Sales Status")

    def destroy_window(self):
        self.app.destroy()
        main_screen()

#Bid Bot [For later]

class bid_bot:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("Bidding Application")
        self.app.geometry("700x500")
        self.app.minsize(700, 500)
        self.app.maxsize(700, 500)

        self.bot_core()

        self.app.mainloop()

    def bot_core(self):
        title_label = customtkinter.CTkLabel(self.app, text="Under Construction", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)



#Cars

def Porsche():
    global vip_screen
    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    porsche_data = Image.open("porsche-model.png")


    porsche = CTkImage(dark_image=porsche_data, light_image=porsche_data, size=(648,364))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=porsche, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Porsche 911 GT3RS", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: Approximately 520 horsepower", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: Naturally aspirated flat-six", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Approximately 200 mph (322 km/h)", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[0]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

    vip_screen.mainloop()

def Mercedes():
    global vip_screen
    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    mercedes_data = Image.open("mercedes.png")
    mercedes = CTkImage(dark_image=mercedes_data, light_image=mercedes_data, size=(540,303))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=mercedes, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Mercedes-AMG ONE", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: Over 1,000 hp.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: Turbocharged 1.6-liter V6 hybrid.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Exceeds 217 mph (350 km/h).", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[1]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

def Triumph():
    global vip_screen

    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    triumph_data = Image.open("triumph.png")


    triumph = CTkImage(dark_image=triumph_data, light_image=triumph_data, size=(518,388))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=triumph, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Triumph Stag", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: Around 145 hp.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: 3.0-liter V8 engine.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Approximately 120 mph (193 km/h).", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[2]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

def Peugeot():
    global vip_screen

    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    peugeot_data = Image.open("peugeot.png")


    peugeot = CTkImage(dark_image=peugeot_data, light_image=peugeot_data, size=(552,290))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=peugeot, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Peugeot 3008 AT", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: 165 horsepower", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: Turbocharged inline-four petrol engine", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Approximately 124 mph (200 km/h)", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[3]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

def Honda():
    global vip_screen

    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    honda_data = Image.open("honda.png")


    honda = CTkImage(dark_image=honda_data, light_image=honda_data, size=(609, 300))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=honda, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Honda Civic", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: Around 158 horsepower.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: Inline-four petrol engine.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Approximately 125 mph (201 km/h)", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[4]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

def Mini():
    global vip_screen

    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    mini_data = Image.open("mini.png")


    mini = CTkImage(dark_image=mini_data, light_image=mini_data, size=(448, 290))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=mini, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Mini Cooper S", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: Around 189 horsepower.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: Turbocharged inline-four petrol engine.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Approximately 146 mph (235 km/h).", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[5]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

def Jaguar():
    global vip_screen

    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    jaguar_data = Image.open("jaguar.png")


    jaguar = CTkImage(dark_image=jaguar_data, light_image=jaguar_data, size=(524, 350))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=jaguar, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Jaguar F-Type", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: 380 horsepower.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: Turbocharged inline-four petrol engine.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Approximately 171 mph (275 km/h).", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[4]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

def Aston():
    global vip_screen

    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    aston_data = Image.open("aston.png")


    aston = CTkImage(dark_image=aston_data, light_image=aston_data, size=(864, 486))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=aston, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Aston Martin Valkyrie", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: Over 1,000 horsepower.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: 6.5-liter naturally aspirated V12 engine", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Estimated to exceed 250 mph (402 km/h)", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[7]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

def BMW():
    global vip_screen

    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    bmw_data = Image.open("bmw.png")


    bmw = CTkImage(dark_image=bmw_data, light_image=bmw_data, size=(644, 388))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=bmw, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="BMW i8 Roadster", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: 369 horsepower", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: 1.5-liter three-cylinder petrol engine combined with an electric motor", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Electronically limited to 155 mph (250 km/h)", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[8]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))

def Ford():
    global vip_screen

    vip_screen = CTk()
    vip_screen.geometry('800x600')
    vip_screen.resizable(0,0)
    vip_screen.title("Porsche")
    #---
    ford_data = Image.open("ford.png")


    ford = CTkImage(dark_image=ford_data, light_image=ford_data, size=(576, 324))
    #---

    Picture_Frame = customtkinter.CTkFrame(master=vip_screen, width=800, height=300, fg_color="#ffffff")
    Picture_Frame.pack_propagate(0)
    Picture_Frame.pack(side="top")
    customtkinter.CTkLabel(master=Picture_Frame, text="", text_color="#601E88", font=("Arial Bold", 20),image=ford, compound='center').pack()
    #---
    customtkinter.CTkLabel(master=vip_screen, text="Ford GT LM Edition", text_color="#601E88", font=("Arial Bold", 24)).pack(pady=(5,10))
    customtkinter.CTkLabel(master=vip_screen, text="Horsepower: 647 horsepower", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Engine Type: 3.5-liter twin-turbocharged EcoBoost V6 engine.", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Top Speed: Approximately 216 mph (348 km/h)", text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkLabel(master=vip_screen, text="Reserve Price: $"+str(reserve_price[8]), text_color="#601E88", font=("Arial Bold", 18)).pack(pady=(0,8))
    customtkinter.CTkButton(master=vip_screen, text="Exit", fg_color=("#DB3E39", "#821D1A"), command=car_info).pack(pady=(20,20))
#2 Main UI





def main_screen():

    global Main_GUI
    #--- Bug Fix
    username = temp_user.get()
    if username == "":
        username = "ANONYMUS"
    userid = temp_id.get()
    if len(userid) == 4:
        pass
    else:
        userid = random.randint(1000,9999)
    if 'app' in globals():
        try:
            app.destroy()
        except Exception:
            pass
    if 'car_screen' in globals():
        try:
            car_screen.destroy()
        except Exception:
            pass
    #--- User gatherer
    #---
    Main_GUI = CTk()
    Main_GUI.geometry('600x800')
    Main_GUI.resizable(0,0)
    Main_GUI.title("Car_Auction.EXE")
    #----p
    customtkinter.CTkLabel(master=Main_GUI, text="Welcome "+str(username)+" To The Aspida Annual Car Auction", font=("Comic Sans MS", 18),  text_color="#601E88", pady=30).pack()
    customtkinter.CTkLabel(master=Main_GUI, text="User ID: "+str(userid), font=("Comic Sans MS", 24),  text_color="#601E88", pady=30).pack()
    customtkinter.CTkButton(master=Main_GUI, fg_color=("#DB3E39", "#821D1A"), text="Personal Dashboard", command=Personal).pack(pady=(0,30))
    customtkinter.CTkButton(master=Main_GUI, fg_color=("#DB3E39", "#821D1A"), text="Cars", command=car_display).pack(pady=(0,30))
    customtkinter.CTkButton(master=Main_GUI, fg_color=("#DB3E39", "#821D1A"), text="Car Details", command=car_info).pack(pady=(0,30))
    customtkinter.CTkButton(master=Main_GUI, fg_color=("#DB3E39", "#821D1A"), text="Car Status", command=Status_Check).pack(pady=(0,30))
    customtkinter.CTkButton(master=Main_GUI, fg_color=("#DB3E39", "#821D1A"), text="Bid", command=BiddingApp).pack(pady=(0,30))
    customtkinter.CTkButton(master=Main_GUI, fg_color=("#DB3E39", "#821D1A"), text="Bid Bot", command=bid_bot).pack(pady=(0,30))
    customtkinter.CTkButton(master=Main_GUI, fg_color=("#DB3E39", "#821D1A"), text="Price Board", command=PriceBoard).pack(pady=(0,30))
    customtkinter.CTkButton(master=Main_GUI, fg_color=("#DB3E39", "#821D1A"), text="Exit", command=nuke).pack(pady=(0,30))
    #---
    Main_GUI.mainloop()


#Login Screen-----------------------

global app


app = CTk()
app.geometry("600x480")
app.resizable(0,0)
app.title("Andrew's Homework Folder")

side_img_data = Image.open("Dragos_Logo.webp")
email_icon_data = Image.open("email-icon.png")
password_icon_data = Image.open("password-icon.png")
google_icon_data = Image.open("google-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17,17))

temp_user = customtkinter.StringVar(master=app, value='')
temp_id = customtkinter.StringVar(master=app, value='')

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = customtkinter.CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

customtkinter.CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
customtkinter.CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

customtkinter.CTkLabel(master=frame, text="Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
customtkinter.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", textvariable=temp_user).pack(anchor="w", padx=(25, 0))



customtkinter.CTkLabel(master=frame, text="4 Digit ID [Leave Blank If New]: ", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
customtkinter.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", textvariable=temp_id).pack(anchor="w", padx=(25, 0))

customtkinter.CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=main_screen).pack(anchor="w", pady=(40, 0), padx=(25, 0))

customtkinter.CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9), text_color="#601E88", width=225, image=google_icon, command=rick).pack(anchor="w", pady=(20, 0), padx=(25, 0))




app.mainloop()

