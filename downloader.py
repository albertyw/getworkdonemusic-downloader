import soundcloud
import urllib
import GetWorkDoneMusic

client = soundcloud.Client(client_id='')

def get_url(track_url):
    # fetch track to stream
    track = client.get('/resolve', url=track_url)
    
    # get the tracks streaming URL
    stream_url = client.get(track.stream_url, allow_redirects=False)
    
    # print the tracks stream URL
    return stream_url.location
    

fast, faster = GetWorkDoneMusic.music()
not_found = {}

for track_url, track_name in fast.items():
    print track_name
    print track_url
    try:
        stream_url = get_url(track_url)
        print stream_url
        urllib.urlretrieve(stream_url, "fast/"+track_name+".mp3")
    except:
        print "NOT FOUND"
        not_found[track_url] = track_name
    print ""

for track_url, track_name in faster.items():
    print track_name
    print track_url
    try:
        stream_url = get_url(track_url)
        print stream_url
        urllib.urlretrieve(stream_url, "faster/"+track_name+".mp3")
    except:
        print "NOT FOUND"
        not_found[track_url] = track_name
    print ""

print ""
print ""
for track_url, track_name in not_found.items():
    print track_name
    print track_url
    print ""
