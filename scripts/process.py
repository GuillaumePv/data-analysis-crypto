import processScripts.tweetProcess as tweetProcess
import processScripts.mergerProcess as merger
import processScripts.indicatorProcess as indicators

#tweetProcess.cleanTweets()
merger.mergeBinance()
indicators.addIndicators()
