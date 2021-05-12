import requests

#function takes in the name of the animal as a string and gives back a list of strings in the form of "can ____"

def getCapable(animal):
    capabilities = []
    #GET request sent to the API, specify the query, animal name, and relation (capable of)
    req = 'http://api.conceptnet.io/query?start=/c/en/' + animal + '&rel=/r/CapableOf&limit=1000'
    obj = requests.get('http://api.conceptnet.io/query?start=/c/en/horse&rel=/r/CapableOf&limit=1000').json()
    #Looping though the edges
    for edge in obj['edges']:
        #surface text is the readable text
        txt = str(edge['surfaceText'])
        #String manipulation to pull out the info we want
        txt = txt.replace('[[','')
        txt = txt.replace(']]','')
        txt = txt.replace('An activity ','')
        txt = txt.replace('do is ','')
        rep = 'A ' + animal + ' '
        txt = txt.replace(rep, '')
        rep = 'a ' + animal + ' '
        txt = txt.replace(rep, '')
        rep = 'The ' + animal + ' '
        txt = txt.replace(rep, '')
        capabilities.append(txt)
    return capabilities
