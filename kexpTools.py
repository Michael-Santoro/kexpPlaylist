'''KEXP Tools:
   Framework to help with the scraping of information from the kexp API
   Michael Santoro - michael.santoro@du.edu'''

## Imports ##
import requests
import pandas as pd 


class kexp:
    '''class for helper function tools for working with the kexp api interface'''
    def __init__(self):
        self.hosts = pd.read_csv('data/djData.csv',index_col=0)
        self.programs = pd.read_csv('data/programData.csv',index_col=0)
        self.rootAPI = 'https://api.kexp.org/v2/'

    def getShowsYear(self, year):
        '''function gets all of the shows for that year and returns a dataframe'''
        rootAddress = f'https://api.kexp.org/v2/shows/?start_time_after={year}-01-01T00:00:00&start_time_before={year+1}-01-01T00:00:00'
        shows = requests.get(rootAddress)
        pages = 20* round(shows.json()['count']/20)

        showsDict = {'id':[],
             'program_id':[],
             'hosts_ids':[],
             'program_name':[],
             'start_time':[]}
        for i in range(0,pages,20):
            print(f'fetching: {i}')
            shows = requests.get(rootAddress + f'&offset={i}')
            for entry in shows.json()['results']:
                showsDict['id'].append(entry['id'])
                showsDict['program_id'].append(entry['program'])
                showsDict['hosts_ids'].append(entry['hosts'])
                showsDict['program_name'].append(entry['program_name'])
                showsDict['start_time'].append(entry['start_time'])
        return pd.DataFrame(showsDict)

    def getShowsDay(self, year, month, day):
        '''function gets all of the shows for that year, month, day, and returns a dataframe'''
        rootAddress = f'https://api.kexp.org/v2/shows/?start_time_after={year}-{str(month).zfill(2)}-{str(day).zfill(2)}T00:00:00&start_time_before={year}-{str(month).zfill(2)}-{str(day+1).zfill(2)}T00:00:00'
        print(f'Root Address: {rootAddress}')
        shows = requests.get(rootAddress)
        pages = 20*round(shows.json()['count']/20)
        print(f'pages: {pages}')
        showsDict = {'id':[],
            'program_id':[],
            'hosts_ids':[],
            'program_name':[],
            'start_time':[]}
        if pages == 0:
            address = rootAddress
            print(f'fetching: {address}')
            shows = requests.get(address)
            for entry in shows.json()['results']:
                showsDict['id'].append(entry['id'])
                showsDict['program_id'].append(entry['program'])
                showsDict['hosts_ids'].append(entry['hosts'])
                showsDict['program_name'].append(entry['program_name'])
                showsDict['start_time'].append(entry['start_time'])
        else:
            for i in range(0,pages,20):
                address = rootAddress + f'&offset={i}'
                print(f'fetching: {address}')
                shows = requests.get(address)
                for entry in shows.json()['results']:
                    showsDict['id'].append(entry['id'])
                    showsDict['program_id'].append(entry['program'])
                    showsDict['hosts_ids'].append(entry['hosts'])
                    showsDict['program_name'].append(entry['program_name'])
                    showsDict['start_time'].append(entry['start_time'])
        return pd.DataFrame(showsDict)

    def getSongsHour(self, year, month, day, hour, t_offset):
        '''function gets all the songs played that hour'''
        playsDict = {'airdate':[],
                     'song':[],
                     'artist':[],
                     'album':[],
                     'labels':[],
                     'release_date':[],
                     'is_live':[]}

        url = 'https://api.kexp.org/v2/plays/'
        params = {'airdate_after':f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}T{str(hour).zfill(2)}:00:00-{str(t_offset).zfill(2)}:00',
                'airdate_before':f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}T{str(hour+1).zfill(2)}:00:00-{str(t_offset).zfill(2)}:00',
                'offset':0}             
        print(f'URL Address: {url}')
        for i in range(0,120,20):
            params['offset'] = i
            print(f'fetching: {params}')
            plays = requests.get(url = url, params = params)
            results = plays.json()['results']
            if results:
                for entry in results:
                    print(entry)
                    print(entry['play_type'] != 'airbreak')
                    if entry['play_type'] != 'airbreak':
                        playsDict['airdate'].append(entry['airdate'])
                        playsDict['song'].append(entry['song'])
                        playsDict['artist'].append(entry['artist'])
                        playsDict['album'].append(entry['album'])
                        playsDict['labels'].append(entry['labels'])
                        playsDict['release_date'].append(entry['release_date'])
                        playsDict['is_live'].append(entry['is_live'])
            else:
                break
            print(playsDict)
        return pd.DataFrame(playsDict)