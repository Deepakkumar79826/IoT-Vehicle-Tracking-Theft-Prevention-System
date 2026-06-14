import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from reportlab.lib import colors

from docs.config import *

def generate_pdf():

    df = pd.read_csv(CSV_LOG_FILE)

    pdf = SimpleDocTemplate(PDF_REPORT)

    data = [df.columns.tolist()] + df.values.tolist()

    table = Table(data)

    table.setStyle(
        TableStyle([
            ('GRID',(0,0),(-1,-1),1,colors.black)
        ])
    )

    pdf.build([table])

    print("PDF Report Generated")