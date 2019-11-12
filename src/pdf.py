import plotting
from fpdf import FPDF

def creaPDF(grouped_regions,year,region,type_c_o,data):
    '''
    Creates a PDF with the values of average price and total 
    volume sold that year and two graphs with the evolution of these 
    two during the 4 years.
    '''

    path_avg=plotting.imprimeavg(grouped_regions,region,type_c_o)
    path_tot=plotting.imprimetot(grouped_regions,region,type_c_o)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(70, 15, txt="El precio del aguacate de la variedad Hass", ln=1, align="C")
    pdf.set_font("Arial", size=8)
    pdf.multi_cell(0, 5, txt=textopdf(data,year,region,type_c_o))
    #pdf.ln(95)
    pdf.image(path_tot, x=20, y=60, w=100)
    pdf.set_font("Arial", size=12)
    #pdf.cell(200, 30, txt="Total Volume", ln=1)
    #pdf.ln(95)  # move 85 down

    pdf.image(path_avg, x=110, y=60, w=100)
    #pdf.cell(200, 100, txt="Average Price", ln=1)
    #pdf.ln(85)  # move 85 down

    pdf.output("../output/result.pdf")

    return

def textopdf(data,year,region,type_c_o):
    text="In the year {} in {}, the average price of a avocado was: {}, the average total volume sold per week was {}.\nAddress of supermarket:{}\nName of supermarket:{}".format(year,region,data[0],data[1],data[2],data[3])
    return text

