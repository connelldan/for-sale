from craigslist import CraigslistForSale

cl_h = CraigslistForSale(site='denver',
                         filters={'query': 'wurlitzer 200'})


for result in cl_h.get_results(sort_by='newest', geotagged=True):
    print(result)
