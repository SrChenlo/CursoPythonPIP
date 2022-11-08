import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels= ["A", "B", "C"]
    values = [34, 34, 34]

    fig, ax = pylot.subplots()
    ax.pie(values, labels=labels)
    pylot.savefig("pie.png")
    pylot.close()