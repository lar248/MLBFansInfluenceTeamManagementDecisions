
import csv
from os import path, listdir, getcwd
import pandas as pd

def exportPlayerStats():
	allUserNameData = []
	for userName in listdir("Royals/"):
		if userName != '.DS_Store':
			# userName = '_KrisMoran_'
			file_path_string = "Royals/"+userName
			filename = open(file_path_string)
			df = pd.read_csv(filename)
			saved_column = df.text
			playerKeywords = ['Zobrist', 'benzobrist18', 'zobrist']
			teamKeywords = ['Royals', 'royals']
			teamRelatedTweets = 0
			weightOfRelationship = 0
			lastNameCount = 0
			twitterHandleCount = 0
			hashtagCount = 0
			for i in range(len(saved_column)):
				if any(y in saved_column[i] for y in teamKeywords):
					teamRelatedTweets += 1
				if any(x in saved_column[i] for x in playerKeywords):
					weightOfRelationship += 1
				if playerKeywords[0] in saved_column[i]:
					lastNameCount += 1
				if playerKeywords[1] in saved_column[i]:
					twitterHandleCount += 1
				if playerKeywords[2] in saved_column[i]:
					hashtagCount += 1
			allUserNameData.append([userName, teamRelatedTweets, weightOfRelationship, lastNameCount, twitterHandleCount, hashtagCount])
			# print userNameData
	print allUserNameData
	# outUserNameData = [[userName, teamRelatedTweets, weightOfRelationship, lastNameCount, twitterHandleCount, hashtagCount] for user in allUserNameData]
	with open('royalsFansCounts.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(['userName', 'teamRelatedTweets', 'weightOfRelationship', 'lastNameCount', 'twitterHandleCount', 'hashtagCount'])
		writer.writerows(allUserNameData)

def exportRelevantTweets():
	allUserNameData = []
	for userName in listdir("Mets/"):
		if userName != '.DS_Store':
			# userName = '_KrisMoran_'
			file_path_string = "Mets/"+userName
			filename = open(file_path_string)
			df = pd.read_csv(filename)
			saved_column = df.text
			keywords = ['Cespedes', 'ynscspds', 'KeepYo']
			for i in range(len(saved_column)):
				if any(y in saved_column[i] for y in keywords):
					allUserNameData.append([userName, saved_column[i]])
			# print userNameData
	# print allUserNameData
	# outUserNameData = [[userName, teamRelatedTweets, weightOfRelationship, lastNameCount, twitterHandleCount, hashtagCount] for user in allUserNameData]
	with open('metsRelevantTweets.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(['userName', 'relevantTweets'])
		writer.writerows(allUserNameData)

if __name__ == '__main__':
	# exportPlayerStats()
	exportRelevantTweets()
