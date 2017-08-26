import os
from os import path
import time
import glob
import re
import datetime

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


#Change These
RSSFile = '/var/www/html/rss2/LNIL.xml'
RSSFeedTitle = 'Late Nights with Iain Lee'
RSSFeedDescription = 'Late Nights with Iain Lee Podcasts RSS Feed - WAN Version'
FilePath = '/var/www/html/Radio/LateNightsIainLee/'
FileType = '*.mp3'
RSSImage = 'http://sammarkham.club/rss/images/lnil.jpg'
FileDirWeb = 'http://sammarkham.club/Radio/LateNightsIainLee/'
#Change this to correct the way files are sorted
ReverseEntries = 1                          

#Print Config
print ' RSSFile: %s\n RSSFeedTitle: %s\n RSSFeedDescription: %s\n FilePath: %s\n FileType: %s\n RSSImage: %s\n' % (RSSFile, RSSFeedTitle, RSSFeedDescription, FilePath, FileType, RSSImage)

#Get Last updated 
Time = (time.strftime("%H:%M:%S"))
Date = (time.strftime("%d/%m/%Y"))
lastupdated = ('- last updated at: %s on %s') % (Time, Date)


#Get and sort items
FilePathAndFileType = ('%s%s') % (FilePath,FileType)
#print FilePathAndFileType
FileLocations = sorted(glob.glob(FilePathAndFileType), key=os.path.getmtime)
#print FileLocations


#Correctly sort the items
if ReverseEntries == 1:
    FileLocations = sorted(FileLocations, reverse=True)
else:
    FileLocations = sorted(FileLocations)


#Start of File
RSSFileName = open(RSSFile, "w")
RSSStart = '<?xml version="1.0" encoding="utf-8"?>\n<rss version="2.0">\n<channel>\n<title>%s</title>\n<description>%s\n%s</description>/n<image>\n<url>%s</url>\n<title>Feed Image</title>\n<link>%s</link>\n</image>\n' % (RSSFeedTitle, RSSFeedDescription, lastupdated, RSSImage, RSSImage)
RSSFileName.write(RSSStart)
print RSSStart
ItemStart = '\n\n<item>'
ItemEnd = '</item>'


FileNames=[]
ItemCount = 0
for item in FileLocations:
    FileName = re.search(r'[^/]+$' , item)
    FileName = FileName.group(0)
    #print FileName
    url = "%s%s" % (FileDirWeb, FileName)
    #print url
    
    Dates = re.findall(r'([0-9]+)', FileName)
    #print Dates
    Year = int(Dates[0])
    Month = int(Dates[1])
    Day = int(Dates[2])
    #print '%s-%s-%s' % (Year, Month, Day)

    ModDate = '%s-%s-%s' % (Year, Month, Day)
    ModDate = datetime.datetime.strptime(ModDate, "%Y-%m-%d")    
    ModDate = ModDate.strftime("%a %b %d %Y")
    print ModDate


    Enclosure = '\n  <enclosure url="%s"\n   type="audio/mpeg" />' % url
    TitleName = '\n  <title>%s</title>' % FileName
    Link = '\n  <link>%s</link>' % url
    pubDate = '\n  <pubDate>%s 22:00</pubDate>' % ModDate
    GUID = '\n  <GUID>http://sammarkham.club/Radio/lnil/%s</GUID>' % FileName
    Description = '\n  <description>Iain Lee Podcast: %s</description>\n\n' % FileName


#Write Item to File
    RSSFileName.write(ItemStart)
    RSSFileName.write(TitleName)
    RSSFileName.write(Link)
    RSSFileName.write(Enclosure)
    RSSFileName.write(GUID)
    RSSFileName.write(pubDate)
    RSSFileName.write(Description)
    RSSFileName.write(ItemEnd)

#Print Item to console
    print ItemStart
    print TitleName
    print Link
    print Enclosure
    print GUID
    print pubDate
    print Description
    print ItemEnd

    ItemCount == ItemCount + 1


#Write end contents of RSS File
RSSEND = '\n\n\n</channel>\n</rss>' 
RSSFileName.write("\n\n\n</channel>\n</rss>")
print "\n\n\n</channel>\n</rss>"
RSSFileName.close()
