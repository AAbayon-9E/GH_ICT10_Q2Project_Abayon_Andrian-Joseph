# yes
from pyscript import display, document


def grades(e):

    grade1 = document.getElementById('Math').value
    grade2 = document.getElementById('English').value
    grade3 = document.getElementById('ICT').value
    grade4 = document.getElementById('Science').value
    grade5 = document.getElementById('Filipino').value
    grade6 = document.getElementById('PE').value

    gwa = round((float(grade1) + float(grade2) + float(grade3) + float(grade4) + float(grade5) + float(grade6)) / 6, 2)

    lname = document.getElementById("input2").value
    fname = document.getElementById("input1").value

    display(f'Name: {fname} {lname}', target='output')
    display (f'GWA:{gwa}', target ='output') 