import tkinter as tk
import math


confidence_intervals = [80, 85, 90, 95, 99, 99.5, 99.9]
z_scores = [1.282, 1.440, 1.645, 1.960, 2.576, 2.807, 3.291]
z_score = 0.0
z_dict = {}
sample_size = 0 #input("What is the Sample Size?")
proportion_percentage = 0.0 #for now?
population_size = 0 #input("What is the Population Size?")
moe = 0


for a in range(7):
    z_dict[confidence_intervals[a]] = z_scores[a]

    #z_dict[i] = z_score[i]
#print(z_dict)

window = tk.Tk()
window.title("Margin of Error Calculator")


moe_label = tk.Label(
    text="Margin of Error",
    height=5,
    width=25,
    bg = 'green',
    fg = 'orange'
)

population_label = tk.Label(
    text="Population Size:",
    height=2,
    width=25
)

sample_label = tk.Label(
    text="Sample Size:",
    height=2,
    width=25
)

proportion_label = tk.Label(
    text="Proportion Percentage:",
    height=2,
    width=25
)

moe_value_label = tk.Label(
    text = 'moe',
    height = 2,
    width =25,
    bg = 'blue',
    fg = 'orange'
)

population_size_entry = tk.Entry(
    width=25
)

sample_size_entry = tk.Entry(
    width=25
)

proportion_percentage_entry = tk.Entry(
    width=25
)

z_options = tk.DoubleVar()
z_score_dropdown = tk.OptionMenu(window,
                                 z_options,
                                 *confidence_intervals,
                                 )
z_score_dropdown.config(width = 25, height = 2)
z_options.set(80)



clear_button = tk.Button(
    text = "Clear All",
    height = 2,
    width = 25,

)

def packs_east():
    moe_label.grid(row = 0, column = 0, columnspan = 2)

    population_label.grid(row = 1)
    population_size_entry.grid(row =1, column =1)
    population_size_entry.insert(0,'0')

    sample_label.grid(row = 2, column = 0)
    sample_size_entry.grid(row = 2, column = 1)
    sample_size_entry.insert(0, '0')

    proportion_label.grid(row = 3, column = 0)
    proportion_percentage_entry.grid(row = 3, column = 1)
    proportion_percentage_entry.insert(0, '0.5')


    z_score_dropdown.grid(row = 4, column =0)

    calculate_button.grid(row = 5, column = 0)
    moe_value_label.grid(row = 5, column = 1,)



def calculate_moe():
    population_size = population_size_entry.get()
    population_size = float(population_size)

    sample_size = sample_size_entry.get()
    sample_size = float(sample_size)

    proportion_percentage = proportion_percentage_entry.get()
    proportion_percentage = float(proportion_percentage)

    z_score = z_dict.get(z_options.get())
    z_score = float(z_score)


    try:
        numerator = math.sqrt(proportion_percentage * (1 - proportion_percentage))
        denom1 = (population_size - 1) * sample_size
        denom2 = population_size - sample_size
        denominator = math.sqrt(denom1 / denom2)
        moe = (z_score * numerator) / denominator
        moe = moe*100
        moe_value_label.config(text = str(moe))
        values = [population_size, sample_size, proportion_percentage, z_score, moe]
        print(
            "Population Size:\t", str(population_size) +"\n" +
            "Sample Size:\t", str(sample_size) +"\n" +
            "Proportion Percentage:\t", str(proportion_percentage) +"\n" +
            "Z-Score:\t", str(z_score) +"\n" +
            "Margin of Error:\t", str(moe) +"\n" +
            "----------------------------------------------------------"
            )
    except:
        pass # pass it to gods hands because i can't even


calculate_button = tk.Button(
    text="Calculate!",
    height=4,
    width=25,
    command = calculate_moe
)




packs_east()
calculate_moe()
window.mainloop()



