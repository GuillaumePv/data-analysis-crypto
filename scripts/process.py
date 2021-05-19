import processScripts.tweetProcess as tweetProcess
import processScripts.mergerProcess as merger
import processScripts.indicatorProcess as indicators
import processScripts.yahooProcess as yahoo

def processData():
    tweetProcess.cleanTweets()
    merger.mergeBinance()
    indicators.addIndicators()
    yahoo.getData()


if __name__ == '__main__':
    processData()
