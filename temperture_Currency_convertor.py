import tkinter as tk
from forex_python.converter import CurrencyRates

class ConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Converter App")

        # Temperature Converter
        self.temp_label = tk.Label(root, text="Temperature Converter", font=('Helvetica', 14))
        self.temp_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.temp_var = tk.StringVar()
        self.temp_entry = tk.Entry(root, textvariable=self.temp_var)
        self.temp_entry.grid(row=1, column=0, padx=5)

        self.temp_menu_var = tk.StringVar()
        self.temp_menu_var.set("Celsius")
        self.temp_menu = tk.OptionMenu(root, self.temp_menu_var, "Celsius", "Fahrenheit")
        self.temp_menu.grid(row=1, column=1, padx=5)

        self.temp_result_label = tk.Label(root, text="", font=('Helvetica', 12))
        self.temp_result_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.temp_convert_button = tk.Button(root, text="Convert", command=self.convert_temperature)
        self.temp_convert_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Currency Converter
        self.currency_label = tk.Label(root, text="Currency Converter", font=('Helvetica', 14))
        self.currency_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.currency_amount_var = tk.StringVar()
        self.currency_amount_entry = tk.Entry(root, textvariable=self.currency_amount_var)
        self.currency_amount_entry.grid(row=5, column=0, padx=5)

        self.currency_from_var = tk.StringVar()
        self.currency_from_var.set("USD")
        self.currency_from_menu = tk.OptionMenu(root, self.currency_from_var, "USD", "EUR", "GBP","INR")
        self.currency_from_menu.grid(row=5, column=1, padx=5)

        self.currency_to_var = tk.StringVar()
        self.currency_to_var.set("EUR")
        self.currency_to_menu = tk.OptionMenu(root, self.currency_to_var, "USD", "EUR", "GBP","INR")
        self.currency_to_menu.grid(row=6, column=1, padx=5)

        self.currency_result_label = tk.Label(root, text="", font=('Helvetica', 12))
        self.currency_result_label.grid(row=7, column=0, columnspan=2, pady=10)

        self.currency_convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.currency_convert_button.grid(row=8, column=0, columnspan=2, pady=5)

    def convert_temperature(self):
        try:
            temp = float(self.temp_var.get())
            unit = self.temp_menu_var.get()

            if unit == "Celsius":
                result = f"{temp} °C is {temp * 9/5 + 32:.2f} °F"
            else:
                result = f"{temp} °F is {(temp - 32) * 5/9:.2f} °C"

            self.temp_result_label.config(text=result)

        except ValueError:
            self.temp_result_label.config(text="Invalid input. Please enter a number.")

    def convert_currency(self):
        try:
            amount = float(self.currency_amount_var.get())
            from_currency = self.currency_from_var.get()
            to_currency = self.currency_to_var.get()

            c = CurrencyRates()
            rate = c.get_rate(from_currency, to_currency)
            result = f"{amount:.2f} {from_currency} is {amount * rate:.2f} {to_currency}"

            self.currency_result_label.config(text=result)

        except ValueError:
            self.currency_result_label.config(text="Invalid input. Please enter a number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
