# yeeeygfywf
from pyscript import display, document


def my_club(e):
    Club1 = document.getElementById("Art").value
    Club2 = document.getElementById("History").value
    Club3 = document.getElementById("Book").value
 

Club1 = {
    'Art Club' 
    'Description':'Bring your imaginations to life and let them soar free for the world to see.',
    'Meeting time':'10:30 am',
    'Location':'Arts and Music room',
    'Club moderator':'Mr. Whatsit',
    'Number of members':'12'
}

def my_club(e):
    Club2 = document.getElementById("History").value
   

Club2 = {
    'History Club' 
    'Description':'Travel back in time and foresee the future.',
    'Meeting time':'1:00 pm',
    'Location':'Library attic',
    'Club moderator':'Diggie',
    'Number of members':'7'
}

def my_club(e):
    Club3 = document.getElementById("Book").value

Club3 = {
    'Book Club' 
    'Description':'Share stories and wonder with people!',
    'Meeting time':'2:30 pm',
    'Location':'Library attic',
    'Club moderator':'Bookworm',
    'Number of members':'12'
}




display((Club1), target='output')
display((Club2), target='output')
display((Club3), target='output')

